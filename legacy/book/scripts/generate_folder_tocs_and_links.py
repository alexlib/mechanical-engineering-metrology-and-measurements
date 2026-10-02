#!/usr/bin/env python3
"""
Generate link lists inside each book/*/intro.md and (optionally) create per-folder _toc.yml.

Usage:
  # install deps
  pip install nbformat pyyaml

  # generate links only
  python3 scripts/generate_folder_tocs_and_links.py

  # generate links and create per-folder _toc.yml files
  python3 scripts/generate_folder_tocs_and_links.py --create-tocs
"""
from pathlib import Path
import nbformat
import re
import yaml
import argparse

BOOK = Path("book")
EXCLUDE = {"_build", ".ipynb_checkpoints"}

AUTOGEN_START = "<!-- AUTOGEN_START -->"
AUTOGEN_END = "<!-- AUTOGEN_END -->"

def get_notebook_title(nb_path: Path):
    try:
        nb = nbformat.read(nb_path, as_version=4)
        # try metadata title
        meta_title = nb.metadata.get("title")
        if meta_title:
            return str(meta_title).strip()
        # otherwise try first markdown heading
        for cell in nb.cells:
            if cell.cell_type == "markdown":
                m = re.search(r"^#\s+(.*)", cell.source, flags=re.MULTILINE)
                if m:
                    return m.group(1).strip()
                # take first non-empty line
                first_line = cell.source.strip().splitlines()
                if first_line:
                    return first_line[0].strip()[:80]
        return nb_path.stem
    except Exception:
        return nb_path.stem

def get_md_title(md_path: Path):
    try:
        text = md_path.read_text(encoding="utf8")
        m = re.search(r"^#\s+(.*)", text, flags=re.MULTILINE)
        if m:
            return m.group(1).strip()
        first_line = text.strip().splitlines()
        if first_line:
            return first_line[0].strip()[:80]
    except Exception:
        pass
    return md_path.stem

def write_intro_links(folder: Path, pages: list[tuple[str,str]]):
    intro = folder / "intro.md"
    header = "## Pages in this chapter\n\n"
    bullets = "\n".join(f"- [{title}]({path})" for title, path in pages) + "\n"
    block = f"{AUTOGEN_START}\n{header}{bullets}{AUTOGEN_END}\n"
    if intro.exists():
        txt = intro.read_text(encoding="utf8")
        if AUTOGEN_START in txt and AUTOGEN_END in txt:
            new_txt = re.sub(
                rf"{re.escape(AUTOGEN_START)}.*?{re.escape(AUTOGEN_END)}",
                block,
                txt,
                flags=re.S,
            )
        else:
            # insert before final TOC or append at end
            if "```{tableofcontents}" in txt:
                new_txt = txt.replace("```{tableofcontents}", block + "\n```{tableofcontents}")
            else:
                new_txt = txt.rstrip() + "\n\n" + block
        intro.write_text(new_txt, encoding="utf8")
        print(f"Updated: {intro}")
    else:
        intro.write_text(f"# {folder.name.capitalize()}\n\n" + block, encoding="utf8")
        print(f"Created: {intro}")

def create_local_toc(folder: Path, pages: list[tuple[str,str]]):
    toc_path = folder / "_toc.yml"
    # entries use filenames without extension, relative to folder
    chapters = []
    for title, relpath in pages:
        p = Path(relpath)
        name = p.name
        stem = Path(name).stem
        chapters.append({"file": stem})
    toc = {"format": "jb-book", "root": "intro", "chapters": chapters}
    toc_path.write_text(yaml.dump(toc, sort_keys=False), encoding="utf8")
    print(f"Created/Updated TOC: {toc_path}")

def main(create_tocs=False):
    if not BOOK.exists():
        print("book/ not found; run from repository root.")
        return
    for folder in sorted(BOOK.iterdir()):
        if not folder.is_dir() or folder.name in EXCLUDE:
            continue
        # find notebooks and md (exclude intro.md and _toc.yml)
        pages = []
        for p in sorted(folder.iterdir()):
            if p.name in EXCLUDE or p.name.startswith("_"):
                continue
            if p.suffix == ".ipynb":
                title = get_notebook_title(p)
                pages.append((title, p.name))
            elif p.suffix == ".md" and p.name != "intro.md":
                title = get_md_title(p)
                pages.append((title, p.name))
        if not pages:
            continue
        write_intro_links(folder, pages)
        if create_tocs:
            create_local_toc(folder, pages)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--create-tocs", action="store_true", help="also write per-folder _toc.yml files")
    args = ap.parse_args()
    main(create_tocs=args.create_tocs)