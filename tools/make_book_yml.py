#!/usr/bin/env python3
"""Generate ``book.yml`` from the legacy ``myst.yml`` TOC.

Keeps the chapter order, section grouping and page ordering of the original
Jupyter Book while emitting marimo-book syntax and the flattened ``content/``
filenames. Run once during the migration; ``book.yml`` is the source of truth
afterwards.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def flat_name(rel: Path) -> str:
    """``theory/00_intro`` -> ``theory-intro`` (matches convert_legacy.py)."""
    stem = rel.stem
    if rel.name in {"intro.md", "00_intro.md"} or stem == "intro":
        stem = "intro"
    return f"{rel.parent.name}-{stem}" if rel.parent != Path(".") else stem


# Short, human-readable sidebar titles. marimo-book nests with
# `section:` + `children:` (a `file:` entry may not carry children), so each
# legacy chapter's `intro` page plus its pages become one section.
SECTION_TITLES = {
    "theory": "Theory",
    "statistics": "Statistics",
    "calibration": "Calibration",
    "dynamic_signals": "Dynamic Signals",
    "a2d": "A/D Conversion",
    "signal_processing": "Signal Processing",
    "unsorted": "Supplementary Material",
}


def section_title(chapter: str) -> str:
    return SECTION_TITLES.get(chapter, chapter.replace("_", " ").title())


# Pages that existed in `legacy/book/` but were not in the legacy TOC, so the
# original book never linked to them either. Several are nevertheless linked
# from a chapter's "Ordered reading" list, which leaves those links dangling.
# Publishing them here keeps that content reachable and the links intact.
SUPPLEMENTARY = [
    {
        "section": "Theory — Supplementary Notes",
        "children": [
            "theory-Sensitivity_Coefficients_Uncertainty.md",
            "theory-exam_example.md",
            "theory-teaching_measurement_introductory_physics_lab.md",
            "theory-simple_example.py",
            "theory-example_from_best_practice.py",
            "theory-iaea_uncertainty_presentation.py",
            "theory-uncertainty_example.py",
            "theory-uncertainty_analysis_NASA.py",
            "theory-uncertainty_sources_notebook.py",
            "theory-surface_roughness_budget.py",
            "theory-teaching_measurement_uncertainty.py",
        ],
    },
    {
        "section": "Calibration — Supplementary Notes",
        "children": [
            "calibration-calibration_sensor_examples.md",
            "calibration-calibration_curve_log_log.py",
            "calibration-full_calibration_analysis_example.py",
            "calibration-calibration_simulation_interactive.md",
        ],
    },
    {
        "section": "Homework and Exploration",
        "children": [
            "unsorted-intro.md",
            "unsorted-homework_1.py",
            "unsorted-homework_example_1.py",
            "unsorted-q2_ex3.py",
            "unsorted-input_output_sin_1st_order.py",
            "unsorted-doppler.py",
            "unsorted-normal_vs_lognormal.py",
            "unsorted-random_data_for_hw_1.py",
        ],
    },
]


def convert_entry(entry: dict) -> dict | None:
    """One legacy TOC entry -> a marimo-book ``file:`` or ``section:`` entry.

    A legacy chapter entry is its intro page *plus* a list of child pages.
    marimo-book nests with ``section:`` + ``children:``, so the intro page
    becomes the section's first child rather than being dropped.
    """
    parts = Path(entry["file"]).parts
    if parts[:1] == ("book",):
        rel = Path(*parts[1:])
    elif parts[:2] == ("legacy", "book"):
        rel = Path(*parts[2:])
    else:
        return None

    children = [c for c in (convert_entry(c) for c in entry.get("children", [])) if c]
    if children:
        intro_suffix = ".py" if rel.suffix == ".ipynb" else ".md"
        return {
            "section": section_title(rel.parent.name),
            "children": [{"file": f"content/{flat_name(rel)}{intro_suffix}"}, *children],
        }
    suffix = ".py" if rel.suffix == ".ipynb" else ".md"
    return {"file": f"content/{flat_name(rel)}{suffix}"}


def main() -> int:
    myst = yaml.safe_load((ROOT / "legacy" / "myst.yml").read_text())
    entries = [convert_entry(e) for e in myst["project"]["toc"]]
    entries = [e for e in entries if e]

    missing = [
        child
        for group in SUPPLEMENTARY
        for child in group["children"]
        if not (ROOT / "content" / child).exists()
    ]
    if missing:
        raise SystemExit(f"supplementary pages not found in content/: {missing}")

    entries += [
        {"section": group["section"],
         "children": [{"file": f"content/{c}"} for c in group["children"]]}
        for group in SUPPLEMENTARY
    ]

    book = {
        "title": "Mechanical Engineering Metrology and Measurements",
        "description": (
            "An open-source book on measurement uncertainty for the undergraduate "
            "course Mechanical Engineering Metrology and Measurements at Tel Aviv University."
        ),
        "authors": [
            {"name": "Alex Liberzon", "affiliation": "Tel Aviv University"},
        ],
        "copyright": "Licensed CC0 1.0 Universal (public domain dedication).",
        "license": "CC0-1.0",
        "repo": "https://github.com/alexlib/mechanical-engineering-metrology-and-measurements",
        "branch": "master",
        "logo": "images/logo.png",
        "favicon": "images/favicon.ico",
        "theme": {"palette": {"primary": "#1F4E79", "accent": "#E07B39"}},
        "launch_buttons": {"molab": True, "github": True, "download": True},
        "dependencies": {"mode": "env"},
        "bibliography": ["references.bib"],
        "cite_style": "apa",
        "defaults": {
            "hide_author_line": True,
            "show_source_link": True,
            "hide_first_code_cell": True,
            "suppress_warnings": True,
        },
        "toc": entries,
    }

    header = (
        "# marimo-book configuration.\n"
        "# See https://marimobook.org/book_yml/ for every field.\n"
        "#\n"
        "# `content/` is deliberately flat (chapter-prefixed names rather than\n"
        "# subdirectories): marimo-book rewrites `../images/` -> `images/` for pages\n"
        "# one level below `content/`, so a nested layout would leave image links a\n"
        "# directory too deep.\n"
    )
    out = ROOT / "book.yml"
    out.write_text(header + yaml.safe_dump(book, sort_keys=False, width=100, allow_unicode=True))
    n_pages = len(re.findall(r"file:", out.read_text()))
    print(f"wrote {out.relative_to(ROOT)} with {n_pages} page entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
