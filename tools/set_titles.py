#!/usr/bin/env python3
"""Give every page a single, unique, human-meaningful H1 title.

The sidebar is the book's primary navigation, so a page with no heading, a
demoted heading, or a duplicated title makes the nav unusable. For each named
page this rewrites the page's first H1, or -- when the page has no H1 at all --
promotes its first heading, or inserts a title cell.

Only text inside prose is considered: ``mo.md(...)`` cells for a notebook, and
the file body minus fenced code blocks for a Markdown page. That matters because
notebooks contain commented-out magics such as ``#%loadpy`` that would otherwise
be mistaken for headings.

Idempotent. Run with ``--check`` to report without writing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

TITLES: dict[str, str] = {
    # --- no heading, or a heading that is not the page's real title --------
    "theory-volume_cylinder_undertainty_example": "Cylinder Volume: Nominal Values and Uncertainty",
    "theory-general_measurement_system_analysis": "The Generalized Measurement System",
    "calibration-calibration_simulation": "Simulation of Calibration Errors",
    "calibration-lvdt_calibration_example":
        "LVDT Calibration: Linearity, Hysteresis and Repeatability",
    "calibration-lvdt_calibration_2": "LVDT Calibration Curve and Its Uncertainty",
    "calibration-orifice_calibration_example": "GUM Budgets: Orifice Flow Meter and Storage Tank",
    "calibration-several_calibration_examples": "Uncertainty Budget Examples (SWGDRUG SD-3)",
    "calibration-weight_scale_example_Wheeler": "Weighing Scale Calibration (Wheeler and Ganji)",
    "calibration-calibration_simulation_interactive": "Interactive Calibration Simulation",
    "signal_processing-fft_of_multi_frequency_signal_window":
        "FFT of a Real Periodic Signal: Naive versus Windowed",
    "statistics-histogram_to_distribution": "From Histogram to Distribution",
    "statistics-Exploring+different+distribution":
        "Exploring Different Probability Distributions",
    "theory-uncertainty_example":
        "Uncertainty Example: Cylinder Volume from Caliper and Micrometer",
    "theory-comparing_two_methods_cylinder_volume": "Comparing Two Methods: Cylinder Volume",
    "unsorted-doppler": "Doppler Shift",
    "unsorted-homework_example_1": "Homework 1: Example Solution",
    "unsorted-input_output_sin_1st_order": "Input-Output Relation of a First-Order System",
    "unsorted-q2_ex3": "Exercise: Question 2, Example 3",
    # --- duplicate or course-artifact titles --------------------------------
    "statistics-outliers_example": "Outlier Detection: Modified Thompson Test",
    "statistics-outliers_example-2": "Outlier Detection: Modified Thompson Test, Second Version",
    "statistics-outliers_example_two": "Outlier Detection: Comparing Tests",
    "statistics-outliers_example_pairs": "Outlier Detection in Regression Residuals",
    "statistics-Lecture_5": "Chi-square Test",
    "statistics-chi_square_test_example": "Chi-square Test: Worked Example",
    "calibration-regression_analysis": "Regression Analysis with Uncertainty",
    "signal_processing-fft_filter_interactive": "Interactive FFT Filtering",
    "calibration-full_calibration_analysis_example":
        "Calibration and Uncertainty: Virtual Experiment",
    "calibration-pressure_calibration_example":
        "Calibration and Uncertainty: Virtual Experiment, Abridged",
}

HEADING = re.compile(r"^(?P<indent>[ \t]*)(?P<hashes>#{1,6})[ \t]+(?P<text>\S.*?)[ \t]*$", re.M)
FENCE = re.compile(r"^([ \t]*)(```|~~~)")
MO_MD = re.compile(r'mo\.md\(\s*(?:r?)"""(?P<body>.*?)"""', re.S)


def level_of(h: re.Match) -> int:
    """Heading level. Indentation is irrelevant: marimo dedents a cell body."""
    return len(h.group("hashes"))


def prose_spans(text: str, path: Path) -> list[tuple[int, int]]:
    """Character ranges of the file that are prose, not code."""
    if path.suffix == ".py":
        return [(m.start("body"), m.end("body")) for m in MO_MD.finditer(text)]

    spans, pos, in_fence = [], 0, None
    for line in re.finditer(r"^.*(?:\n|$)", text, re.M):
        end = line.end()
        fence = FENCE.match(line.group(0))
        if fence:
            marker = fence.group(2)
            if in_fence is None:
                in_fence = marker
            elif marker == in_fence:
                in_fence = None
        elif in_fence is None:
            spans.append((pos, end))
        pos = end
    return spans


def first_cell_end(text: str) -> int | None:
    """Offset just past the first ``@app.cell`` block, or None if there is none."""
    start = text.find("@app.cell")
    if start == -1:
        return None
    nxt = text.find("@app.cell", start + 1)
    tail = text.find('if __name__ == "__main__":', start + 1)
    candidates = [c for c in (nxt, tail) if c != -1]
    return min(candidates) if candidates else len(text)


def headings_in(text: str, spans: list[tuple[int, int]]) -> list[re.Match]:
    out = []
    for start, end in spans:
        out.extend(HEADING.finditer(text, start, end))
    return out


def apply_title(path: Path, title: str, check: bool) -> tuple[bool, str]:
    text = path.read_text()
    found = headings_in(text, prose_spans(text, path))

    # A first heading already at level 1 is the page title: rewrite in place.
    # A lone heading at a deeper level was clearly meant as the title too.
    # Otherwise the page has real internal structure, so prepend a title
    # rather than overwriting a section heading.
    target = None
    if found and (level_of(found[0]) == 1 or len(found) == 1):
        target = found[0]

    if target is not None:
        if target.group("text").strip() == title and level_of(target) == 1:
            return False, "already correct"
        verb = "rewrite H1" if level_of(target) == 1 else "promote to H1"
        if check:
            return True, f"{verb} {target.group('text')!r} -> {title!r}"
        new = text[: target.start()] + f"{target.group('indent')}# {title}\n" + text[target.end():]
        path.write_text(new)
        return True, f"{verb} -> {title!r}"

    verb = "prepend heading" if path.suffix == ".md" else "insert title cell"
    if check:
        return True, f"{verb} {title!r}"

    if path.suffix == ".md":
        body = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)
        if body is not text:
            path.write_text(f"# {title}\n\n{body}")
        else:
            path.write_text(f"# {title}\n\n{text}")
        return True, f"prepended heading {title!r}"

    # Not every converted notebook has an `import marimo as mo` cell -- the
    # converter only emits one when the source notebook used `mo`. A notebook
    # with no prose at all therefore has nothing defining `mo`, so the inserted
    # cell must bring its own. If a `mo` cell does exist, adding a second would
    # trip marimo's "name defined in two cells" rule.
    if "import marimo as mo" in text:
        cell = (
            "@app.cell(hide_code=True)\n"
            "def _(mo):\n"
            f'    mo.md(r"""\n    # {title}\n    """)\n'
            "    return\n\n\n"
        )
    else:
        cell = (
            "@app.cell(hide_code=True)\n"
            "def _():\n"
            "    import marimo as mo\n"
            f'    mo.md(r"""\n    # {title}\n    """)\n'
            "    return (mo,)\n\n\n"
        )
    at = first_cell_end(text)
    if at is None:
        return False, "could not find a cell to insert after"
    path.write_text(text[:at] + cell + text[at:])
    return True, f"inserted title cell {title!r}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    missing, changed = [], []
    for stem, title in sorted(TITLES.items()):
        matches = [p for p in CONTENT.iterdir() if p.stem == stem]
        if not matches:
            missing.append(stem)
            continue
        ok, msg = apply_title(matches[0], title, args.check)
        print(f"  {'--' if args.check and ok else 'ok'}  {matches[0].name:60} {msg}")
        if ok:
            changed.append(stem)

    if missing:
        print(f"\nno such page: {missing}", file=sys.stderr)
        return 1
    print(f"\n{len(changed)} page(s) {'would change' if args.check else 'changed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
