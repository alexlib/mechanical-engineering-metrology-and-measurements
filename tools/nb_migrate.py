#!/usr/bin/env python3
"""Rewrite Jupyter notebooks so ``marimo convert`` produces runnable notebooks.

marimo is stricter than Jupyter in ways that matter for this book:

* ``import *`` is rejected outright -> expand to explicit imports.
* Cell magics (``%pylab inline``, ``%timeit``) have no equivalent -> strip or
  evaluate, depending on which one it is.
* A notebook may not rebind a name across two cells, so we never duplicate an
  import when inlining a helper module.
* Every name a cell reads must be produced by exactly one cell.

Each function here does one rewrite and returns notes about what it changed so
the driver can report them.
"""

from __future__ import annotations

import ast
import builtins
import importlib
import re
import warnings
from pathlib import Path

# Repo-root-relative asset paths move with the marimo-book layout.
PATH_REWRITES = [
    ("book/theory/fig/", "images/"),
    ("book/img/", "images/"),
    ("book/data/", "data/"),
    # ``../img/`` / ``fig/`` were relative to ``book/<chapter>/``
    ("../img/", "../images/"),
]

BUILTINS = set(dir(builtins)) | {"__name__", "__file__", "__doc__", "get_ipython"}

# Magics that only configure the environment and can simply be dropped.
DROP_MAGIC_LINE = re.compile(r"^\s*%(matplotlib|load_ext|autosave|precision)\b.*$")
# ``%pylab inline`` is shorthand for "import pylab's namespace"; rewrite it to
# the star import so ``expand_star_imports`` can resolve the bare names
# (``plot``, ``show``, ``xlabel``, ...) the rest of the notebook uses.
PYLAB_MAGIC = re.compile(r"^\s*%pylab\b.*$")
# ``%timeit expr`` -> ``expr`` (we keep the measurement out of a static build).
TIMEDIT_MAGIC = re.compile(r"^(\s*)%timeit\s+(.*)$")
# MATLAB-flavoured ``%`` comment blocks that leaked into a Python cell. ``%run``
# is excluded: ``inline_run_scripts`` handles it, and it must see the magic
# before it is turned into a comment.
PERCENT_COMMENT = re.compile(r"^(\s*)%(?P<magic>run\b)?(?!%)\s?(.*)$")


def rewrite_paths(text: str) -> str:
    for old, new in PATH_REWRITES:
        text = text.replace(old, new)
    return text


# --------------------------------------------------------------------------
# Syntactic analysis helpers
# --------------------------------------------------------------------------

def _bound_names(tree: ast.AST) -> set[str]:
    """Every name the given code binds (assignments, imports, defs, args...)."""
    bound: set[str] = set()

    def add_target(node: ast.AST) -> None:
        for n in ast.walk(node):
            if isinstance(n, ast.Name):
                bound.add(n.id)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                bound.add((a.asname or a.name).split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for a in node.names:
                bound.add(a.asname or a.name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bound.add(node.name)
            a = getattr(node, "args", None)
            if a is not None:
                for arg in [*a.posonlyargs, *a.args, *a.kwonlyargs]:
                    bound.add(arg.arg)
                if a.vararg:
                    bound.add(a.vararg.arg)
                if a.kwarg:
                    bound.add(a.kwarg.arg)
        elif isinstance(node, ast.Lambda):
            a = node.args
            for arg in [*a.posonlyargs, *a.args, *a.kwonlyargs]:
                bound.add(arg.arg)
            if a.vararg:
                bound.add(a.vararg.arg)
            if a.kwarg:
                bound.add(a.kwarg.arg)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Store, ast.Del)):
            bound.add(node.id)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            bound.add(node.name)
        elif isinstance(node, (ast.Global, ast.Nonlocal)):
            bound.update(node.names)
    return bound


def _loaded_names(tree: ast.AST) -> set[str]:
    return {n.id for n in ast.walk(tree) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}


