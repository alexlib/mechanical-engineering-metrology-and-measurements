#!/usr/bin/env python3
"""
Minimal migration helper: copy book/ -> memm_book/, convert .ipynb/.md -> .qmd (via jupytext),
and write a simple _quarto.yml listing pages (alphabetical per folder).
Run from repository root: python3 scripts/migrate_to_quarto.py
"""
from pathlib import Path
import shutil, sys
import jupytext, nbformat, yaml

SRC = Path("book")
DST = Path("memm_book")
EXCLUDE = {"_build", ".ipynb_checkpoints"}

def process_folder(src_folder: Path, dst_folder: Path, pages: list):
    """Process a single folder: convert notebooks and markdown to .qmd and
    copy resource files and directories. If a subdirectory contains notebooks
    or markdown, recurse into it so those documents are converted rather than
    blindly copying the whole tree.
    """
    dst_folder.mkdir(parents=True, exist_ok=True)
    for item in sorted(src_folder.iterdir()):
        # skip excluded names and private files
        if item.name in EXCLUDE or item.name.startswith("_"):
            continue
        if item.is_dir():
            # decide if this directory contains documents to convert
            contains_docs = any(p.is_file() and p.suffix in (".ipynb", ".md") for p in item.rglob("*"))
            if contains_docs:
                # recurse into the directory so .ipynb/.md files get converted
                process_folder(item, dst_folder / item.name, pages)
            else:
                # treat as an assets directory (fig/, data/, etc.) and copy it
                target = dst_folder / item.name
                try:
                    shutil.copytree(str(item), str(target), dirs_exist_ok=True)
                    print("copied asset dir:", item, "->", target)
                except TypeError:
                    # older Python: dirs_exist_ok not supported -> fall back to manual copy
                    target.mkdir(parents=True, exist_ok=True)
                    for src_path in item.rglob("*"):
                        rel = src_path.relative_to(item)
                        dst_path = target / rel
                        if src_path.is_dir():
                            dst_path.mkdir(parents=True, exist_ok=True)
                        else:
                            dst_path.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(str(src_path), str(dst_path))
                    print("copied asset dir (fallback):", item, "->", target)
            continue

        # files
        if item.suffix == ".ipynb":
            dst_file = (dst_folder / item.stem).with_suffix(".qmd")
            nb = jupytext.read(str(item))
            jupytext.write(nb, str(dst_file))
            pages.append(str(dst_file.relative_to(DST)))
            print("converted", item, "->", dst_file)
        elif item.suffix == ".md":
            dst_file = (dst_folder / item.stem).with_suffix(".qmd")
            shutil.copy2(str(item), str(dst_file))
            pages.append(str(dst_file.relative_to(DST)))
            print("copied md -> qmd:", item, "->", dst_file)
        else:
            # copy other resource files (images, data) into the dst folder
            shutil.copy2(str(item), str(dst_folder / item.name))
            print("copied file:", item, "->", dst_folder / item.name)

    # ensure an index.qmd exists for this folder (use intro.md if present)
    intro_src = src_folder / "intro.md"
    index_dst = dst_folder / "index.qmd"
    if intro_src.exists():
        shutil.copy2(str(intro_src), str(index_dst))
    else:
        index_dst.write_text(f"# {src_folder.name}\n\nPages in this chapter.\n")

def copy_and_convert():
    if DST.exists():
        print("Destination exists:", DST)
    DST.mkdir(exist_ok=True)
    pages = []
    for folder in sorted(p for p in SRC.iterdir() if p.is_dir() and p.name not in EXCLUDE):
        dst_folder = DST / folder.name
        # recursively process this folder
        process_folder(folder, dst_folder, pages)
        # make the chapter index the first listed page for that folder
        index_dst = dst_folder / "index.qmd"
        if index_dst.exists():
            pages.insert(0, str(index_dst.relative_to(DST)))

    # also copy any root-level files (e.g., top-level intro)
    for f in sorted(SRC.iterdir()):
        if f.is_file() and f.suffix in (".md",):
            dst_f = DST / f.name.replace(".md", ".qmd")
            shutil.copy2(str(f), str(dst_f))
            pages.insert(0, str(dst_f.relative_to(DST)))
    return pages

def write_quarto_yaml(pages):
    # Build a chapters list that contains only top-level chapter indexes
    chapters = []
    root_index = DST / "index.qmd"
    if root_index.exists():
        chapters.append(str(root_index.relative_to(DST)))
    # add each folder's index.qmd if present
    for folder in sorted(p for p in DST.iterdir() if p.is_dir() and p.name not in EXCLUDE):
        idx = folder / "index.qmd"
        if idx.exists():
            chapters.append(str(idx.relative_to(DST)))

    cfg = {
        "project": {"type": "book"},
        "book": {"title": "Mechanical Engineering Metrology and Measurements",
                 "author": "Prof. Alex Liberzon",
                 "chapters": chapters},
        "format": {"html": {"toc": True, "toc-depth": 2}},
        "bibliography": "references.bib",
    }
    (DST / "_quarto.yml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    print("Wrote", DST / "_quarto.yml")

def main():
    pages = copy_and_convert()
    write_quarto_yaml(pages)
    print("Migration copy complete. Now run: quarto render memm_book/")

if __name__ == "__main__":
    main()