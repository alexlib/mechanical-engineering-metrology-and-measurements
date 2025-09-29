# Theory — Introduction and Learning Goals

Short summary
This chapter covers measurement theory: uncertainty concepts, best practices, measurement-system analysis, and worked Monte Carlo examples.

Learning objectives
- Understand types of measurement uncertainty and how to report them.
- Distinguish repeatability vs reproducibility, bias, and systematic errors.
- Apply basic uncertainty propagation (analytical and Monte Carlo).
- Recognize good-practice recommendations for lab notebooks and reporting.

Key concepts (brief)
- GUM-style uncertainty vs Type A/B estimates.
- Propagation of uncertainty for slopes and model parameters.
- Role of simulations (Monte Carlo) to validate analytical propagation.

Recommended notebooks to run
- uncertainty_example.ipynb
- uncertainty_of_a_slope.ipynb
- uncertainty_propagation_monte_carlo_gum.ipynb
- teaching_measurement_uncertainty.ipynb
- best_practice_summary.ipynb

Suggested exercises
- Compute and compare analytical and Monte Carlo propagation on a simple function.
- Prepare a short lab report following the best-practice notebook checklist.

Prerequisites
Basic probability, calculus, and comfort with Python arrays.

<!-- AUTOGEN_START -->
## Pages in this chapter

- [Sensitivity Coefficients in Uncertainty Budgets](Sensitivity_Coefficients_Uncertainty.md)
- [Short summary of the ``Measurement good practice guide '' by NPL](best_practice_summary.ipynb)
- [Mars Rover Temperature Measurement & Uncertainty Analysis](exam_example.md)
- [Using AI tools to learn uncertainty](example_from_best_practice.ipynb)
- [Engineering Example: Uncertainty Analysis in Mechanical Measurements](example_uncertainty_analysis.md)
- [## General measurement system diagram](general_measurement_system_analysis.ipynb)
- [Uncertainty in simple terms from IAEA](iaea_uncertainty_presentation.ipynb)
- [Laboratory Notebook](laboratory_notebook.ipynb)
- [Significant digits](significant_digits.md)
- [Simple example of mechanical measurement with uncertainty analysis](simple_example.ipynb)
- [Using simulations to explain uncertainty](simulations_for_uncertainty.ipynb)
- [Standardization](standartization.ipynb)
- [Teaching Measurement in the Introductory Physics Laboratory](teaching_measurement_introductory_physics_lab.md)
- [Teaching uncertainty in mechanical measurements](teaching_measurement_uncertainty.ipynb)
- [Uncertainty 101](uncertainty101.md)
- [Uncertainty Analysis](uncertainty_analysis_NASA.ipynb)
- [uncertainty_example](uncertainty_example.ipynb)
- [How to estimate the uncertainty of a slope for static calibration or regression](uncertainty_of_a_slope.ipynb)
- [Propagating uncertainty using Monte-Carlo simulations](uncertainty_propagation_monte_carlo_gum.ipynb)
<!-- AUTOGEN_END -->

## Ordered reading (suggested)

Follow this sequence when teaching or self-studying. The order moves from foundational lab practice and best-practice guidance, to measurement-system analysis and elementary worked examples, then to uncertainty concepts and quantitative propagation methods (analytical & Monte Carlo), and finishes with advanced case studies and community presentations.

1. [laboratory_notebook.ipynb](laboratory_notebook.ipynb) — practical lab notebook practices and data recording.
2. [best_practice_summary.ipynb](best_practice_summary.ipynb) — concise recommendations for reporting and reproducibility.
3. [teaching_measurement_uncertainty.ipynb](teaching_measurement_uncertainty.ipynb) — pedagogical overview of uncertainty.
4. [standartization.ipynb](standartization.ipynb) — standards and common terminology.
5. [general_measurement_system_analysis.ipynb](general_measurement_system_analysis.ipynb) — system-level thinking and error sources.
6. [simple_example.ipynb](simple_example.ipynb) — a short worked example linking practice and theory.
7. [example_from_best_practice.ipynb](example_from_best_practice.ipynb) — illustrated application of best practices.
8. [uncertainty_example.ipynb](uncertainty_example.ipynb) — basic uncertainty calculations and interpretation.
9. [uncertainty_of_a_slope.ipynb](uncertainty_of_a_slope.ipynb) — propagation for regression-derived quantities.
10. [uncertainty_propagation_monte_carlo_gum.ipynb](uncertainty_propagation_monte_carlo_gum.ipynb) — Monte Carlo propagation following GUM ideas.
11. [simulations_for_uncertainty.ipynb](simulations_for_uncertainty.ipynb) — simulation-driven exploration of uncertainty.
12. [uncertainty_analysis_NASA.ipynb](uncertainty_analysis_NASA.ipynb) — applied example from NASA guidance.
13. [iaea_uncertainty_presentation.ipynb](iaea_uncertainty_presentation.ipynb) — community presentation and advanced perspectives.

Rationale: this ordering lets students first acquire good lab habits and reporting skills, then build a conceptual toolbox for system analysis, then learn measurement uncertainty in increasing rigor (examples → slope propagation → Monte Carlo → case studies). Use the checklists added to notebooks to guide in-class or lab activities.
