---
title: Interactive Calibration-Error Simulation
---

## Interactive Calibration-Error Simulation

This is an interactive version of the **simulation of calibration errors**
notebook. Move the sliders to inject zero offset, sensitivity, linearity,
hysteresis, dead-band and resolution errors into an ideal sensor — the
simulated data, best-fit line and residual arrows update automatically.

It was converted from `calibration_simulation.ipynb` (which used
`ipywidgets.interact`) to MyST Markdown with
[marimo](https://marimo.io) snippets, so the page stays light: no stored
outputs, no JavaScript widget state in the HTML.

```{marimo-config}
:echo: true
```

```{marimo} python
import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
```

The error model is a pure function of its parameters (no widgets here):

```{marimo} python
def apply_calibration_errors(X_ideal, ideal_slope, ideal_intercept,
                             n_cycles, n_points_per_half_cycle,
                             zero_offset, sensitivity_error, linearity_error,
                             hysteresis_error, dead_band, resolution,
                             rng):
    """Generate cyclical data and apply the static errors. Returns X_sim, Y_sim, Y_ideal, is_ascending."""

    X_min = X_ideal.min()
    X_max = X_ideal.max()

    # One cycle: ascending then descending (endpoints not duplicated)
    x_asc = np.linspace(X_min, X_max, n_points_per_half_cycle)
    x_desc = np.linspace(X_max, X_min, n_points_per_half_cycle)
    x_cycle = np.concatenate([x_asc, x_desc[1:-1]])
    X_sim = np.tile(x_cycle, n_cycles)

    is_ascending = np.tile(
        np.concatenate([np.ones(len(x_asc), dtype=bool),
                        np.zeros(len(x_desc) - 2, dtype=bool)]),
        n_cycles,
    )

    # Start from the ideal response, then stack the errors
    Y_ideal = ideal_slope * X_sim + ideal_intercept
    Y_err = Y_ideal.copy()
    Y_err += zero_offset                                  # zero offset (bias)
    Y_err *= (1 + sensitivity_error / 100.0)              # sensitivity (gain)
    X_mid = (X_max + X_min) / 2
    Y_err += linearity_error * (X_sim - X_mid) ** 2       # linearity
    Y_err[is_ascending] += hysteresis_error / 2           # hysteresis
    Y_err[~is_ascending] -= hysteresis_error / 2
    dead_band_mask = (X_sim > -dead_band) & (X_sim < dead_band)
    Y_err[dead_band_mask] = ideal_intercept + zero_offset # dead band flat spot
    if resolution > 0:                                    # quantization
        Y_err = np.round(Y_err / resolution) * resolution

    Y_sim = Y_err + rng.normal(0, 0.1, len(Y_err))
    return X_sim, Y_sim, Y_ideal, is_ascending
```

Use the sliders to choose the acquisition settings and the error magnitudes:

```{marimo} python
cycles_slider = mo.ui.slider(start=1, stop=5, step=1, value=2, label="Cycles (N)")
points_slider = mo.ui.slider(start=10, stop=100, step=10, value=30, label="Points / half-cycle")
zero_slider = mo.ui.slider(start=-2.0, stop=2.0, step=0.1, value=0.0, label="Zero offset (bias)")
sens_slider = mo.ui.slider(start=-10.0, stop=10.0, step=1.0, value=0.0, label="Sensitivity error (%)")
lin_slider = mo.ui.slider(start=-0.05, stop=0.05, step=0.005, value=0.0, label="Linearity error (x² coeff)")
hyst_slider = mo.ui.slider(start=0.0, stop=1.0, step=0.1, value=0.0, label="Hysteresis error (mag)")
dead_slider = mo.ui.slider(start=0.0, stop=1.0, step=0.1, value=0.0, label="Dead band (input width)")
res_slider = mo.ui.slider(start=0.0, stop=0.5, step=0.05, value=0.0, label="Resolution (quantization)")

mo.vstack([
    mo.md("**Acquisition**"),
    cycles_slider, points_slider,
    mo.md("**Static errors**"),
    zero_slider, sens_slider, lin_slider,
    hyst_slider, dead_slider, res_slider,
])
```

Simulate, fit a straight line, and plot the residuals (orange arrows):

```{marimo} python
rng = np.random.default_rng(42)  # fixed seed: sliders change errors, not noise
X_ideal_range = np.array([-10.0, 10.0])

X_sim, Y_sim, Y_ideal, is_ascending = apply_calibration_errors(
    X_ideal_range, 1.0, 0.0,
    cycles_slider.value, points_slider.value,
    zero_slider.value, sens_slider.value, lin_slider.value,
    hyst_slider.value, dead_slider.value, res_slider.value,
    rng,
)

slope, intercept, r_value, p_value, std_err = linregress(X_sim, Y_sim)
Y_fit = slope * X_sim + intercept
calibration_error = Y_sim - Y_fit
max_abs_error = np.max(np.abs(calibration_error))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(X_sim[is_ascending], Y_sim[is_ascending], "o", color="blue",
        markersize=3, alpha=0.5, label="Simulated (increasing X)")
ax.plot(X_sim[~is_ascending], Y_sim[~is_ascending], "o", color="red",
        markersize=3, alpha=0.5, label="Simulated (decreasing X)")
ax.plot(X_sim, Y_fit, "-", color="black", linewidth=2,
        label=f"Best-fit: Y = {slope:.2f}X + {intercept:.2f}")
ax.plot(X_sim, Y_ideal, "--", color="gray", linewidth=1,
        label="Ideal: Y = 1.00X + 0.00")

arrow_skip = max(len(X_sim) // 20, 1)
for i in range(0, len(X_sim), arrow_skip):
    ax.annotate("", xy=(X_sim[i], Y_fit[i]), xytext=(X_sim[i], Y_sim[i]),
                arrowprops=dict(arrowstyle="->", color="darkorange", linewidth=1.5))

ax.set_title(f"Static calibration error simulation (R² = {r_value**2:.4f})")
ax.set_xlabel("Input (X)")
ax.set_ylabel("Output (Y)")
ax.legend(loc="upper left")
ax.set_xlim(X_ideal_range[0] - 1, X_ideal_range[1] + 1)
ax.set_ylim(X_ideal_range[0] - 3, X_ideal_range[1] + 3)

plt.close()
mo.vstack([
    fig,
    mo.md(f"**Key metrics** — max absolute residual: `{max_abs_error:.2f}`; "
          f"span (max Y − min Y): `{Y_sim.max() - Y_sim.min():.2f}`"),
])
```