def _attribute_roots(tree: ast.AST) -> set[str]:
    """Module roots referenced via attribute access, e.g. ``np.foo`` -> ``np``.

    Note this must *not* be folded into the bound set: ``np.log10(x)`` mentions
    ``np`` without importing it, and that is exactly the free name we want the
    star-import expander to resolve.
    """
    roots = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Attribute):
            cur: ast.AST = n
            while isinstance(cur, ast.Attribute):
                cur = cur.value
            if isinstance(cur, ast.Name):
                roots.add(cur.id)
    return roots


# Jupyter injects these into every cell's global namespace; a marimo cell has no
# such injection, so a bare reference has to become a real import. Only applied
# to names that are read but never bound anywhere in the notebook.
IMPLICIT_IMPORTS = {
    "np": "import numpy as np",
    "numpy": "import numpy as np",
    "plt": "import matplotlib.pyplot as plt",
    "pylab": "import pylab",
    "matplotlib": "import matplotlib",
    "mpl": "import matplotlib as mpl",
    "pl": "import pylab as pl",
    "random": "import numpy.random as random",
    "os": "import os",
    "sys": "import sys",
    "display": "from IPython.display import display",
    "Image": "from IPython.display import Image",
    "HTML": "from IPython.display import HTML",
    "Markdown": "from IPython.display import Markdown",
    "scipy": "import scipy",
    "stats": "from scipy import stats",
    "signal": "from scipy import signal",
    "interp1d": "from scipy.interpolate import interp1d",
    "fft": "from scipy import fft",
    "t": "from scipy.stats import t",
    "norm": "from scipy.stats import norm",
    "pearsonr": "from scipy.stats import pearsonr",
}


