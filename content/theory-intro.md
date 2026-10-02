# Metrology theory — Introduction and Learning Goals

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


<!-- AUTOGEN_START -->
## Pages in this chapter

- [Laboratory Notebook](theory-laboratory_notebook.md)
- [Short summary of the ``Measurement good practice guide '' by NPL](theory-best_practice_summary.md)
- [Standardization and Traceability](theory-standartization.md)
- [theory-general_measurement_system_analysis](theory-general_measurement_system_analysis.md)
- [Using simulations to explain uncertainty](theory-simulations_for_uncertainty.md)
- [Basic error analysis](theory-02_basic_error_analysis.md)
- [How to estimate the uncertainty of a slope for static calibration or regression](theory-uncertainty_of_a_slope.md)
- [Propagating uncertainty using Monte-Carlo simulations](theory-uncertainty_propagation_monte_carlo_gum.md)
- [Nominal (Mean) Values](theory-volume_cylinder_undertainty_example.md)
- [Full Uncertainty Budget of a Hot-Wire Anemometer for Isothermal Turbulent Air Flow in a Wind Tunnel](theory-hot-wire_uncertainty_budget.md)
- [Simple example of mechanical measurement with uncertainty analysis](theory-simple_example.md)
- [Using AI tools to learn uncertainty](theory-example_from_best_practice.md)
- [Uncertainty in simple terms from IAEA](theory-iaea_uncertainty_presentation.md)
- [theory-uncertainty_example](theory-uncertainty_example.md)
- [Uncertainty Analysis](theory-uncertainty_analysis_NASA.md)
- [Sources of Uncertainty in Measurement for Every Uncertainty Budget](theory-uncertainty_sources_notebook.md)
- [Introduction to uncertainty analysis](theory-surface_roughness_budget.md)
- [Teaching uncertainty in mechanical measurements](theory-teaching_measurement_uncertainty.md)

<!-- AUTOGEN_END -->


## Ordered reading (suggested)

Follow this sequence when teaching or self-studying. The order moves from foundational lab practice and best-practice guidance, to measurement-system analysis and elementary worked examples, then to uncertainty concepts and quantitative propagation methods (analytical & Monte Carlo), and finishes with advanced case studies and community presentations.

1. [theory-laboratory_notebook.md](theory-laboratory_notebook.md) — practical lab notebook practices and data recording.
2. [theory-best_practice_summary.md](theory-best_practice_summary.md) — concise recommendations for reporting and reproducibility.
3. [theory-teaching_measurement_uncertainty.md](theory-teaching_measurement_uncertainty.md) — pedagogical overview of uncertainty.
4. [theory-standartization.md](theory-standartization.md) — standards and common terminology.
5. [theory-general_measurement_system_analysis.md](theory-general_measurement_system_analysis.md) — system-level thinking and error sources.
6. [theory-simple_example.md](theory-simple_example.md) — a short worked example linking practice and theory.
7. [theory-example_from_best_practice.md](theory-example_from_best_practice.md) — illustrated application of best practices.
8. [theory-uncertainty_example.md](theory-uncertainty_example.md) — basic uncertainty calculations and interpretation.
9. [theory-uncertainty_of_a_slope.md](theory-uncertainty_of_a_slope.md) — propagation for regression-derived quantities.
10. [theory-uncertainty_propagation_monte_carlo_gum.md](theory-uncertainty_propagation_monte_carlo_gum.md) — Monte Carlo propagation following GUM ideas.
11. [theory-simulations_for_uncertainty.md](theory-simulations_for_uncertainty.md) — simulation-driven exploration of uncertainty.
12. [theory-uncertainty_analysis_NASA.md](theory-uncertainty_analysis_NASA.md) — applied example from NASA guidance.
13. [theory-iaea_uncertainty_presentation.md](theory-iaea_uncertainty_presentation.md) — community presentation and advanced perspectives.
14. [Watch the 1 hr video by Fluke - leading measurement equipment company](https://www.fluke.com/en-us/learn/blog/electrical-calibration/introduction-iso-guide-expression-uncertainty-measurement-gum)

Rationale: this ordering lets students first acquire good lab habits and reporting skills, then build a conceptual toolbox for system analysis, then learn measurement uncertainty in increasing rigor (examples → slope propagation → Monte Carlo → case studies). Use the checklists added to notebooks to guide in-class or lab activities.

---

## What comes next?

Now that you understand *what* uncertainty is and where it comes from, the **Statistics** chapter teaches you how to *quantify* it from real measurement data. You'll learn to use histograms, distributions, and statistical tests to characterize the variability in your measurements — which feeds directly into Type A uncertainty budgets.
