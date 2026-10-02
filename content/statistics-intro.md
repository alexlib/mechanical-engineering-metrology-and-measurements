# Statistics — Introduction and Learning Goals

Short summary
Hands-on statistics for measurement data: distributions, descriptive stats, hypothesis testing, outliers, and the central limit theorem.

Learning objectives
- Compute and interpret mean, variance, confidence intervals.
- Apply t-tests, chi-square tests, and identify outliers.
- Relate histograms to probability distributions and sampling variability (CLT).

Key concepts (brief)
- Sampling distributions and the Central Limit Theorem.
- When to use t-distribution vs normal approximation.
- Robust statistics and practical outlier handling.

Prerequisites
Introductory probability and basic Python (NumPy, matplotlib).

---

## Ordered reading (suggested)

Follow this sequence to build statistical tools progressively. The order moves from basic descriptive statistics, through probability distributions and hypothesis testing, and concludes with practical outlier detection methods.

1. [Very basic review of some statistics terms](statistics-basic_statistics.md) — mean, variance, standard deviation, and fundamental statistical concepts
2. [Chi-square Test](statistics-Lecture_5.md) — probability fundamentals and introduction to distributions
3. [Probability Distributions and the Central Limit Theorem](statistics-distributions.md) — overview of common probability distributions and their properties
4. [Central limit theorem (or why errors often look Gaussian)](statistics-Central_limit_theorem_illustration.md) — why errors are often Gaussian; the power of averaging many measurements
5. ["Student" t-distribution](statistics-t-distribution.md) — Student's t-distribution and its importance for small samples in measurement data
6. [t-test](statistics-t-test.md) — hypothesis testing and comparing two datasets
7. [Outlier Detection: Modified Thompson Test](statistics-outliers_example.md) — detecting and handling outliers using the Modified Thompson test
8. [Outlier Detection in Regression Residuals](statistics-outliers_example_pairs.md) — outlier detection in regression residuals (bivariate data)

Rationale: Students first learn to compute and interpret basic statistics, then understand how distributions arise from data, then learn hypothesis testing and practical statistical tests. Outlier detection concludes the chapter because it often requires multiple statistical tools. Skip the redundant distribution exploration files — one comprehensive reference (`distributions.ipynb`) is sufficient.

---

## What comes next?

Now that you can *quantify uncertainty from data*, the **Calibration** chapter shows you how to use these statistical tools to characterize real instruments. You'll build calibration curves, estimate regression uncertainty, and learn to quantify systematic errors (Type B sources) that complement the statistical (Type A) errors you just learned to compute.
