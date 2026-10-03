# Metrology and Uncertainty — Introduction and Learning Goals

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

### Laboratory notebook

Keep a good laboratory notebook for the course: date, name, instruments and their
calibration stickers, temperature, and every reading, laid out so outliers stand out.
Guides: [MIT](https://web.mit.edu/me-ugoffice/communication/labnotebooks.pdf),
[Science Buddies](https://www.sciencebuddies.org/science-fair-projects/science-fair/laboratory-notebooks-stem),
[UBC](https://phas.ubc.ca/~phys259/2012-13Term1/pickyTA_ENPH259example.htm).

## Ordered reading (suggested)

Foundations first, then the core lecture and workflow, then worked examples of increasing
difficulty, finishing with two full real-world budgets and capstones.

1. [Significant digits](theory-significant_digits.md) — how many digits to keep, and how to report $x \pm u$ (1 sig. fig. for $u$).
2. [Standardization and Traceability](theory-standardization.md) — standards, traceability chains, common terminology.
3. [Short summary of the ``Measurement good practice guide '' by NPL](theory-best_practice_summary.md) — error vs uncertainty, Type A/B in one precis.
4. [The Generalized Measurement System](theory-general_measurement_system_analysis.md) — system-level thinking: stages, signals, error sources at each block.
5. [Basic error analysis](theory-02_basic_error_analysis.md) — systematic vs random errors, RSS combination, $P$/$B$ notation, small-sample $t$ note.
6. [Uncertainty 101](theory-01_uncertainty101.md) — the core lecture: Type A/B, divisors, combined and expanded uncertainty on the caliper example ($\ell = 21.49 \pm 0.05$ mm, $k=2$).
7. [The Engineer's 9-Step Uncertainty Analysis Checklist](theory-checklist.md) — the workflow (with the NASA 5-step variant as sidebar).
8. [Engineering Example: Uncertainty Analysis in Mechanical Measurements](theory-example_uncertainty_analysis.md) — full 8-step shaft measurement.
9. [Simple example of mechanical measurement with uncertainty analysis](theory-simple_example.md) — string and tape measure, plus how to (carefully) use AI tools on the guides.
10. [Sources of Uncertainty in Measurement for Every Uncertainty Budget](theory-uncertainty_sources_notebook.md) — the 8-source catalog with instrument examples.
11. [Comparing Two Methods: Cylinder Volume](theory-comparing_two_methods_cylinder_volume.md) — geometric vs gravimetric, dominant contributors, fractional-form appendix.
12. [How to estimate the uncertainty of a slope for static calibration or regression](theory-uncertainty_of_a_slope.md) — **interactive**: drag $u(I)$ and watch the slope interval change.
13. [Propagating uncertainty using Monte-Carlo simulations](theory-uncertainty_propagation_monte_carlo_gum.md) — **interactive**: non-normal outputs, cube/thermal/cosine/density examples, best practices.
14. [Sensitivity Coefficients in Uncertainty Budgets](theory-Sensitivity_Coefficients_Uncertainty.md) — partial derivatives as weights, building-height example.
15. [Introduction to uncertainty analysis](theory-surface_roughness_budget.md) — full surface-roughness budget with Welch–Satterthwaite.
16. [Full Uncertainty Budget of a Hot-Wire Anemometer for Isothermal Turbulent Air Flow in a Wind Tunnel](theory-hot-wire_uncertainty_budget.md) — complete 24-source real-world budget.
17. [Mars Rover Temperature Measurement & Uncertainty Analysis](theory-exam_example.md) — capstone: instrument selection, static/dynamic calibration design, full 8-step exam answer.
18. [Teaching Measurement in the Introductory Physics Laboratory](theory-teaching_measurement_introductory_physics_lab.md) — pedagogy capstone: plain-language guide plus instructor material.

Rationale: students first acquire reporting habits and vocabulary, then the propagation toolbox, then the canonical workflow — each worked example reuses the same 8 steps on harder systems until the capstones.

---

## What comes next?

Now that you understand *what* uncertainty is and where it comes from, the **Statistics** chapter teaches you how to *quantify* it from real measurement data. You'll learn to use histograms, distributions, and statistical tests to characterize the variability in your measurements — which feeds directly into Type A uncertainty budgets.
