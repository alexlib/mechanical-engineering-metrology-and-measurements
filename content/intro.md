# Mechanical Engineering Metrology and Measurements (MEMM)

An open-source book of interactive notebooks and worked examples, prepared by
[Prof. Alex Liberzon](https://turbulencelab.sites.tau.ac.il), School of
Mechanical Engineering, Faculty of Engineering, Tel Aviv University, for the
course called in many places "Mechanical Measurements Lab 1", "Theory and Design
of Mechanical Measurements", or "Introduction to Measurements for Mechanical
Engineers".

This book does not replace the course materials but organizes them into a
readable sequence. We hope it is useful as learning material for undergraduate
engineering laboratory courses. It is an open-source project, and any
contribution is welcome (contact on [GitHub](https://github.com/alexlib)).

## How this book is organised

The chapter sequence and the topic grouping follow a widely used structure for
undergraduate instrumentation courses. We are grateful to Adam W. Duran for
permitting the reuse of that structure and for the reference material that
shaped it:

> MEGN 300: Instrumentation & Automation course materials by Adam W. Duran,
> Colorado School of Mines, used under CC BY 4.0.
> Source: [https://github.com/professor-duran/MEGN300](https://github.com/professor-duran/MEGN300)

All content, code, and worked examples in this book are our own; the attribution
above covers the course structure and sequencing only.

## Textbook and relevant books

This course follows the [@textbook]. It is also recommended to consult
[@dunn_davis] and [@wheeler].


---

This book collects practical notebooks and concise explanations to teach core
concepts in mechanical engineering metrology and measurements. Content
emphasizes hands-on examples, reproducible analyses, and problem-solving skills
appropriate for undergraduate laboratory and lecture use.

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

**Reading order:** work through the chapters in the order they appear in the
sidebar. Each chapter opens with a page explaining what it covers, what you
should already know, and the reasoning behind its sequence — start there rather
than jumping into a notebook.

- Every chapter begins with an introduction page: learning objectives, key
  concepts, prerequisites, a suggested reading path, and a note on what the
  chapter enables you to do next.
- Pages are numbered notebooks with prose between them. Read the prose, then run
  the notebook; the figures are regenerated when the book is built, so what you
  see is what the code actually produces.
- Many pages carry **Open in molab**, **View on GitHub**, and **Download `.py`**
  buttons, so you can pick up any example as a live, editable notebook.
- Interactive pages have a slider or switch you can move; the figure updates as
  you drag. These are worth exploring rather than reading.
- If a concept feels under-explained, the "Ordered reading" list at the end of
  each chapter introduction points to the pages that develop it in depth.

## Quick environment notes

Python 3.11 or newer, with NumPy, SciPy, Matplotlib, pandas, and SymPy. See the
[README](https://github.com/alexlib/mechanical-engineering-metrology-and-measurements)
for installation and for how to build the book locally.

---
## Table of contents
```{tableofcontents}
```

## Copyright and attribution

Content in this book is released under
[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

<a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/">
<img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" /> </a>

To the extent possible under law, the person who associated CC0 with this work
has waived all copyright and related or neighboring rights to this work.

The chapter structure and topic sequencing follow
[MEGN 300: Instrumentation & Automation](https://github.com/professor-duran/MEGN300)
course materials by Adam W. Duran, Colorado School of Mines, used under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

<!-- 
## References
```{bibliography}
``` -->
