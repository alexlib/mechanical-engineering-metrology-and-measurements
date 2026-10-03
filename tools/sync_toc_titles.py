#!/usr/bin/env python3
"""Give every ``book.yml`` TOC entry an explicit ``title:``.

marimo-book emits the mkdocs nav without titles, so mkdocs falls back to the
staged *filename* -- which for this book means the sidebar reads
"Theory uncertainty of a slope" rather than "How to estimate the uncertainty of
a slope". A page's own ``# H1`` does not fix this: it is not the first thing in
the staged file (the launch buttons precede it), so it never reaches the nav.

``title:`` on a TOC entry is the documented override. This script fills each one
in from the page's first H1, so the sidebar always shows what the page is
actually called. Re-run it after renaming or adding a page.

Edits book.yml line-by-line rather than round-tripping YAML, to preserve the
hand-written comments at the top of the file.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from set_titles import CONTENT, headings_in, level_of, prose_spans  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book.yml"

FILE_ENTRY = re.compile(r"^(?P<indent>\s*)- file: (?P<path>content/[\w.+-]+)\s*$")
TITLE_LINE = re.compile(r"^(?P<indent>\s*)title:.*$")


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def page_title(stem: str) -> str | None:
    for suffix in (".py", ".md"):
        p = CONTENT / f"{stem}{suffix}"
        if not p.exists():
            continue
        text = p.read_text()
        h1 = next((h for h in headings_in(text, prose_spans(text, p)) if level_of(h) == 1), None)
        return h1.group("text").strip() if h1 else None
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report without writing")
    args = ap.parse_args()

    lines = BOOK.read_text().splitlines(keepends=True)
    out: list[str] = []
    changed = untitled = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        m = FILE_ENTRY.match(line.rstrip("\n"))
        if not m:
            out.append(line)
            i += 1
            continue

        out.append(line)
        indent = m.group("indent")
        stem = Path(m.group("path")).stem
        title = page_title(stem)

        # Consume any existing title line so we rewrite rather than duplicate.
        existing = None
        if i + 1 < len(lines):
            t = TITLE_LINE.match(lines[i + 1].rstrip("\n"))
            if t and len(t.group("indent")) > len(indent):
                existing = lines[i + 1]
                i += 1

        if title is None:
            untitled += 1
            if existing:
                out.append(existing)
            print(f"  !! no H1 for {stem}")
        elif existing is not None and existing.strip() == f"title: {yaml_quote(title)}":
            out.append(existing)
        else:
            changed += 1
            print(f"  {'--' if args.check else 'ok'}  {stem:56} {title}")
            out.append(f"{indent}  title: {yaml_quote(title)}\n")
        i += 1

    if args.check:
        print(f"\n{changed} title(s) would be written, {untitled} page(s) without an H1")
        return 0

    BOOK.write_text("".join(out))
    print(f"\n{changed} title(s) written, {untitled} page(s) without an H1")
    return 1 if untitled else 0


if __name__ == "__main__":
    raise SystemExit(main())
