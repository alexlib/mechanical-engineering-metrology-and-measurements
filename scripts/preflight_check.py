#!/usr/bin/env python3
"""
Preflight checks for the memm_book Quarto project.

Checks performed:
- every top-level folder has an index.qmd
- identifies orphan pages (qmd/ipynb/md) at top-level folders that are not listed in their index.qmd
- basic check for duplicate citation keys in references.bib
- simple check for local file links that point to missing targets (heuristic)

Usage:
  python3 scripts/preflight_check.py
  python3 scripts/preflight_check.py --fix   # create missing index.qmd via the generator
"""
from pathlib import Path
import re
import argparse
import yaml
import subprocess

ROOT = Path("memm_book")
EXCLUDE = {"_build", ".ipynb_checkpoints", "_site", ".quarto", "_book"}

def find_chapters_from_quarto():
    yml = ROOT / "_quarto.yml"
    if not yml.exists():
        return []
    data = yaml.safe_load(yml.read_text(encoding="utf8"))
    chapters = data.get("book", {}).get("chapters", [])
    return chapters

def check_missing_indexes():
    missing = []
    for p in sorted(ROOT.iterdir()):
        if not p.is_dir() or p.name in EXCLUDE:
            continue
        idx = p / "index.qmd"
        if not idx.exists():
            missing.append(str(p))
    return missing

def collect_files_not_listed():
    orphans = []
    chapters = find_chapters_from_quarto()
    # build a set of referenced filenames
    refs = set(chapters)
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir() or folder.name in EXCLUDE:
            continue
        # read index.qmd and parse links of the form [text](file)
        idx = folder / "index.qmd"
        listed = set()
        if idx.exists():
            txt = idx.read_text(encoding="utf8")
            for m in re.finditer(r"\]\(([^)]+)\)", txt):
                listed.add(m.group(1))
        # find qmd/ipynb/md files under folder
        files = [f for f in folder.iterdir() if f.is_file() and f.suffix in (".qmd", ".ipynb", ".md")]
        for f in files:
            if f.name not in listed and str(f.relative_to(ROOT)) not in refs:
                orphans.append(str(f))
    return orphans

def check_duplicate_bib_keys(bibfile="references.bib"):
    file = Path(bibfile)
    if not file.exists():
        return []
    keys = {}
    with file.open(encoding="utf8") as fh:
        for line in fh:
            m = re.match(r"@\w+\{\s*([^,]+),", line)
            if m:
                k = m.group(1).strip()
                keys[k] = keys.get(k, 0) + 1
    dup = [k for k, v in keys.items() if v > 1]
    return dup

def check_local_links():
    bad = []
    # check simple relative links inside qmd files for missing targets
    for p in ROOT.rglob("*.qmd"):
        txt = p.read_text(encoding="utf8")
        for m in re.finditer(r"\]\(([^)]+)\)", txt):
            target = m.group(1)
            if target.startswith("http") or target.startswith("#"):
                continue
            # resolve relative to p
            tgt = (p.parent / target).resolve()
            if not tgt.exists():
                bad.append(f"{p}: missing target {target}")
    return bad

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="Auto-create missing index.qmd files")
    ap.add_argument("--fix-quarto", action="store_true", help="Remove missing chapters from _quarto.yml")
    args = ap.parse_args()

    print("Scanning memm_book/ for issues...")
    missing = check_missing_indexes()
    if missing:
        print("Missing index.qmd in folders:")
        for m in missing:
            print(" - ", m)
    else:
        print("All top-level folders have index.qmd")

    orphans = collect_files_not_listed()
    if orphans:
        print("Orphan content files not listed in their index files or top-level chapters:")
        for o in orphans:
            print(" - ", o)
    else:
        print("No orphan content detected")

    dups = check_duplicate_bib_keys()
    if dups:
        print("Duplicate bibliography keys found:")
        for d in dups:
            print(" - ", d)
    else:
        print("No duplicate bib keys found")

    missing_links = check_local_links()
    if missing_links:
        print("Potential broken local links:")
        for l in missing_links[:50]:
            print(" - ", l)
    else:
        print("No obvious broken local links in .qmd files")

    if args.fix and missing:
        print("Auto-creating missing index.qmd files...")
        for m in missing:
            subprocess.run(["python3", "scripts/generate_chapter_indexes.py", "--folder", Path(m).name, "--force"]) 
        print("Re-run preflight to verify fixes.")

    # check chapters referenced in _quarto.yml
    if args.fix_quarto or (not args.fix and missing):
        qy = ROOT / '_quarto.yml'
        if qy.exists():
            txt = qy.read_text(encoding='utf8')
            data = yaml.safe_load(txt)
            chapters = data.get('book', {}).get('chapters', [])
            missing_chaps = []
            for ch in chapters:
                ch_path = (ROOT / ch).resolve()
                if not ch_path.exists():
                    missing_chaps.append(ch)
            if missing_chaps:
                print('Chapters referenced in _quarto.yml that are missing:')
                for mc in missing_chaps:
                    print(' -', mc)
                if args.fix_quarto or args.fix:
                    # backup
                    bak = qy.with_suffix('.yml.bak')
                    qy.rename(bak)
                    print(f'Backed up _quarto.yml to {bak}')
                    # remove missing chapters
                    new_chapters = [c for c in chapters if c not in missing_chaps]
                    data['book']['chapters'] = new_chapters
                    qy.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf8')
                    print('Wrote updated _quarto.yml without missing chapters')
            else:
                print('All chapters listed in _quarto.yml exist')
        else:
            print('_quarto.yml not found; skipping chapter check')

if __name__ == '__main__':
    raise SystemExit(main())
