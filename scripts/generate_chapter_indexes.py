#!/usr/bin/env python3
"""
Generate or refresh detailed index.qmd files for each top-level chapter in memm_book/.

The script will create a rich index page for each chapter folder containing:
- a YAML front matter with a title
- a short summary (taken from intro.md/intro.qmd when available or a sensible default)
- a small set of learning objectives (default by chapter name, customizable)
- a 'Pages in this chapter' auto-generated block with links and one-line descriptions

By default the script updates only the auto-generated block inside existing index.qmd files
and preserves any other content. Use --force to overwrite the non-autogen content.

Usage:
  python3 scripts/generate_chapter_indexes.py       # update all chapters
  python3 scripts/generate_chapter_indexes.py --force   # overwrite content
  python3 scripts/generate_chapter_indexes.py --folder theory  # update single folder
"""
from pathlib import Path
import re
import argparse
import textwrap
import nbformat

# Configuration
ROOT = Path("memm_book")
EXCLUDE = {"_build", ".ipynb_checkpoints", "_site", ".quarto", "_book"}
AUTOGEN_START = "<!-- AUTOGEN_START -->"
AUTOGEN_END = "<!-- AUTOGEN_END -->"

# Default chapter summaries and objectives -- used when no intro.md/intro.qmd is present
DEFAULT_SUMMARIES = {
    "theory": "This chapter covers measurement theory: uncertainty, best practices, and uncertainty propagation.",
    "statistics": "Hands-on statistics for measurement data: sampling, distributions, hypothesis testing, and outlier handling.",
    "calibration": "Sensor and instrument calibration methods, regression, hysteresis, and calibration uncertainty.",
    "signal_processing": "Frequency-domain analysis using FFT, windowing, spectral interpretation, and simple filtering.",
    "dynamic_signals": "Time-domain system responses, first/second-order systems, and vibration-based measurement examples.",
    "a2d": "Sampling, aliasing, reconstruction, and practical analog-to-digital conversion examples.",
    "unsorted": "Homework, drafts, and extra examples. Consult these after core chapters.",
    "archive": "Historical notes and supplementary material retained for reference.",
}

DEFAULT_OBJECTIVES = {
    "theory": [
        "Understand measurement uncertainty and how to report it.",
        "Apply simple uncertainty propagation methods and Monte Carlo checks.",
    ],
    "statistics": [
        "Compute and interpret mean, variance, and confidence intervals.",
        "Apply t-tests and detect common outliers in measurement data.",
    ],
    "calibration": [
        "Perform regression-based calibrations and evaluate residuals.",
        "Construct a calibration uncertainty budget and report results.",
    ],
    "a2d": [
        "Describe the sampling theorem and Nyquist frequency.",
        "Demonstrate aliasing and basic reconstruction with sinc interpolation.",
    ],
    "signal_processing": [
        "Compute discrete Fourier transforms and interpret spectra.",
        "Understand windowing effects and how to reduce spectral leakage.",
    ],
    "dynamic_signals": [
        "Estimate time constants, damping, and natural frequency from responses.",
        "Link time-domain behavior with frequency content.",
    ],
}

DEFAULT_PREREQS = {
    "default": [
        "Basic calculus and introductory statistics.",
        "Comfort with Python and Jupyter notebooks (NumPy/Matplotlib helpful).",
    ]
}

