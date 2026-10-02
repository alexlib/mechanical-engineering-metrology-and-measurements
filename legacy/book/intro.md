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

## The Central Theme: Understanding and Managing Measurement Uncertainty

Every measurement has uncertainty — whether you quantify it or not. This book teaches you to:

1. **Understand where uncertainty comes from** — in your instruments, your data collection, your analysis
2. **Quantify it rigorously** — using statistics, error budgets, and propagation methods
3. **Reduce it where possible** — through careful calibration and experimental design
4. **Report it correctly** — so others know how much to trust your results

This is the journey of a metrologist: **Theory → Statistics → Calibration → Real-world Systems → Uncertainty Budget → Informed Reporting**.

---

## How This Book Is Organized: A Learning Pathway

Each chapter builds on the previous one, all focused on the central goal of managing measurement uncertainty:

| Chapter | Purpose | Contributes to Understanding |
|---------|---------|------------------------------|
| **Theory** | Foundational concepts: where errors come from, how uncertainty is defined | *What is uncertainty?* |
| **Statistics** | Tools to quantify data variability, detect outliers, compute confidence intervals | *How do I measure uncertainty from data?* |
| **Calibration** | Use statistics to characterize instruments, reduce systematic errors, build calibration curves | *How do I reduce and control uncertainty in my instruments?* |
| **Dynamic Signals** | Understand how measurement systems respond to changes; recognize when you're measuring the system, not the quantity | *What affects the fidelity of my measurement?* |
| **Signal Processing** | Separate true signals from noise using frequency-domain tools; understand sampling and filtering trade-offs | *How do I extract clean measurements from noisy data?* |
| **A/D Conversion** | Understand how analog signals are digitized; manage aliasing and quantization effects | *How do I capture measurements without introducing new errors?* |

---

## Key Insights You'll Build

- **After Theory:** You understand what uncertainty *is*, where it comes from, and that every measurement has a "confidence zone" around it
- **After Statistics:** You can *quantify* uncertainty from real data using Type A (statistical) methods and recognize when your sample size is adequate
- **After Calibration:** You can *characterize* and *reduce* systematic errors in instruments, and you understand Type B (systematic) uncertainty sources
- **After Dynamic Signals & Signal Processing:** You understand that your measurement system itself affects the result — bandwidth, frequency response, and noise filtering all matter
- **After A/D Conversion:** You know how to capture signals digitally without losing information or introducing aliasing artifacts
- **Capstone:** You can plan a complete measurement workflow: identify uncertainty sources → design an experiment → collect data → analyze with appropriate statistical rigor → propagate and report uncertainty

---

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

**Recommended reading order:** Follow the chapters in the order presented — **Theory → Statistics → Calibration → Dynamic Signals → Signal Processing → A/D Conversion**. This sequence builds understanding progressively, with each chapter providing tools needed for the next.

- Navigate chapters via the table of contents. Each chapter contains short explanatory pages and runnable notebooks for labs and examples.
- Start with **Theory** to build foundational understanding of measurement uncertainty and error sources.
- Move to **Statistics** to learn how to quantify uncertainty from data.
- Study **Calibration** to see how statistics apply to real instruments and measurement systems.
- Explore **Dynamic Signals & Signal Processing** to understand how systems and noise affect measurements.
- Learn **A/D Conversion** to complete your toolkit for acquiring and processing measurement data.
- Do the notebooks interactively: create a local virtual environment, install requirements, and run the notebooks in Jupyter Lab/Notebook.
- Work through the Theory section's "Ordered reading" guidance first — it establishes the vocabulary and concepts you'll use throughout.
- For each chapter, follow its "Ordered reading (suggested)" section rather than jumping between topics randomly.
- Instructors: adopt notebooks as lab exercises, add assessment items, and redistribute with solutions for guided learning.

## Quick environment notes
Recommended Python ecosystem: Python 3.9+, NumPy, SciPy, Matplotlib, pandas, jupyter-book, myst-nb. See the README for environment setup and installation instructions.

---
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
