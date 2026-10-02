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
## Ordered reading (suggested)

Follow this sequence when teaching or self-studying. The order moves from foundational lab practice and best-practice guidance, to measurement-system analysis and elementary worked examples, then to uncertainty concepts and quantitative propagation methods (analytical & Monte Carlo), and finishes with advanced case studies and community presentations.

1. [Laboratory Notebook](theory-laboratory_notebook.md) — practical lab notebook practices and data recording.
2. [Short summary of the ``Measurement good practice guide '' by NPL](theory-best_practice_summary.md) — concise recommendations for reporting and reproducibility.
3. [Teaching uncertainty in mechanical measurements](theory-teaching_measurement_uncertainty.md) — pedagogical overview of uncertainty.
4. [Standardization and Traceability](theory-standartization.md) — standards and common terminology.
5. [The Generalized Measurement System](theory-general_measurement_system_analysis.md) — system-level thinking and error sources.
6. [Simple example of mechanical measurement with uncertainty analysis](theory-simple_example.md) — a short worked example linking practice and theory.
7. [Using AI tools to learn uncertainty](theory-example_from_best_practice.md) — illustrated application of best practices.
8. [Uncertainty Example: Cylinder Volume from Caliper and Micrometer](theory-uncertainty_example.md) — basic uncertainty calculations and interpretation.
9. [How to estimate the uncertainty of a slope for static calibration or regression](theory-uncertainty_of_a_slope.md) — propagation for regression-derived quantities.
10. [Propagating uncertainty using Monte-Carlo simulations](theory-uncertainty_propagation_monte_carlo_gum.md) — Monte Carlo propagation following GUM ideas.
11. [Using simulations to explain uncertainty](theory-simulations_for_uncertainty.md) — simulation-driven exploration of uncertainty.
12. [Uncertainty Analysis](theory-uncertainty_analysis_NASA.md) — applied example from NASA guidance.
13. [Uncertainty in simple terms from IAEA](theory-iaea_uncertainty_presentation.md) — community presentation and advanced perspectives.
14. [Watch the 1 hr video by Fluke - leading measurement equipment company](https://www.fluke.com/en-us/learn/blog/electrical-calibration/introduction-iso-guide-expression-uncertainty-measurement-gum)

Rationale: this ordering lets students first acquire good lab habits and reporting skills, then build a conceptual toolbox for system analysis, then learn measurement uncertainty in increasing rigor (examples → slope propagation → Monte Carlo → case studies). Use the checklists added to notebooks to guide in-class or lab activities.

---

## What comes next?

Now that you understand *what* uncertainty is and where it comes from, the **Statistics** chapter teaches you how to *quantify* it from real measurement data. You'll learn to use histograms, distributions, and statistical tests to characterize the variability in your measurements — which feeds directly into Type A uncertainty budgets.
