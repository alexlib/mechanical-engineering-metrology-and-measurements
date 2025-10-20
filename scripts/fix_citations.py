#!/usr/bin/env python3
from pathlib import Path
import re
import nbformat

ROOT = Path("memm_book")
CITE_RE = re.compile(r"\{cite\}`([^`]*)`")

def convert_text(text):
    def repl(m):
        keys = [k.strip() for k in m.group(1).split(";") if k.strip()]
        keys = [k.lstrip("@") for k in keys]  # ensure no repeated @
        return "[" + "; ".join("@" + k for k in keys) + "]"
    return CITE_RE.sub(repl, text)

def process_md(path):
    s = path.read_text(encoding="utf8")
    s2 = convert_text(s)
    if s2 != s:
        path.write_text(s2, encoding="utf8")
        print("Patched:", path)

def process_ipynb(path):
    nb = nbformat.read(str(path), as_version=4)
    changed = False
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            new = convert_text(cell.source)
            if new != cell.source:
                cell.source = new
                changed = True
    if changed:
        nbformat.write(nb, str(path))
        print("Patched notebook:", path)

for p in ROOT.rglob("*"):
    if p.suffix in (".qmd", ".md"):
        process_md(p)
    elif p.suffix == ".ipynb":
        process_ipynb(p)
print("Done.")