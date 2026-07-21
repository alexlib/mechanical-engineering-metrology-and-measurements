# Mechanical Engineering Metrology and Measurements

A [Jupyter Book](https://jupyterbook.org) (built with [MyST](https://mystmd.org)) of
Python examples and notes for the undergraduate course *Mechanical Engineering
Metrology and Measurements* at Tel Aviv University.

The book covers measurement theory and uncertainty, calibration, statistics,
dynamic signals, analog-to-digital conversion, and signal processing.

## Getting started

### 1. Install `uv`

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager.
Install it once (no Python required beforehand):

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On macOS / Linux use:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

See <https://docs.astral.sh/uv/getting-started/installation/> for other options.

### 2. Install the dependencies

Dependencies are declared in [`pyproject.toml`](pyproject.toml) and locked in
[`uv.lock`](uv.lock). `uv` will create a virtual environment (`.venv`) and
install everything for you:

```bash
uv sync
```

This book is tested with Python 3.13. If you want to pin the interpreter to an
already-installed version (to avoid downloading a new one), run:

```bash
uv sync --python 3.13
```

### 3. Build the book

Build the static HTML website from the `myst.yml` project configuration:

```bash
uv run jupyter-book build --html
```

The rendered site is written to `_build/html/` (this is the command used by the
GitHub Pages workflow in `.github/workflows/deploy.yml`). The `--site` flag
instead produces a MyST site bundle under `_build/site/` for hosting on
mystmd.org.

To also (re)execute the notebooks and regenerate their figures/outputs, add
`--execute` (this is slower):

```bash
uv run jupyter-book build --html --execute
```

### 4. Preview locally

Open the generated site in your browser, for example:

```powershell
Start-Process _build\html\index.html
```

Or serve it with a static file server:

```bash
uv run python -m http.server -d _build/html 8000
# then visit http://localhost:8000
```

## Project layout

- `myst.yml` — book project configuration and table of contents
- `book/` — the content, organized into sections:
  - `theory/` — lab habits, uncertainty, error analysis, Monte Carlo / GUM
  - `calibration/` — regression, hysteresis, worked examples (LVDT, orifice, micrometer…)
  - `statistics/` — distributions, t-tests, outliers, central limit theorem
  - `dynamic_signals/` — 1st/2nd order responses, FFT, spectra
  - `a2d/` — sampling, aliasing, sinc reconstruction
  - `signal_processing/` — Fourier analysis, windowing, FFT filtering
- `pyproject.toml` / `uv.lock` — dependency declarations and lockfile

## Notes

- The source of truth for dependencies is `pyproject.toml`; `uv.lock` pins exact
  versions for reproducible installs. There is no `requirements.txt` — use
  `uv export -o requirements.txt` if you need one for a non-`uv` workflow.
- The book is also built and published automatically via GitHub Pages; see
  `.github/` for the workflow.
