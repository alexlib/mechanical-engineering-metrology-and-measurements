# Calibration Examples: Real Sensors and Instruments

This page is a reference guide to the calibration examples in this chapter. Each example shows how to apply static calibration, error analysis, and uncertainty budgeting to a real measurement instrument.

## Quick Reference: Sensor Calibration Workflows

| Instrument | Key Error | Notebook | Best For Learning |
|---|---|---|---|
| **LVDT** (Linear Variable Differential Transformer) | Linearity, hysteresis | [calibration-lvdt_calibration_example.md](calibration-lvdt_calibration_example.md) or [calibration-lvdt_calibration_2.md](calibration-lvdt_calibration_2.md) | Linear calibration curve, typical electronics |
| **Pressure Transducer** | Hysteresis, non-linearity | [calibration-pressure_calibration_example.md](calibration-pressure_calibration_example.md) or [calibration-calibration_error_analysis_pressure.md](calibration-calibration_error_analysis_pressure.md) | Real data, systematic errors, uncertainty propagation |
| **Micrometer** | Resolution, repeatability, calibration blocks | [calibration-micrometer_calibration.md](calibration-micrometer_calibration.md) | Mechanical instruments, gage block standards |
| **Orifice Plate** (Flow measurement) | Non-linear response | [calibration-pressure_calibration_example.md](calibration-pressure_calibration_example.md) (orifice section) | Application-specific calibration |
| **Weight Scale** (Wheeler method) | Zero error, hysteresis | [calibration-weight_scale_example_Wheeler.md](calibration-weight_scale_example_Wheeler.md) | Historical method, mechanical devices |

---

## How to Use These Examples

1. **Choose your instrument type** — find it in the table above
2. **Run the recommended notebook** — execute cells and observe:
   - How reference standards are applied
   - Hysteresis checks (up-scale vs down-scale)
   - Regression fits and residual analysis
   - Error quantification and Type B uncertainty sources
   - Final calibration curve and uncertainty budget
3. **Adapt to your own instrument** — the same workflow applies to thermometers, load cells, rotational encoders, etc.

---

## Common Patterns Across All Examples

Every calibration follows this structure:

### 1. **Reference Standard & Setup**
   - Choose a reference with lower uncertainty than your test instrument
   - Document traceability and uncertainty of the reference
   - Example: calibrated gage blocks for mechanical instruments, pressure standard for transducers

### 2. **Data Collection**
   - Apply known input values across the full operational range
   - At each point: wait for equilibrium, record multiple readings (assess repeatability)
   - **Hysteresis check:** measure on both increasing and decreasing input to detect path-dependent errors
   - Example: temperature chamber holding 5 set points, pressure pump at 10 pressures

### 3. **Initial Analysis & Error Detection**
   - Plot output vs. input
   - Check for: zero offset, non-linearity, hysteresis, outliers
   - Compute repeatability (Type A) as standard deviation of repeated measurements
   - Example: LVDT output should be linear; pressure transducer might show 2% non-linearity

### 4. **Fit a Calibration Curve**
   - Linear regression for linear instruments
   - Polynomial or logarithmic fit for non-linear instruments
   - Report: equation, $R^2$, standard error of regression
   - Example: $y = 0.502x + 2.3$, $u_\text{regression} = 0.1$ V

### 5. **Quantify Systematic Errors** (Type B sources)
   - **Hysteresis error** ($u_h$): max difference between up/down curves
   - **Linearity error** ($u_L$): max deviation from best-fit line
   - **Zero error** ($u_z$): offset when input = 0
   - **Sensitivity uncertainty** ($u_K$): confidence in the slope
   - Example: hysteresis = ±0.3%, linearity = ±0.5%

### 6. **Build Uncertainty Budget**
   - Combine Type A (repeatability) and Type B (systematic) sources
   - Use root-sum-square (RSS): $u_c = \sqrt{u_A^2 + u_h^2 + u_L^2 + u_z^2 + \dots}$
   - Compute expanded uncertainty: $U = k \cdot u_c$ (typically $k=2$ for 95% confidence)
   - Example: $u_c = \pm 0.7\%$, $U = \pm 1.4\%$

---

## Example-Specific Notes

### LVDT Calibration
- **Why LVDT first?** Excellent linearity, no hysteresis, clean data → easiest to learn from
- **What to notice:** How gage blocks establish reference standard, data collection under different loading scenarios
- See: [calibration-lvdt_calibration_example.md](calibration-lvdt_calibration_example.md)

### Pressure Transducer
- **Why challenging?** Non-linear response (often log-scale at low pressures), noticeable hysteresis
- **What to notice:** How to fit polynomial instead of linear, identifying and quantifying hysteresis error
- See: [calibration-pressure_calibration_example.md](calibration-pressure_calibration_example.md)

### Micrometer
- **Why practical?** Mechanical instrument students will use in labs; familiar uncertainty sources (gage block tolerance, surface finish)
- **What to notice:** How resolution and repeatability limit the usable precision; concept of "last-digit uncertainty"
- See: [calibration-micrometer_calibration.md](calibration-micrometer_calibration.md)

### Non-linear Relations (Orifice, Polynomial Fits)
- **Why included?** Many real sensors don't follow $y = mx + b$; logarithmic pressure transducers, non-linear thermal sensors, etc.
- **What to notice:** How to choose model (polynomial order, log vs linear); trade-off between complexity and accuracy
- See: [calibration-calibration_non_linear_relations.md](calibration-calibration_non_linear_relations.md)

### Weight Scale (Wheeler Method)
- **Why historical?** Wheeler method is elegant and still used for some mechanical instruments
- **What to notice:** How mechanical hysteresis is characterized; pure Type B error quantification without statistical fitting
- See: [calibration-weight_scale_example_Wheeler.md](calibration-weight_scale_example_Wheeler.md)

---

## Tips for Your Own Instrument

1. **Start simple:** If your instrument looks linear, use linear regression (LVDT example)
2. **Don't over-fit:** Resist the urge to fit 5th-order polynomials. A simple model with clear uncertainty is better than a complex one that overfits noise
3. **Always measure hysteresis:** Even if you think there's none, check up-scale vs down-scale. It often reveals mechanism (friction, compliance, temperature lag)
4. **Propagate uncertainty into use:** Once you have the calibration curve and its uncertainty, use it to predict how much margin/confidence you have in future measurements
5. **Document everything:** Which standard? What temperature? What humidity? A calibration is only useful if the conditions are repeatable

---

## Recommended Reading Order

2. [calibration-regression_analysis.md](calibration-regression_analysis.md) — detailed analysis with uncertainty
3. [calibration-lvdt_calibration_example.md](calibration-lvdt_calibration_example.md) — simple, clean example
4. [calibration-pressure_calibration_example.md](calibration-pressure_calibration_example.md) — introduces complexity (non-linearity, hysteresis)
5. [calibration-calibration_non_linear_relations.md](calibration-calibration_non_linear_relations.md) — when linear fit fails
6. [calibration-hysteresis_error_analysis.md](calibration-hysteresis_error_analysis.md) — deep dive into characterizing hysteresis

Then explore other sensors matching your interests (micrometer, scale, etc.).
