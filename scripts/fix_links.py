#!/usr/bin/env python3
"""
Fix local links in .qmd files that point to .ipynb/.md targets by rewriting them
to .qmd when a corresponding .qmd file exists. Operates in dry-run mode by default.

Usage:
  python3 scripts/fix_links.py         # dry-run: report potential fixes
  python3 scripts/fix_links.py --fix   # apply fixes in-place
  python3 scripts/fix_links.py --folder statistics  # only process a specific folder
"""
from pathlib import Path
import re
import argparse

ROOT = Path("memm_book")
EXCLUDE = {"_build", ".ipynb_checkpoints", "_site", ".quarto", "_book"}

def find_qmd_equivalent(target_path: Path):
    """Return a Path to the .qmd equivalent if it exists, else None."""
    qmd = target_path.with_suffix('.qmd')
    if qmd.exists():
        return qmd
    # also check same directory but with different case or sanitized names
    alt = target_path.parent / (target_path.stem.replace(' ', '_') + '.qmd')
    if alt.exists():
        return alt
    return None

def process_file(path: Path, do_fix=False):
    txt = path.read_text(encoding='utf8')
    changes = []
    def repl(m):
        link = m.group(1)
        if link.startswith('http') or link.startswith('#'):
            return m.group(0)
        tgt = (path.parent / link).resolve()
        # ignore external or absolute links
        if not tgt.exists():
            # try replacing .ipynb or .md with .qmd
            cand = find_qmd_equivalent(Path(path.parent / link))
            if cand:
                rel = cand.relative_to(path.parent)
                changes.append((link, str(rel)))
                return f"]({rel})"
        return m.group(0)

    new_txt = re.sub(r"\]\(([^)]+)\)", repl, txt)
    if changes:
        print(f"{path}: will change {len(changes)} link(s)")
        for old, new in changes:
            print(f"  - {old} -> {new}")
        if do_fix:
            path.write_text(new_txt, encoding='utf8')
            print(f"Applied fixes to {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="Apply fixes in-place")
    ap.add_argument("--folder", help="Only process a specific top-level folder")
    args = ap.parse_args()

    folders = [p for p in sorted(ROOT.iterdir()) if p.is_dir() and p.name not in EXCLUDE]
    if args.folder:
        folders = [p for p in folders if p.name == args.folder]

    for folder in folders:
        for q in folder.rglob('*.qmd'):
            process_file(q, do_fix=args.fix)

if __name__ == '__main__':
    main()