def strip_front_matter(text: str) -> str:
    """Remove YAML front matter from text (if present) and return the remainder."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    if m:
        return text[m.end():]
    return text

def first_heading_and_paragraph_from_md_text(text: str):
    text = strip_front_matter(text)
    # find first H1 heading
    m = re.search(r"^#\s+(.*)$", text, flags=re.M)
    title = None
    if m:
        title = m.group(1).strip()
        rest = text[m.end():].strip()
    else:
        # fallback to first non-empty line
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        title = lines[0] if lines else None
        rest = "\n".join(lines[1:]) if len(lines) > 1 else ""

    # first paragraph after the heading
    para = ""
    if rest:
        paras = re.split(r"\n\s*\n", rest)
        if paras:
            para = paras[0].strip()
    return title or "", para or ""

def title_and_desc_for_file(path: Path):
    try:
        if path.suffix in (".qmd", ".md"):
            txt = path.read_text(encoding="utf8")
            return first_heading_and_paragraph_from_md_text(txt)
        elif path.suffix == ".ipynb":
            nb = nbformat.read(str(path), as_version=4)
            # look for metadata title
            meta_title = nb.metadata.get("title") if hasattr(nb, "metadata") else None
            if meta_title:
                title = str(meta_title)
            else:
                title = None
            desc = ""
            for cell in nb.cells:
                if cell.cell_type != "markdown":
                    continue
                t = cell.source
                if not title:
                    m = re.search(r"^#\s+(.*)$", t, flags=re.M)
                    if m:
                        title = m.group(1).strip()
                # find first paragraph
                p = re.split(r"\n\s*\n", t)
                if p and len(p[0].strip()) > 0:
                    desc = p[0].strip()
                    break
            return (title or path.stem, desc)
    except Exception:
        return (path.stem, "")
    return (path.stem, "")

def build_autogen_block(folder: Path, entries: list):
    """Create the AUTOGEN block string for index.qmd.

    entries is a list of tuples: (title, link, short_description)
    """
    lines = [AUTOGEN_START, "## Pages in this chapter", ""]
    def sanitize_desc(text: str, max_len: int = 180) -> str:
        if not text:
            return ""
        # remove fenced code blocks ```...``` and inline backticks
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
        text = re.sub(r"`([^`]*)`", r"\1", text)
        # remove markdown links [text](target)
        text = re.sub(r"\[.*?\]\(.*?\)", " ", text)
        # strip remaining brackets to avoid accidental link patterns
        text = text.replace("[", "").replace("]", "")
        # replace newlines and collapse whitespace
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) > max_len:
            text = text[: max_len - 1].rstrip() + "…"
        return text

    for title, link, desc in entries:
        # short description on same line if available, sanitized and truncated
        clean = sanitize_desc(desc)
        safe_desc = (" — " + clean) if clean else ""
        lines.append(f"- [{title}]({link}){safe_desc}")
    lines.append("")
    lines.append(AUTOGEN_END)
    return "\n".join(lines)

def read_intro_text(folder: Path):
    # prefer intro.qmd -> intro.md -> intro.ipynb
    candidates = [folder / "intro.qmd", folder / "intro.md", folder / "intro.ipynb"]
    for c in candidates:
        if c.exists():
            if c.suffix == ".ipynb":
                nb = nbformat.read(str(c), as_version=4)
                for cell in nb.cells:
                    if cell.cell_type == "markdown":
                        txt = cell.source.strip()
                        if txt:
                            # return first paragraph
                            return re.split(r"\n\s*\n", strip_front_matter(txt))[0].strip()
                return ""
            else:
                txt = c.read_text(encoding="utf8")
                # return the first paragraph after the first heading
                title, para = first_heading_and_paragraph_from_md_text(txt)
                return para or title or ""
    return ""

def generate_index_for_folder(folder: Path, force=False):
    """Generate or update index.qmd in the given folder.

    If force is False the script will update only the AUTOGEN block and will try to
    preserve existing non-autogen content. If force is True the full index is replaced.
    """
    if not folder.is_dir():
        return False

    title_name = folder.name.replace("_", " ").replace("+", " ").title()
    index_path = folder / "index.qmd"

    # collect page files (only immediate child files)
    page_files = [p for p in sorted(folder.iterdir()) if p.is_file() and p.name not in ("index.qmd") and not p.name.startswith("_") and p.suffix in (".qmd", ".md", ".ipynb")]

    entries = []
    for p in page_files:
        link_target = p.name
        # if a .qmd version exists for a notebook prefer that link
        if p.suffix == ".ipynb":
            qmd_candidate = folder / (p.stem + ".qmd")
            if qmd_candidate.exists():
                link_target = qmd_candidate.name
        title, desc = title_and_desc_for_file(p)
        entries.append((title, link_target, desc))

    # summary and learning objectives
    summary = read_intro_text(folder) or DEFAULT_SUMMARIES.get(folder.name, "Short chapter summary.")
    objectives = DEFAULT_OBJECTIVES.get(folder.name, DEFAULT_OBJECTIVES.get("default", []))
    prereqs = DEFAULT_PREREQS.get(folder.name, DEFAULT_PREREQS["default"])

    autogen_block = build_autogen_block(folder, entries)

    # prepare new body content
    objectives_md = "\n".join(f"- {o}" for o in objectives) if objectives else "- Read the pages and run the notebooks."
    prereqs_md = "\n".join(f"- {p}" for p in prereqs)

    new_body = textwrap.dedent(f"""
    {summary}

    ## Learning objectives

    {objectives_md}

    ## Prerequisites

    {prereqs_md}

    {autogen_block}

    """)

    # write or update index.qmd
    if index_path.exists() and not force:
        txt = index_path.read_text(encoding="utf8")
        # preserve front matter if present
        fm = None
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, flags=re.S)
        if m:
            fm = m.group(0)
            rest = txt[m.end():]
        else:
            rest = txt

        if AUTOGEN_START in rest and AUTOGEN_END in rest:
            # replace existing AUTOGEN block
            # use a function as the replacement to avoid \-escapes in the
            # autogen_block being interpreted as backreferences by re.sub
            new_rest = re.sub(
                re.escape(AUTOGEN_START) + r".*?" + re.escape(AUTOGEN_END),
                lambda _m: autogen_block,
                rest,
                flags=re.S,
            )
            new_txt = (fm or f"---\ntitle: \"{title_name}\"\n---\n\n") + new_rest
            index_path.write_text(new_txt, encoding="utf8")
            print(f"Updated AUTOGEN block in: {index_path}")
        else:
            # append the autogen block at the end
            new_txt = (fm or f"---\ntitle: \"{title_name}\"\n---\n\n") + rest.rstrip() + "\n\n" + new_body
            index_path.write_text(new_txt, encoding="utf8")
            print(f"Appended AUTOGEN block to existing index: {index_path}")
    else:
        # create a fresh index file (overwrites if force=True)
        fm = f"---\ntitle: \"{title_name}\"\n---\n\n"
        full = fm + new_body
        index_path.write_text(full, encoding="utf8")
        print(f"Created index: {index_path}")
    return True

def generate_all(force=False, folder_name=None):
    if not ROOT.exists():
        print("memm_book/ not found. Run the migration script first or create the directory.")
        return 1
    folders = [p for p in sorted(ROOT.iterdir()) if p.is_dir() and p.name not in EXCLUDE]
    if folder_name:
        folders = [p for p in folders if p.name == folder_name]
    for f in folders:
        generate_index_for_folder(f, force=force)
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="Overwrite index content (not just the AUTOGEN block)")
    ap.add_argument("--folder", help="Only generate index for a specific top-level folder (by name)")
    args = ap.parse_args()
    return generate_all(force=args.force, folder_name=args.folder)

if __name__ == '__main__':
    raise SystemExit(main())
