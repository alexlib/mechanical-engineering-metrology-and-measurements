# Calibration — Introduction and Learning Goals

Short summary
Calibration methods and error analysis for sensors: linear & nonlinear regression, hysteresis, sensitivity, and full calibration workflow.

Learning objectives
- Perform linear regression for sensor calibration and compute confidence intervals.
- Analyze hysteresis and nonlinearity errors.
- Design calibration experiments and propagate calibration uncertainty into measurements.

Key concepts (brief)
- Regression residuals, standard error, and calibration curve interpretation.
- Hysteresis and repeatability characterization.
- Sensitivity analysis and combining calibration with measurement uncertainty.

Prerequisites
Basic regression, statistics, and familiarity with plotting in Python.

---

## Ordered reading (suggested)

Follow this sequence to learn calibration from theory to practice. The order moves from foundational regression concepts, through systematic error characterization, to applied examples on real instruments.

2. [calibration-regression_analysis.md](calibration-regression_analysis.md) — detailed regression analysis with uncertainty in slope and intercept
3. [calibration-sensitivity_analysis.md](calibration-sensitivity_analysis.md) — how to estimate sensitivity coefficients from calibration data
4. [calibration-hysteresis_error_analysis.md](calibration-hysteresis_error_analysis.md) — identifying and quantifying hysteresis as a Type B uncertainty source
5. [calibration-calibration_non_linear_relations.md](calibration-calibration_non_linear_relations.md) — polynomial and logarithmic fits when linearity fails
6. **[Calibration Examples: Real Sensors & Instruments](calibration-calibration_sensor_examples.md)** — Comprehensive reference guide with links to all sensor calibration notebooks (LVDT, pressure, micrometer, orifice, weight scale). Choose examples matching your lab instruments.

Rationale: Students first master linear regression theory, then learn to identify and quantify systematic errors from the calibration process (hysteresis, linearity, repeatability). The consolidated examples guide at the end shows how to apply all these concepts to real sensors and helps students navigate to the right example for their needs. This hands-on, practical focus grounds the theory in authentic measurement scenarios.

---

## The Static Calibration Process

Static calibration is a procedure used to characterize a measurement system by applying a known, constant input value to the system and observing the resulting output value. The term "static" refers to the fact that the variables are held constant, meaning the input is not dependent on time.

### Purpose

The primary purpose of static calibration is twofold:

1. **Functional Relationship:** To develop a functional relationship, or a correlation ($y = f(x)$), between the system's known input ($x$) and its output ($y$). This correlation is often determined using curve fitting techniques, such as regression analysis, on the calibration curve.
2. **Systematic Error Identification:** To identify and quantify systematic errors (biases) such as zero error, linearity error, and hysteresis.

### Procedure Steps

To perform a static calibration, you generate a calibration curve by recording the output values ($y_i$) for a range of known input values ($x_i$).

* **Reference Standard:** A **standard** (known value) that is traceable to national standards must be used. This reference instrument should have significantly lower uncertainty than the instrument being tested.
* **Controlled Points:** The chamber or environment is set to a series of stable, discrete input points across the operational range.
* **Hysteresis Check:** Measurements should be taken by varying the input value in both the increasing (upscale) and decreasing (downscale) directions to assess hysteresis.
* **Data Collection:** At each stable point, the system is allowed to reach thermal equilibrium, and multiple readings are taken to assess repeatability.
* **Data Analysis:** The data is plotted to create the calibration curve. This curve is used to determine key parameters like **static sensitivity** (the slope of the curve), and to quantify errors like **linearity** and **hysteresis**.

### Error Analysis and Uncertainty Categorization

In metrology, an **error** is the quantifiable difference between an estimate and the "true value," which can sometimes be corrected. **Uncertainty** is the quantification of the doubt about that measurement result.

Systematic errors found during calibration, such as zero offset, can sometimes be corrected by adjustment. If the error cannot be corrected (e.g., hysteresis, remaining linearity deviation), the quantified range of that potential error must be included in the uncertainty budget as a Type B contribution.

The table below outlines common error types, how they are determined, and their subsequent role in uncertainty analysis:

