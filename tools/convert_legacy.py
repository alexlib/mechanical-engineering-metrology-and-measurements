#!/usr/bin/env python3
"""One-shot migration: MyST/Jupyter Book (``book/``) -> marimo-book (``content/``).

Reads every ``book/**/*.ipynb``, applies the marimo-compatibility fixups in
``nb_migrate.py``, hands the result to ``marimo convert``, and writes it to
``content/<chapter>-<stem>.py``.

Content is flattened to a single directory because marimo-book rewrites
``../images/`` -> ``images/`` for pages one level below ``content/``; nested
chapter folders would leave image links a directory too deep. The chapter
prefix keeps page names unique (seven chapters each ship an ``intro``).

Usage::

    uv run --with marimo python tools/convert_legacy.py
    uv run --with marimo python tools/convert_legacy.py --validate
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import nb_migrate as mig  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LEGACY = ROOT / "legacy" / "book"
CONTENT = ROOT / "content"
SCRIPTS = ROOT / "legacy" / "book" / "scripts"

# Local helper modules imported by a handful of notebooks.
LOCAL_MODULES = {
    "linear_regression": SCRIPTS / "linear_regression.py",
    "signal_processing": SCRIPTS / "signal_processing.py",
}

# Scripts pulled in with ``%run`` rather than imported.
RUN_SCRIPTS = {
    "book/scripts/create_random_data": SCRIPTS / "create_random_data.py",
}

# Modules whose namespace we search when expanding ``from M import *``.
STAR_SEARCH = {
    "numpy": "numpy",
    "pylab": "pylab",
    "sympy": "sympy",
    "matplotlib.pyplot": "matplotlib.pyplot",
}

# Source-level modernisations applied to the converted page, keyed by flat
# filename. These are real code bugs (not conversion artefacts) that only
# worked on older NumPy, so they are spelled out rather than pattern-guessed.
POST_PATCHES: dict[str, list[tuple[str, str]]] = {
    # The random concentrations/transmittances were generated as (6, 1) column
    # arrays, so the regression coefficients came out as shape-(1,) arrays.
    # NumPy 2 refuses to scalarise those in `%6.4f` formatting and in `float()`.
    # Generating 1-D samples is what the commented-out `np.array([...])` above
    # the cell clearly intended. Patterns tolerate PEP 8 spacing because
    # `marimo convert` reformats the source before this runs.
    "unsorted-homework_example_1.py": [
        (r"np\.sort\(\s*np\.random\.rand\(\s*6\s*,\s*1\s*\)\s*\*\s*55\s*,\s*axis\s*=\s*1\s*\)",
         "np.sort(np.random.rand(6) * 55)"),
        (r"np\.random\.rand\(\s*1\s*\)\s*\*\s*0\.05", "np.random.rand() * 0.05"),
        (r"np\.random\.rand\(\s*6\s*,\s*1\s*\)\s*\*\s*10", "np.random.rand(6) * 10"),
        (r"^(\s*)c1 = \(a1 - b\)/K$", r"\1c1 = float((a1 - b) / K)"),
    ],
}

# Prose links inside a notebook's markdown cells have to be retargeted the same
# way `tools/convert_markdown.py` retargets the standalone pages. Only link and
# `src=` syntax is touched, never Python string literals -- those are build-time
# file reads and must stay repo-root-relative.
PROSE_IPYNB_LINK = re.compile(
    r"(?P<pre>\]\()(?P<path>[^)\s\"]*?)(?P<stem>[A-Za-z0-9_.+-]+)\.ipynb(?P<post>[)#])"
)
PROSE_IMAGE_LINK = re.compile(r'(?P<pre>(?:\]\(|src="))img/(?P<name>[^)"\s]+)')


def rewrite_prose_links(text: str, flat_by_stem: dict[str, str]) -> str:
    def link_sub(m: re.Match) -> str:
        flat = flat_by_stem.get(m.group("stem"))
        if not flat:
            return m.group(0)
        return f"{m.group('pre')}{flat}.md{m.group('post')}"

    text = PROSE_IPYNB_LINK.sub(link_sub, text)
    return PROSE_IMAGE_LINK.sub(lambda m: f"{m.group('pre')}../images/{m.group('name')}", text)


def flat_name(rel_no_ext: str) -> str:
    """``theory/00_intro`` -> ``theory-intro``; ``stats/t-test`` -> ``stats-t-test``."""
    chapter, _, stem = rel_no_ext.rpartition("/")
    if re_full_intro(stem):
        stem = "intro"
    return f"{chapter}-{stem}" if chapter else stem


def re_full_intro(stem: str) -> bool:
    import re

    return stem in {"intro", "00_intro"} or re.fullmatch(r"\d+_intro", stem) is not None


def prepare(nb: dict, func_index: dict[str, str]) -> tuple[dict, list[str], list[str]]:
    """Apply every fixup. Returns (notebook, notes, unresolved free names)."""
    nb = json.loads(json.dumps(nb))

    # Every notebook page is stripped of stored outputs: marimo re-executes at
    # build time and the base64 blobs would only bloat the repository.
    for cell in nb["cells"]:
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        cell["source"] = mig.rewrite_paths("".join(cell["source"])).splitlines(keepends=True)

    notes: list[str] = []
    notes += mig.drop_ipython_scaffolding(nb)
    notes += mig.raw_cells_to_code(nb)
    notes += mig.strip_magics(nb)
    notes += mig.markdown_images_in_code(nb)
    notes += mig.expand_symbol_declarations(nb)
    notes += mig.inline_run_scripts(nb, RUN_SCRIPTS)
    notes += mig.inline_local_modules(nb, LOCAL_MODULES)
    notes += mig.inline_missing_functions(nb, func_index)[0]
    star_notes, unresolved = mig.expand_star_imports(nb, STAR_SEARCH)
    notes += star_notes
    implicit_notes, unresolved = mig.add_missing_imports(nb)
    notes += implicit_notes
    return nb, notes, unresolved


def convert_one(rel_no_ext: str, prepared: dict, tmpdir: Path,
                flat_by_stem: dict[str, str]) -> tuple[bool, str]:
    tmp = tmpdir / (rel_no_ext.replace("/", "__") + ".ipynb")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps(prepared, indent=1))

    dest = CONTENT / (flat_name(rel_no_ext) + ".py")
    dest.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        [sys.executable, "-m", "marimo", "convert", str(tmp), "-o", str(dest)],
        capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode != 0 or not dest.exists():
        msg = (proc.stderr or proc.stdout).strip().splitlines()
        return False, msg[-1] if msg else "unknown error"

    # Patches first: some of them match the *legacy* prose paths that
    # `rewrite_prose_links` is about to rewrite.
    text = dest.read_text()
    for pattern, replacement in POST_PATCHES.get(dest.name, []):
        text = re.sub(pattern, replacement, text, flags=re.M)
    dest.write_text(rewrite_prose_links(text, flat_by_stem))
    return True, ""


def validate(rel_no_ext: str) -> tuple[bool, str]:
    """Execute the notebook the way marimo-book does, surfacing cell errors."""
    dest = CONTENT / (flat_name(rel_no_ext) + ".py")
    out = ROOT / ".convert_check.ipynb"
    proc = subprocess.run(
        [sys.executable, "-m", "marimo", "export", "ipynb", "--include-outputs",
         "-f", str(dest), "-o", str(out)],
        capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode == 0:
        out.unlink(missing_ok=True)
        return True, "ok"
    detail = ""
    if out.exists():
        nb = json.loads(out.read_text())
        for i, cell in enumerate(nb["cells"]):
            for o in cell.get("outputs", []):
                if o.get("output_type") == "error":
                    tb = o.get("traceback", [])
                    tail = " | ".join(ln.strip() for ln in tb[-3:])
                    detail = f"cell {i}: {tail}"[:200]
                    break
            if detail:
                break
        out.unlink(missing_ok=True)
    return False, detail or (proc.stdout + proc.stderr).strip().splitlines()[-1][:200]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true", help="execute each converted notebook")
    args = ap.parse_args()

    tmpdir = ROOT / ".convert_tmp"
    tmpdir.mkdir(exist_ok=True)

    sources = [p for p in sorted(LEGACY.rglob("*.ipynb")) if ".ipynb_checkpoints" not in p.parts]
    print(f"found {len(sources)} notebooks under {LEGACY.relative_to(ROOT)}")

    # Index helpers defined in one notebook and consumed by another (e.g. ``adc``)
    # before any fixup runs, so the index reflects the original sources.
    func_index = mig.index_functions([json.loads(p.read_text()) for p in sources])
    if func_index:
        print(f"indexed {len(func_index)} cross-notebook helper function(s)")

    # Legacy notebook stem -> flat content stem, so prose links can be retargeted.
    flat_by_stem: dict[str, str] = {}
    for p in sources:
        rel_no_ext = p.relative_to(LEGACY).with_suffix("")
        flat_by_stem[rel_no_ext.stem] = flat_name(str(rel_no_ext))

    failures: list[tuple[str, str]] = []
    unresolved_all: set[str] = set()
    for i, path in enumerate(sources, 1):
        rel = str(path.relative_to(LEGACY).with_suffix(""))
        prepared, notes, unresolved = prepare(json.loads(path.read_text()), func_index)
        unresolved_all |= set(unresolved)
        ok, msg = convert_one(rel, prepared, tmpdir, flat_by_stem)
        if not ok:
            failures.append((rel, f"CONVERT: {msg}"))
            print(f"[{i}/{len(sources)}] CONVERT FAIL {rel}: {msg}")
            continue
        tag = f" ({'; '.join(sorted(set(notes)))})" if notes else ""
        print(f"[{i}/{len(sources)}] {flat_name(rel)}.py{tag}")

    if unresolved_all:
        print(f"\nfree names no star-import could supply: {sorted(unresolved_all)}")

    if args.validate:
        print("\n--- validating (executing each notebook) ---")
        bad = 0
        for path in sources:
            rel = str(path.relative_to(LEGACY).with_suffix(""))
            ok, msg = validate(rel)
            if ok:
                print(f"  OK   {flat_name(rel)}")
            else:
                bad += 1
                failures.append((rel, f"RUN: {msg}"))
                print(f"  FAIL {flat_name(rel)}: {msg}")
        print(f"\n{bad} notebook(s) failed to execute")

    print(f"\n{len(failures)} failure(s)")
    for rel, msg in failures:
        print(f"  {rel} -> {msg}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
