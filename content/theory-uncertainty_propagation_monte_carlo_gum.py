import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Propagating uncertainty using Monte-Carlo simulations

    The analytical law of propagation (RSS with sensitivity coefficients) has three limits:

    1. It is exact only for **linear** measurement functions.
    2. It assumes the output is **normally distributed**.
    3. Complex models invite algebra mistakes when combining terms.

    Monte-Carlo (MC) propagation skips the algebra: draw many random input sets from their
    distributions, push each through $y = f(x)$, and read the output distribution directly —
    mean, standard deviation, and any coverage interval.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interactive: what does $y = a + b$ look like?

    Even the simplest sum produces different output shapes depending on the inputs.
    Drag the slider through the 6 cases ($10^6$ trials each, seed 42):

    1. normal + normal, equal size → normal output
    2. normal + wider normal → still normal, wider
    3. uniform + uniform, equal size → triangular output
    4. uniform + wider uniform → complex (trapezoidal) output
    5. normal + uniform → complex output, hard to predict
    6. normal + wider uniform → complex output
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mc_case = mo.ui.slider(
        start=1, stop=6, step=1, value=3,
        label="Input combination case (y = a + b)",
    )
    mc_case
    return (mc_case,)


@app.cell(hide_code=True)
def _(mc_case, mo, np, plt):
    _n = 1_000_000
    _rng = np.random.default_rng(42)
    _c = int(mc_case.value)
    if _c == 1:
        _a = _rng.normal(0, 1, _n); _b = _rng.normal(0, 1, _n)
    elif _c == 2:
        _a = _rng.normal(0, 1, _n); _b = _rng.normal(0, 2, _n)
    elif _c == 3:
        _a = _rng.uniform(-np.sqrt(3), np.sqrt(3), _n); _b = _rng.uniform(-np.sqrt(3), np.sqrt(3), _n)
    elif _c == 4:
        _a = _rng.uniform(-np.sqrt(3), np.sqrt(3), _n); _b = _rng.uniform(-2 * np.sqrt(3), 2 * np.sqrt(3), _n)
    elif _c == 5:
        _a = _rng.normal(0, 1, _n); _b = _rng.uniform(-np.sqrt(3), np.sqrt(3), _n)
    else:
        _a = _rng.normal(0, 1, _n); _b = _rng.uniform(-2 * np.sqrt(3), 2 * np.sqrt(3), _n)
    _y = _a + _b

    _fig, _ax = plt.subplots(figsize=(6.4, 4.1))
    _ax.hist(_y, bins=120, density=True, alpha=0.7, color="steelblue")
    _ax.set_xlabel("Standardized $y = a + b$")
    _ax.set_ylabel("Density")
    _ax.set_title(f"Case {_c}: output of a sum need not be normal")
    _ax.grid(alpha=0.3)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How simulation works

    1. Define the measurement function $y = f(x)$, with $x$ a vector of influence quantities.
    2. Draw $m$ random input sets from each input's distribution (normal, rectangular, …).
    3. Push every set through $f$: $Y = f(X)$.
    4. Read the output: mean, standard deviation, and percentiles for the coverage interval
       (e.g. 2.5th/97.5th for 95%).

    ## Example 1: non-linear propagation — cube volume $V = h^3$
    """)
    return


@app.cell
def _(np, plt):
    def monte_carlo_cube_volume(measurements, resolution, num_simulations=100000):
        # Calculate mean and standard deviation of measurements
        mean_height = np.mean(measurements)
        std_height = np.std(measurements, ddof=1)

        # Type B uncertainty (assuming rectangular distribution for resolution)
        u_b = resolution / np.sqrt(3)

        # Combine Type A and Type B uncertainties
        u_c = np.sqrt((std_height / np.sqrt(len(measurements)))**2 + u_b**2)

        # Generate Monte Carlo simulations
        simulated_heights = np.random.normal(mean_height, u_c, num_simulations)

        # Calculate volumes
        simulated_volumes = simulated_heights**3

        # Calculate results
        mean_volume = np.mean(simulated_volumes)
        std_volume = np.std(simulated_volumes)

        # Calculate coverage interval (95%)
        coverage_interval = np.percentile(simulated_volumes, [2.5, 97.5])

        print(f"Mean height: {mean_height:.6f}")
        print(f"Combined standard uncertainty of height: {u_c:.6f}")
        print(f"Mean volume: {mean_volume:.6f}")
        print(f"Standard uncertainty of volume: {std_volume:.6f}")
        print(f"95% coverage interval for volume: [{coverage_interval[0]:.6f}, {coverage_interval[1]:.6f}]")

        # Plot histogram of simulated volumes
        plt.figure(figsize=(6.4, 4.1))
        plt.hist(simulated_volumes, bins=100, density=True, alpha=0.7, color='skyblue')
        plt.axvline(mean_volume, color='red', linestyle='dashed', linewidth=2, label='Mean Volume')
        plt.axvline(coverage_interval[0], color='green', linestyle='dashed', linewidth=2, label='95% Coverage Interval')
        plt.axvline(coverage_interval[1], color='green', linestyle='dashed', linewidth=2)
        plt.xlabel('Volume')
        plt.ylabel('Probability Density')
        plt.title('Distribution of Cube Volumes (Monte Carlo Simulation)')
        plt.legend()
        plt.show()

    return (monte_carlo_cube_volume,)


@app.cell
def _(monte_carlo_cube_volume):
    # Example usage
    height_measurements = [10.02, 10.03, 10.01, 10.02, 10.03, 10.02, 10.01, 10.02, 10.03, 10.02]
    resolution = 0.01  # mm
    monte_carlo_cube_volume(height_measurements, resolution)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Example 2: thermal expansion — where first-order theory falls short

    Measurement model: $\Delta L = L \cdot \Delta T \cdot \alpha$.

    First-order propagation gives
    $u^2(\Delta L) = (\Delta T\alpha)^2u^2(L) + (L\alpha)^2u^2(\Delta T) + (L\Delta T)^2u^2(\alpha)$,
    but the exact expansion adds higher-order products such as
    $\Delta T\,u^2(L)u^2(\alpha)$ and $u^2(\Delta T)u^2(L)u^2(\alpha)$.
    A $10^6$-trial simulation of $(L, \Delta T, \alpha)$ needs none of that algebra and
    stays correct where the first-order approximation drifts — especially at 99.9%
    coverage, where the simulated range runs almost twice the first-order prediction.

    ## Example 3: cosine error — a non-normal output

    A 200 mm length measured with 2 µm length uncertainty and 1° alignment uncertainty
    produces a visibly non-normal output distribution. Theory and simulation agree on the
    standard uncertainty but disagree on the confidence limits — and the gap grows with
    the confidence level. This is exactly the case simulation exists for.

    ## Example 4: real data — density from caliper, micrometer, and balance

    Diameter (caliper, res 0.01 mm), height (micrometer, res 0.001 mm), and mass
    (balance, $u = 0.1$ g) combine into density. Analytical relative propagation and a
    5000-trial MC of the mean density agree — run both and compare.
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt, stats):
    from scipy.stats import norm

    res_caliper = 0.01     # mm
    res_micrometer = 0.001  # mm
    dm = 0.1               # g
    d = np.array([14.5, 14.4, 14.6, 14.5, 14.4, 14.5])
    h = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.6])
    m = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.1])

    vol_cm3 = (np.pi * d**2 / 4.0 * h) * 1e-3
    densities = m / vol_cm3
    rel_V = np.sqrt((2 * res_caliper / d)**2 + (res_micrometer / h)**2)
    sigma_D = densities * np.sqrt((dm / m)**2 + rel_V**2)

    rng = np.random.default_rng(0)
    sims = np.mean(
        rng.normal(m, dm, (5000, 6))
        / ((np.pi * rng.normal(d, res_caliper, (5000, 6))**2 / 4.0
            * rng.normal(h, res_micrometer, (5000, 6))) * 1e-3),
        axis=1,
    )
    D_mean, D_std = float(np.mean(sims)), float(np.std(sims, ddof=1))

    fig, ax = plt.subplots(figsize=(6.4, 4.1))
    ax.hist(sims, bins=40, density=True, alpha=0.6, label="MC mean density")
    _x = np.linspace(D_mean - 4 * D_std, D_mean + 4 * D_std, 300)
    ax.plot(_x, norm.pdf(_x, D_mean, D_std), "k--", label="Normal fit")
    ax.axvline(D_mean, color="k", linestyle="--", linewidth=1)
    ax.set_xlabel("Mean density (g/cm³)")
    ax.set_ylabel("Probability density")
    ax.legend()
    print(f"Mean density = {D_mean:.4f} ± {D_std:.4f} g/cm^3 (1σ, MC of the mean)")
    fig.tight_layout()
    fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Best practices for simulation

    1. **Trials:** use at least $10^6$ trials; more for high confidence levels; check
       convergence by increasing the count.
    2. **Distributions:** match actual measurement conditions and document every assumption.
    3. **Validation:** compare against the analytical result where one exists, and check
       sensitivity to input parameters.
    4. **Documentation:** record trial count, distributions, and confidence level with the result.
    """)
    return


if __name__ == "__main__":
    app.run()
