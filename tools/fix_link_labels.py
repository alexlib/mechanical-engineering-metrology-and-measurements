#!/usr/bin/env python3
"""Replace filename link labels in chapter intro pages with real page titles.

The migration retargeted ``[label](page.ipynb)`` links to ``[label](page.md)`` and
rewrote the label too when it was just the old filename, which left ordered
reading lists reading ``[theory-laboratory_notebook.md](theory-laboratory_notebook.md)``.
This restores a human label taken from each page's own H1, leaving any label that
is already prose alone.

Run with ``--check`` to report without writing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from set_titles import CONTENT, headings_in, level_of, prose_spans  # noqa: E402

LINK = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<target>[^)\s]+)\)")
# A label that is only a filename adds no information over the link text.
FILENAME_LABEL = re.compile(r"^[\w.+-]+\.(md|py|ipynb)$")


def title_map() -> dict[str, str]:
    """staged page filename (no extension) -> page title."""
    out = {}
    for p in sorted(CONTENT.iterdir()):
        if p.suffix not in {".md", ".py"}:
            continue
        text = p.read_text()
        h1 = next((h for h in headings_in(text, prose_spans(text, p)) if level_of(h) == 1), None)
        if h1:
            out[p.stem] = h1.group("text").strip()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    titles = title_map()
    total = 0
    for intro in sorted(CONTENT.glob("*-intro.md")):
        text = original = intro.read_text()

        def sub(m: re.Match) -> str:
            nonlocal total
            label, target = m.group("label"), m.group("target")
            if not FILENAME_LABEL.match(label):
                return m.group(0)
            stem = target.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            title = titles.get(stem)
            if not title:
                return m.group(0)
            total += 1
            return f"[{title}]({target})"

        text = LINK.sub(sub, text)
        if text != original:
            print(f"  {'--' if args.check else 'ok'}  {intro.name}")
            if not args.check:
                intro.write_text(text)

    verb = "label(s) would be" if args.check else "label(s) rewritten"
    print(f"\n{total} {verb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