def _parses(source: str) -> ast.Module | None:
    """Parse ``source``, or return None. Escape-sequence warnings are noise."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        try:
            return ast.parse(source)
        except SyntaxError:
            return None


# Per-module repairs applied when a helper module is inlined, keyed by filename.
# value = (whole-word renames applied to the body, lines prepended to it).
INLINE_FIXUPS: dict[str, tuple[dict[str, str], list[str]]] = {
    # ``fft`` was the scipy.fft *module* here and is called as ``fft.fft(...)``;
    # the notebook imports ``fft`` as a function, so route it through numpy.
    "signal_processing.py": ({"fft": "np.fft"}, []),
    # ``random`` was random.random here, but the notebook uses the module.
    "create_random_data.py": (
        {"random": "_random"},
        ["from random import random as _random"],
    ),
}

# Names a star import must not supply, because the notebook needs a different
# binding. ``pylab.random`` resolves to ``numpy.random.random`` (the function),
# but the notebooks that use ``random.normal(...)`` mean the module.
STAR_NAME_BLOCKLIST: dict[str, set[str]] = {
    "pylab": {"random"},
}

# --------------------------------------------------------------------------
# Cell-type and magic fixups
# --------------------------------------------------------------------------

def raw_cells_to_code(nb: dict) -> list[str]:
    """Turn ``raw`` cells holding plotting code into real code cells.

    A raw cell never executed in Jupyter, so it has no imports and uses
    unqualified numpy/pyplot names. Qualify them against the two modules every
    notebook in this book already relies on.
    """
    notes = []
    bare = {
        "ones": "np.ones", "zeros": "np.zeros", "array": "np.array", "linspace": "np.linspace",
        "arange": "np.arange", "sqrt": "np.sqrt", "exp": "np.exp", "log": "np.log",
        "sin": "np.sin", "cos": "np.cos", "pi": "np.pi",
        "plot": "plt.plot", "figure": "plt.figure", "show": "plt.show",
        "subplots": "plt.subplots", "xlabel": "plt.xlabel", "ylabel": "plt.ylabel",
        "title": "plt.title", "legend": "plt.legend", "grid": "plt.grid",
    }
    for cell in nb["cells"]:
        if cell.get("cell_type") != "raw":
            continue
        src = "".join(cell["source"])
        lines = []
        for line in src.splitlines():
            for name, qualified in bare.items():
                line = re.sub(rf"(?<![\w.]){name}\s*\(", f"{qualified}(", line)
            lines.append(line)
        body = "\n".join(lines).strip()
        if not body:
            continue
        cell["cell_type"] = "code"
        cell["source"] = (
            "import numpy as np\nimport matplotlib.pyplot as plt\n" + body
        ).splitlines(keepends=True)
        cell["outputs"] = []
        cell["execution_count"] = None
        notes.append("raw cell promoted to code cell")
    return notes


def strip_magics(nb: dict) -> list[str]:
    """Remove or rewrite IPython magics that marimo cannot execute."""
    notes = []
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        out, changed = [], False
        for line in "".join(cell["source"]).splitlines(keepends=True):
            bare_line = line.rstrip("\n")
            if PYLAB_MAGIC.match(bare_line):
                changed = True
                out.append("from pylab import *\n")
                continue
            if DROP_MAGIC_LINE.match(bare_line):
                changed = True
                continue
            m = TIMEDIT_MAGIC.match(bare_line)
            if m:
                changed = True
                out.append(f"{m.group(1)}{m.group(2)}\n")
                continue
            m = PERCENT_COMMENT.match(bare_line)
            if m and not m.group("magic"):
                changed = True
                out.append(f"{m.group(1)}# {m.group(2)}\n".rstrip() + "\n")
                continue
            out.append(line)
        if changed:
            cell["source"] = out
            notes.append("magics stripped")
    return notes


def expand_symbol_declarations(nb: dict) -> list[str]:
    """Rewrite ``sympy.var('x,b,p')`` into an explicit tuple unpacking.

    ``sympy.var(...)`` binds names at runtime, which marimo's static analysis
    cannot see, so every later reference reads as an undefined name. The
    unpacking form binds them statically and means the same thing.
    """
    notes = []
    symbol_list = r"[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
    pattern = re.compile(rf"^(\s*)sympy\.var\(\s*['\"]({symbol_list})['\"]\s*\)\s*$")
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        out, changed = [], False
        for line in "".join(cell["source"]).splitlines(keepends=True):
            m = pattern.match(line.rstrip("\n"))
            if m:
                names = [n.strip() for n in m.group(2).split(",")]
                out.append(f"{m.group(1)}{', '.join(names)} = sympy.symbols({m.group(2)!r})\n")
                changed = True
                continue
            out.append(line)
        if changed:
            cell["source"] = out
            notes.append("sympy.var expanded to explicit unpacking")
    return notes


def markdown_images_in_code(nb: dict) -> list[str]:
    """Promote code cells that are really Markdown images to markdown cells."""
    notes = []
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"]).strip()
        if src and all(
            ln.lstrip().startswith("![") or not ln.strip() for ln in src.splitlines()
        ):
            cell["cell_type"] = "markdown"
            notes.append("image-only code cell promoted to markdown")
    return notes


# --------------------------------------------------------------------------
# Star imports -> explicit imports
# --------------------------------------------------------------------------

def _free_names(nb: dict) -> set[str]:
    """Names read but never bound anywhere in the notebook."""
    bound: set[str] = set(BUILTINS)
    loaded: set[str] = set()
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"])
        tree = _parses(src)
        if tree is None:
            # Unparsable cell: scan imports textually so we don't invent an
            # import for something the cell itself already binds.
            for m in re.finditer(r"^\s*(?:import|from)\s+.*$", src, re.M):
                bound.update(re.findall(r"[A-Za-z_]\w*", m.group(0)))
            continue
        bound |= _bound_names(tree)
        loaded |= _loaded_names(tree)
    return loaded - bound


def _first_code_cell(nb: dict) -> dict | None:
    for cell in nb["cells"]:
        if cell.get("cell_type") == "code":
            return cell
    return None


def add_missing_imports(nb: dict) -> tuple[list[str], list[str]]:
    """Import Jupyter's implicit globals that the notebook uses but never binds.

    Returns ``(notes, still_unresolved)``.
    """
    free = _free_names(nb)
    wanted: dict[str, str] = {}
    unresolved = []
    for name in sorted(free):
        if name in IMPLICIT_IMPORTS:
            # ``np`` and ``numpy`` both map to the same import; keep one.
            stmt = IMPLICIT_IMPORTS[name]
            key = stmt.split()[-1] if name in {"np", "numpy"} else name
            wanted[key] = stmt
        else:
            unresolved.append(name)
    if not wanted:
        return [], unresolved

    cell = _first_code_cell(nb)
    if cell is None:
        return [], unresolved
    lines = "".join(cell["source"]).splitlines(keepends=True)
    cell["source"] = ["\n".join(sorted(set(wanted.values()))) + "\n", *lines]
    return [f"added {len(wanted)} implicit import(s)"], unresolved


def expand_star_imports(nb: dict, search_modules: dict[str, str]) -> tuple[list[str], list[str]]:
    """Replace ``from M import *`` with explicit imports for the names used.

    Walks the whole notebook for names that are read but never bound, then
    resolves each against the star-imported modules (last import wins, matching
    Python's own semantics). Returns ``(notes, unresolved)``.
    """
    notes, unresolved = [], []

    star_modules: list[str] = []
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        tree = _parses("".join(cell["source"]))
        if tree is None:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and any(a.name == "*" for a in node.names):
                star_modules.append(node.module or "")

    if not star_modules:
        return notes, unresolved

    # Import the candidate namespaces once so we can look names up.
    # ``importlib.import_module`` (not ``__import__``) is required: the latter
    # returns the *top-level* package for a dotted name, so ``matplotlib.pyplot``
    # would resolve to ``matplotlib`` and lose every plotting symbol.
    namespaces: dict[str, set[str]] = {}
    for mod in star_modules:
        if mod in namespaces:
            continue
        try:
            namespaces[mod] = set(dir(importlib.import_module(mod)))
        except Exception:  # pragma: no cover - defensive
            namespaces[mod] = set()

    free = _free_names(nb)
    needed: dict[str, set[str]] = {}
    for name in sorted(free):
        for mod in reversed(star_modules):  # later import shadows earlier
            if name in STAR_NAME_BLOCKLIST.get(mod, ()):
                continue
            if name in namespaces.get(mod, ()):
                needed.setdefault(mod, set()).add(name)
                break
        else:
            unresolved.append(name)

    # Rewrite: drop the star imports, emit one explicit import per module at
    # the site of the first star import.
    emitted = False
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"])
        if not re.search(r"^\s*from\s+\S+\s+import\s+\*", src, re.M):
            continue
        out = []
        for line in src.splitlines(keepends=True):
            if re.match(r"^\s*from\s+\S+\s+import\s+\*", line):
                if not emitted:
                    for mod, names in needed.items():
                        out.append(f"from {mod} import {', '.join(sorted(names))}\n")
                    emitted = True
                continue
            out.append(line)
        cell["source"] = out

    for mod, names in needed.items():
        notes.append(f"expanded `from {mod} import *` -> {len(names)} name(s)")
    return notes, sorted(set(unresolved))


def drop_ipython_scaffolding(nb: dict) -> list[str]:
    """Remove helper functions that only work inside a live Jupyter kernel.

    ``%run``-style helpers call ``get_ipython()`` and walk ``nb.worksheets``
    (the nbformat v3 API). They exist so an author can re-run a sibling notebook
    from a cell -- meaningless for a static build, where each page executes on
    its own and the sibling is a page of its own. Any cell whose only job was to
    invoke such a helper goes too.
    """
    notes: list[str] = []
    kernel_only: set[str] = set()

    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"])
        tree = _parses(src)
        if tree is None or "get_ipython" not in src:
            continue
        kept, changed = [], False
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                seg = ast.get_source_segment(src, node) or ""
                if "get_ipython" in seg:
                    changed = True
                    kernel_only.add(node.name)
                    notes.append(f"dropped kernel-only helper `{node.name}`")
                    continue
                kept.append(seg + "\n\n")
                continue
            kept.append((ast.get_source_segment(src, node) or "") + "\n")
        if changed:
            cell["source"] = ("".join(kept).strip() + "\n").splitlines(keepends=True)

    # Drop cells whose only remaining statements are imports plus a call to a
    # helper we just removed (the original often bundled `import io` with it).
    if kernel_only:
        def only_kernel_calls(node: ast.stmt) -> bool:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                return True
            return (
                isinstance(node, ast.Expr)
                and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id in kernel_only
            )

        kept_cells = []
        for cell in nb["cells"]:
            src = "".join(cell["source"]) if cell.get("cell_type") == "code" else ""
            tree = _parses(src) if src else None
            if tree is not None and tree.body and all(only_kernel_calls(n) for n in tree.body):
                notes.append("dropped cell that only re-ran a sibling notebook")
                continue
            kept_cells.append(cell)
        nb["cells"] = kept_cells

    return notes


# --------------------------------------------------------------------------
# Cross-notebook helpers
# --------------------------------------------------------------------------

def index_functions(notebooks: list[dict]) -> dict[str, str]:
    """Map function name -> source, for functions defined in exactly one notebook.

    A few chapters call a helper that lives in a sibling notebook (``adc`` is
    defined in ``create_plot_signal`` and used by ``sampling_aliasing_examples``).
    That only worked when a student ran both in one live kernel, so the consumer
    gets an inlined copy. Names defined more than once are ambiguous and skipped.
    """
    owners: dict[str, int] = {}
    sources: dict[str, str] = {}
    for nb in notebooks:
        for cell in nb["cells"]:
            if cell.get("cell_type") != "code":
                continue
            src = "".join(cell["source"])
            tree = _parses(src)
            if tree is None:
                continue
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    seg = ast.get_source_segment(src, node)
                    # Kernel-only helpers are not portable; never lend them out.
                    if seg and "get_ipython" not in seg:
                        owners[node.name] = owners.get(node.name, 0) + 1
                        sources[node.name] = seg
    return {name: sources[name] for name, count in owners.items() if count == 1}


def inline_missing_functions(nb: dict, index: dict[str, str]) -> tuple[list[str], list[str]]:
    """Insert an inlined copy of each borrowed function before its first use.

    Runs to a fixpoint: an inlined helper such as ``adc`` calls ``sampling``,
    ``quantization`` and ``clipping``, which are borrowed from the same sibling
    notebook and have to be pulled in on the next round.
    """
    notes: list[str] = []
    if not index:
        return notes, []

    for _ in range(len(index)):
        defined: set[str] = set()
        for cell in nb["cells"]:
            if cell.get("cell_type") != "code":
                continue
            tree = _parses("".join(cell["source"]))
            if tree is not None:
                for node in tree.body:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                        defined.add(node.name)

        free = _free_names(nb)
        wanted = [(n, s) for n, s in index.items() if n not in defined and n in free]
        if not wanted:
            break

        # Insert immediately before the first cell that reads a borrowed name.
        insert_at = None
        wanted_names = {n for n, _ in wanted}
        for i, cell in enumerate(nb["cells"]):
            if cell.get("cell_type") != "code":
                continue
            tree = _parses("".join(cell["source"]))
            if tree is None:
                continue
            if _loaded_names(tree) & wanted_names:
                insert_at = i
                break
        if insert_at is None:
            break

        nb["cells"][insert_at:insert_at] = [
            {
                "cell_type": "code",
                "source": (src + "\n").splitlines(keepends=True),
                "metadata": {},
                "outputs": [],
                "execution_count": None,
            }
            for _, src in wanted
        ]
        notes.extend(f"inlined cross-notebook function `{n}`" for n, _ in wanted)

    return notes, []


# --------------------------------------------------------------------------
# Local helper modules -> inlined cells
# --------------------------------------------------------------------------

def _module_definitions(path: Path) -> tuple[str, list[str]]:
    """Split a helper module into (definitions, import lines it relied on).

    The notebook's own cells already bind numpy/pyplot/sympy, so the inlined
    copy keeps definitions only -- a duplicated import would trip marimo's
    "name defined in two cells" rule. The dropped imports are handed back so
    the caller can re-add only the ones the notebook lacks.

    ``INLINE_FIXUPS`` repairs names that meant something different in module
    scope: ``fft`` was the ``scipy.fft`` module there (now qualified through
    ``np``), and ``random`` was ``random.random`` there (now aliased so it does
    not collide with the notebook's own ``random``).
    """
    renames, prefix = INLINE_FIXUPS.get(path.name, ({}, []))
    kept, imports = [], []
    for line in path.read_text().splitlines():
        if re.match(r"^\s*(import |from .* import )", line):
            imports.append(line.strip())
            continue
        if re.match(r"^\s*mpl\.rc", line):  # module-level rcParams tweaks
            continue
        if re.match(r"^\s*(#!|__generated|import marimo|app = marimo|@app\.)", line):
            continue
        for old, new in renames.items():
            line = re.sub(rf"(?<![\w.]){re.escape(old)}\b", new, line)
        kept.append(line)
    body = "\n".join(kept).strip("\n")
    if prefix:
        body = "\n".join(prefix) + "\n\n" + body
    return body, imports


def _import_binds(stmt: str) -> set[str]:
    """Names an import statement binds."""
    names: set[str] = set()
    if m := re.match(r"^import\s+(\S+)", stmt):
        names.add(m.group(1).split(".")[0])
    elif m := re.match(r"^from\s+\S+\s+import\s+(.+)$", stmt):
        for part in m.group(1).replace("(", "").replace(")", "").split(","):
            part = part.strip()
            if not part or part == "*":
                continue
            names.add(part.split(" as ")[-1].strip())
    return names


def inline_local_modules(nb: dict, modules: dict[str, Path]) -> list[str]:
    """Inline ``from local_helper import ...`` by embedding the module body."""
    notes = []
    if not modules:
        return notes

    extra_imports: set[str] = set()
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        tree = _parses("".join(cell["source"]))
        if tree is None:
            continue
        hits = [n for n in ast.walk(tree)
                if isinstance(n, ast.ImportFrom) and n.module in modules]
        if not hits:
            continue
        body, imports = _module_definitions(modules[hits[0].module])
        extra_imports.update(imports)
        cell["source"] = (body + "\n").splitlines(keepends=True)
        notes.append(f"inlined local helper `{hits[0].module}`")

    # Re-add any import the notebook itself does not already satisfy.
    already: set[str] = set()
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        tree = _parses("".join(cell["source"]))
        if tree is not None:
            already |= _bound_names(tree)
        else:
            for m in re.finditer(r"^\s*(?:import|from)\s+.*$", "".join(cell["source"]), re.M):
                already.update(re.findall(r"[A-Za-z_]\w*", m.group(0)))

    needed = sorted(
        stmt for stmt in extra_imports
        if _import_binds(stmt) - already
    )
    if needed:
        target = _first_code_cell(nb)
        if target is not None:
            lines = "".join(target["source"]).splitlines(keepends=True)
            target["source"] = ["\n".join(needed) + "\n", *lines]
            notes.append(f"re-added {len(needed)} import(s) needed by inlined helpers")
    return notes


def inline_run_scripts(nb: dict, scripts: dict[str, Path]) -> list[str]:
    """Replace ``%run path/to/script.py`` with the script's definitions."""
    notes = []
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"])
        m = re.search(r"^\s*%run\s+(\S+)\s*$", src, re.M)
        if not m:
            continue
        target = m.group(1)
        if target not in scripts:
            continue
        body, _ = _module_definitions(scripts[target])
        cell["source"] = (body + "\n").splitlines(keepends=True)
        notes.append(f"inlined `%run {target}`")
    return notes