| Error Type | Description & Measurement Method | Systematic Error Correction? | Uncertainty Type/Source |
| :--- | :--- | :--- | :--- |
| **Repeatability Error ($u_{rep}$)** | The variability or scatter found when the same input is applied repeatedly. Accounts for random variations. **Measured:** Calculated as the standard deviation ($S_x$) from repeated readings taken during the static calibration procedure. | No. This is a source of **random error**. | **Type A**. Calculated as the standard deviation of the mean ($S_x / \sqrt{n}$). |
| **Static Sensitivity ($K$)** | The slope of the calibration curve at any given point. **Measured:** Defined as $K(x_1) = (dy/dx)_{x=x_1}$. | Used to define the functional relationship for converting output ($y$) back to input ($x$). | **Type B** (The Sensitivity *Error* ($u_K$) is a statistical measure of random error in the estimate of the slope). |
| **Zero Error ($u_z$)** | A vertical shift or offset from the true zero point of the instrument. **Measured:** Determined by checking the output when a zero input condition is applied. | Yes. If possible, the error is reduced by physically adjusting the output under a zero input condition. | **Type B** (The remaining, uncorrected zero uncertainty, often related to resolution). |
| **Linearity Error ($u_L$)** | The deviation of the calibration curve from an expected straight line. **Measured:** Calculated as the maximum deviation between the actual output $y(x)$ and the best-fit linear output $y_L(x)$. | If the deviation is large, the correction may involve using a higher-order polynomial fit, which models the error. | **Type B** (If a linear fit is required, the linearity error bounds define a semi-range limit for a Type B rectangular distribution). |
| **Hysteresis Error ($u_h$)** | The maximum difference in output value when the input is approached from increasing versus decreasing directions. Caused by friction or residual charge. **Measured:** Calculated as the maximum difference between upscale and downscale readings at the same input point across the full range. | No. Typically quantified, but not corrected. It is a systematic bias that must be factored into the uncertainty estimate. | **Type B** (The maximum hysteresis error defines the limit for a Type B uncertainty estimate, often expressed as a percentage of the full-scale output range). |
| **Overall Instrument Error ($u_c$)** | The total quantified uncertainty of the instrument due to known effects (e.g., combining $u_h$, $u_L$, $u_K$). **Measured:** Combined using the Root-Sum-Squared (RSS) method: $u_c = \sqrt{u_h^2 + u_L^2 + u_K^2 + \dots}$. | If the calibration shows a consistent offset or non-linearity, a correction can be applied to future readings. | **Combined Standard Uncertainty** ($u_c$). |

---

## What comes next?

Calibration tells you how to *characterize and reduce* uncertainty in your instruments — but instruments exist in the real world, where dynamic effects, noise, and signal acquisition choices matter. The **Dynamic Signals** chapter teaches you how measurement systems actually respond to inputs, and **Signal Processing** shows you frequency-domain tools to separate true signals from noise.




<!-- AUTOGEN_START -->
## Pages in this chapter

- [calibration-calibration_simulation](calibration-calibration_simulation.md)
- [Sensitivity estimate example](calibration-sensitivity_analysis.md)
- [Estimate $a,b$ and also $\Delta a$ and $\Delta b$](calibration-linear_regression.md)
- [Lecture 6](calibration-regression_analysis.md)
- [Sensitivity error example](calibration-hysteresis_error_analysis.md)
- [Linearity error example](calibration-Lineariy_error_example.md)
- [Hysteresis example](calibration-calibration_error_analysis_2.md)
- [Hysteresis and regression analysis example](calibration-calibration_error_analysis_pressure.md)
- [Calibration of non-linear relations](calibration-calibration_non_linear_relations.md)
- [Calculate averages for the plot](calibration-weight_scale_example_Wheeler.md)
- [--- Input Values (Slide 4) ---](calibration-orifice_calibration_example.md)
- [Calibration and uncertainty analysis - virtual experiment](calibration-pressure_calibration_example.md)
- [calibration-lvdt_calibration_example](calibration-lvdt_calibration_example.md)
- [calibration-lvdt_calibration_2](calibration-lvdt_calibration_2.md)
- [Micrometer calibration using gage block](calibration-micrometer_calibration.md)
- [Measurement Uncertainty Budget Examples (SWGDRUG SD-3)](calibration-several_calibration_examples.md)
- [Calibration of non-linear (logarithmic) function](calibration-calibration_curve_log_log.md)
- [Calibration and uncertainty analysis - virtual experiment](calibration-full_calibration_analysis_example.md)

<!-- AUTOGEN_END -->

