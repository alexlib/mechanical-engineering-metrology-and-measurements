# Uncertainty — Introduction and Learning Goals

This chapter covers measurement theory or *metrology*: uncertainty concepts, best practices, analytical measurement system analysis, examples of measurement systems.

### Learning objectives
- Understand types of *measurement uncertainty* and how to report them.
- Distinguish repeatability vs reproducibility, bias, and systematic errors.
- Apply basic uncertainty propagation.
- Recognize good-practice recommendations for lab notebooks and reporting.

### Key concepts
- GUM-style uncertainty vs Type A/B estimates.
- Propagation of uncertainty in complex measurements

### Prerequisites
Basic probability, calculus, and comfort with Python, Numpy, Matplotlib, Scipy, Jupyter.

## Ordered reading (suggested)

Follow this sequence when teaching or self-studying. Start with lab practice and best-practice guidance, then measurement-system analysis and elementary worked examples, then uncertainty concepts and quantitative propagation methods (analytical & Monte Carlo), and finish with supplementary case studies.

Core path:

1. [Laboratory Notebook](theory-laboratory_notebook.md) — practical lab notebook practices and data recording.
2. [Significant digits](theory-significant_digits.md) — how many digits to keep and report.
3. [Short summary of the ``Measurement good practice guide '' by NPL](theory-best_practice_summary.md) — concise recommendations for reporting and reproducibility.
4. [Standardization and Traceability](theory-standartization.md) — standards and common terminology.
5. [The Generalized Measurement System](theory-general_measurement_system_analysis.md) — system-level thinking and error sources.
6. [Uncertainty 101](theory-01_uncertainty101.md) — what uncertainty is, Type A vs Type B, combined and expanded uncertainty.
7. [The Engineer's 9-Step Uncertainty Analysis Checklist](theory-checklist.md) — step-by-step workflow for an uncertainty budget.
8. [Basic error analysis](theory-02_basic_error_analysis.md) — errors, propagation, worst-case vs RSS.
9. [Engineering Example: Uncertainty Analysis in Mechanical Measurements](theory-example_uncertainty_analysis.md) — full worked example.
10. [Using simulations to explain uncertainty](theory-simulations_for_uncertainty.md) — simulation-driven exploration of uncertainty.
11. [How to estimate the uncertainty of a slope for static calibration or regression](theory-uncertainty_of_a_slope.md) — propagation for regression-derived quantities.
12. [Propagating uncertainty using Monte-Carlo simulations](theory-uncertainty_propagation_monte_carlo_gum.md) — Monte Carlo propagation following GUM ideas.
13. [Comparing Two Methods: Cylinder Volume](theory-comparing_two_methods_cylinder_volume.md) — two ways to get the same volume, compared.
14. [Cylinder Volume: Nominal Values and Uncertainty](theory-volume_cylinder_undertainty_example.md) — nominal values and uncertainty calculation.
15. [Full Uncertainty Budget of a Hot-Wire Anemometer for Isothermal Turbulent Air Flow in a Wind Tunnel](theory-hot-wire_uncertainty_budget.md) — complete real-world budget.

Supplementary notes and case studies:

16. [Sensitivity Coefficients in Uncertainty Budgets](theory-Sensitivity_Coefficients_Uncertainty.md) — what sensitivity coefficients do and how to use them.
17. [Simple example of mechanical measurement with uncertainty analysis](theory-simple_example.md) — a short worked example linking practice and theory.
18. [Uncertainty Example: Cylinder Volume from Caliper and Micrometer](theory-uncertainty_example.md) — basic uncertainty calculations and interpretation.
19. [Sources of Uncertainty in Measurement for Every Uncertainty Budget](theory-uncertainty_sources_notebook.md) — checklist of sources for every budget.
20. [Introduction to uncertainty analysis](theory-surface_roughness_budget.md) — surface-roughness budget example.
21. [Uncertainty Analysis](theory-uncertainty_analysis_NASA.md) — applied example from NASA guidance.
22. [Uncertainty in simple terms from IAEA](theory-iaea_uncertainty_presentation.md) — community presentation and advanced perspectives.
23. [Mars Rover Temperature Measurement & Uncertainty Analysis](theory-exam_example.md) — exam-style temperature example.
24. [Teaching uncertainty in mechanical measurements](theory-teaching_measurement_uncertainty.md) — pedagogical overview of uncertainty.
25. [Teaching Measurement in the Introductory Physics Laboratory](theory-teaching_measurement_introductory_physics_lab.md) — teaching perspective from physics labs.
26. [Using AI tools to learn uncertainty](theory-example_from_best_practice.md) — illustrated application of best practices.

Rationale: this ordering lets students first acquire good lab habits and reporting skills, then build a conceptual toolbox for system analysis, then learn measurement uncertainty in increasing rigor (examples → slope propagation → Monte Carlo → case studies).

---

## What comes next?

Now that you understand *what* uncertainty is and where it comes from, the **Statistics** chapter teaches you how to *quantify* it from real measurement data. You'll learn to use histograms, distributions, and statistical tests to characterize the variability in your measurements — which feeds directly into Type A uncertainty budgets.
