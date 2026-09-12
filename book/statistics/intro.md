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

1. [basic_statistics.ipynb](basic_statistics.ipynb) — mean, variance, standard deviation, and fundamental statistical concepts
2. [Lecture_5.ipynb](Lecture_5.ipynb) — probability fundamentals and introduction to distributions
3. [distributions.ipynb](distributions.ipynb) — overview of common probability distributions and their properties
4. [Central_limit_theorem_illustration.ipynb](Central_limit_theorem_illustration.ipynb) — why errors are often Gaussian; the power of averaging many measurements
5. [t-distribution.ipynb](t-distribution.ipynb) — Student's t-distribution and its importance for small samples in measurement data
6. [t-test.ipynb](t-test.ipynb) — hypothesis testing and comparing two datasets
7. [outliers_example.ipynb](outliers_example.ipynb) — detecting and handling outliers using the Modified Thompson test
8. [outliers_example_pairs.ipynb](outliers_example_pairs.ipynb) — outlier detection in regression residuals (bivariate data)

Rationale: Students first learn to compute and interpret basic statistics, then understand how distributions arise from data, then learn hypothesis testing and practical statistical tests. Outlier detection concludes the chapter because it often requires multiple statistical tools. Skip the redundant distribution exploration files — one comprehensive reference (`distributions.ipynb`) is sufficient.

---

## What comes next?

Now that you can *quantify uncertainty from data*, the **Calibration** chapter shows you how to use these statistical tools to characterize real instruments. You'll build calibration curves, estimate regression uncertainty, and learn to quantify systematic errors (Type B sources) that complement the statistical (Type A) errors you just learned to compute.

<!-- AUTOGEN_START -->
## Pages in this chapter

- [Central limit theorem (or why errors often look Gaussian)](Central_limit_theorem_illustration.ipynb)
- [Statistical distribution](Exploring+different+distribution.ipynb)
- [## Lecture 5 - probability and statistics](Lecture_5.ipynb)
- [Very basic review of some statistics terms](basic_statistics.ipynb)
- [Statistics example](chi_square_test_example.ipynb)
- [Probability Distributions and the Central Limit Theorem](distributions.ipynb)
- [Statistical parameters using probability density function](estimate_mean_variance_median_using_pdf.ipynb)
- [histogram_to_distribution](histogram_to_distribution.ipynb)
- [Outliers](outliers_example-2.ipynb)
- [Outliers](outliers_example.ipynb)
- [Outliers example 2](outliers_example_pairs.ipynb)
- [Outliers](outliers_example_two.ipynb)
- ["Student" t-distribution](t-distribution.ipynb)
- [t-test](t-test.ipynb)
<!-- AUTOGEN_END -->
