# Mechanical Engineering Metrology and Measurements (MEMM)

Set of Jupyter notebooks, prepared by [Prof. Alex Liberzon](https://turbulencelab.sites.tau.ac.il), School of Mechanical Engineering, Faculty of Engineering, Tel Aviv University for the course that is called in many places as "Mechanical Measurements Lab 1" or "Theory and Design of Mechanical Measurements", "Introduction to Measurements for Mechanical Engineers", etc. 

<!-- This is a small sample book to give you a feel for how book content is
structured.
It shows off a few of the major file types and some sample content.
It does not discuss any particular topic in depth—for more information, check out [the Jupyter Book documentation](https://jupyterbook.org).
 -->
 
This book does not replace the course materials but rather organizes them in Jupyter and Markdown notebooks. We hope it is useful as an assistance learning material for undergraduate engineering laboratory courses. It is an open-source project, and any contribution is welcome ( contact on [Github](https://github.com/alexlib) ).


## Textbook and relevant books: 
This course follows the {cite}`textbook`. It is also recommended to consult with {cite}`dunn_davis` and {cite}`wheeler`


# Metrology & Measurements — Course Introduction

This book collects practical notebooks and concise explanations to teach core concepts in mechanical engineering metrology and measurements. Content emphasizes hands-on examples, reproducible analyses, and problem-solving skills appropriate for undergraduate laboratory and lecture use.

## Learning objectives
By the end of this course/readings, students will be able to:
- Explain fundamental measurement concepts: accuracy, precision, resolution, and uncertainty.
- Apply statistical tools to analyze measurement data (distributions, confidence intervals, t‑tests, outlier detection).
- Perform calibration and regression analysis for common sensors and instruments.
- Analyze dynamic signals using time‑domain and frequency‑domain methods (FFT, windowing, spectral interpretation).
- Understand sampling, aliasing, and basic reconstruction for A/D systems.
- Model simple measurement systems (first and second order) and interpret step/impulse responses.
- Propagate measurement uncertainty (analytical and Monte Carlo) and report results following good practice.
- Implement reproducible experiments and analyses using Python and Jupyter notebooks.

## Recommended prerequisites
Students should be comfortable with:
- Calculus and basic differential equations
- Linear algebra (vectors, matrices)
- Introductory probability and statistics
- Basics of signals and systems (sinusoids, frequency, convolution helpful but not required)
- Basic Python programming (variables, functions, NumPy arrays)
- Familiarity with Jupyter notebooks and command-line usage is helpful

## How to use this book
- Navigate chapters via the table of contents. Each chapter contains short explanatory pages and runnable notebooks for labs and examples.
- Do the notebooks interactively: create a local virtual environment, install requirements, and run the notebooks in Jupyter Lab/Notebook.
- Work through the "unsorted" and "archive" content only after core topics; many items are homework examples or experimental notes.
- Instructors: adopt notebooks as lab exercises, add assessment items, and redistribute with solutions for guided learning.

## Quick environment notes
Recommended Python ecosystem: Python 3.9+, NumPy, SciPy, Matplotlib, pandas, jupyter-book, myst-nb. Add a pinned requirements.txt in the repo root for reproducible builds.

---
Start with the "theory", "statistics", and "a2d" chapters, then proceed to "signal_processing", "dynamic_signals", and "calibration" for lab work and examples.


## Table of contents
```{tableofcontents}
```

## Copyright Information

<a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/">
<img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" /> </a>

To the extent possible under law, <span rel="dct:publisher" resource="[_:publisher]">the person who associated CC0</span> with this work has waived all copyright and related or neighboring rights to this work.

<!-- 
## References
```{bibliography}
``` -->
