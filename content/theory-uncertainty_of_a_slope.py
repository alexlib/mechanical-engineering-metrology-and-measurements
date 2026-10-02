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
    # How to estimate the uncertainty of a slope for static calibration or regression
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    A calibration experiment gives you pairs of readings: you command an input `U`
    and the instrument reports `I`. Plotting `I` against `U` should give a straight
    line, and the **slope of that line is the sensitivity** of the instrument — the
    number you actually want, with an uncertainty attached.

    Here is one such series. We will do three things, in order:

    1. plot the measurements,
    2. attach error bars and fit a straight line,
    3. find the steepest and shallowest lines the data allow.
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    # Six calibration points: commanded voltage against reported current.
    U = np.array([4.5, 6.0, 7.0, 8.0, 9.0, 10.0])  # voltage, V
    I = np.array([109.5, 115.3, 129.2, 134.8, 142.1, 144.6])  # current, mA

    du = 0.15  # standard uncertainty of the voltage reading, V
    return I, U, du, np, plt


@app.cell
def _(I, U, mo, plt):
    mo.md(r"""
    ## 1. The measurements

    Six points. There is a clear upward trend, but they do not lie exactly on a
    line — that scatter is the measurement uncertainty we need to quantify.
    """)
    return


@app.cell
def _(I, U, mo, plt):
    fig1, ax1 = plt.subplots(figsize=(7, 4.5))
    ax1.plot(U, I, "o", markersize=7, color="tab:blue", label="measurements")
    ax1.set_xlabel("$U$ [V]")
    ax1.set_ylabel("$I$ [mA]")
    ax1.set_title("Calibration measurements")
    ax1.grid(alpha=0.3)
    ax1.legend()
    fig1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Error bars and a least-squares fit

    Each reading carries an uncertainty, drawn as an error bar. Drag the slider to
    change the standard uncertainty `u(I)` of the current measurement and watch the
    picture change.

    `np.polyfit(U, I, 1)` returns the least-squares slope and intercept, which is
    our best estimate $m$.
    """)
    return


@app.cell
def _(I, U, np):
    m_best, intercept = np.polyfit(U, I, 1)
    print(f"least-squares slope   m = {m_best:.2f} mA/V")
    print(f"intercept                 = {intercept:.1f} mA")
    return intercept, m_best


@app.cell
def _(mo, np):
    u_I = mo.ui.slider(
        start=1.0,
        stop=6.0,
        step=0.25,
        value=4.5,
        label="standard uncertainty of the current reading, u(I) [mA]",
    )
    u_I
    return (u_I,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. The steepest and shallowest acceptable lines

    Rather than trusting a formula, ask a geometric question: *what is the range of
    slopes for which some straight line still passes through every error bar?*

    The lines that just touch the error bars at one end give the two limits. Each
    one ignores most of the points — that is the point. Only the pair of points
    that binds the answer matters; the rest only have to be consistent.
    """)
    return


@app.cell
def _(I, U, du, np, u_I):
    def slope_limits(U, I, du, di):
        """Steepest and shallowest lines that cross every error bar.

        The line b + m*x crosses box i when it is above the bottom-right corner
        and below the top-left corner, i.e. for some b,

            (I_i - di) - m (U_i + du)  <=  b  <=  (I_i + di) - m (U_i - du)

        A b exists for all boxes only when every box is compatible with every
        other, which reduces to a bound on m per pair i, j:

            (I_i - di) - (I_j + di)  <=  m * [ (U_i + du) - (U_j - du) ]

        Taking the largest lower bound and the smallest upper bound over all
        pairs gives the interval of acceptable slopes. A box never constrains
        itself, so i == j is excluded.
        """
        n = len(U)
        i, j = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
        other = i != j
        gap = (U[i] + du) - (U[j] - du)
        rise = (I[i] - di) - (I[j] + di)
        safe = np.where(gap == 0, 1.0, gap)

        # gap > 0 forces m to be at least rise/gap; take the strongest such bound.
        m_lo = float(np.where(other & (gap > 0), rise / safe, -np.inf).max())
        # gap < 0 forces m to be at most rise/gap; take the strongest such bound.
        m_hi = float(np.where(other & (gap < 0), rise / safe, np.inf).min())

        feasible = m_lo <= m_hi
        return (m_lo, m_hi) if feasible else (np.nan, np.nan)

    def touching_intercept(U, I, du, di, m):
        """Largest intercept for which the line of slope m still crosses every bar."""
        return float(np.max((I - di) - m * (U + du)))

    m_min, m_max = slope_limits(U, I, du, u_I.value)
    feasible = np.isfinite(m_min) and np.isfinite(m_max)

    if feasible:
        b_min = touching_intercept(U, I, du, u_I.value, m_min)
        b_max = touching_intercept(U, I, du, u_I.value, m_max)
    else:
        b_min = b_max = np.nan

    return b_max, b_min, feasible, m_max, m_min


@app.cell
def _(
    I, U, b_max, b_min, du, feasible, intercept, m_best, m_max, m_min, plt, u_I,
):
    fig2, ax2 = plt.subplots(figsize=(7.5, 4.8))
    ax2.errorbar(
        U, I, xerr=du, yerr=u_I.value, fmt="o", markersize=7,
        capsize=4, color="tab:blue", label="measurements $\\pm u$",
    )

    if feasible:
        grid = np.linspace(U.min() - du, U.max() + du, 200)
        ax2.plot(grid, m_best * grid + intercept, "k-", lw=2,
                label=f"least squares, $m={m_best:.2f}$")
        ax2.plot(grid, m_min * grid + b_min, color="tab:green", ls="--", lw=2,
                label=f"shallowest, $m_{{\\min}}={m_min:.2f}$")
        ax2.plot(grid, m_max * grid + b_max, color="tab:red", ls="--", lw=2,
                label=f"steepest, $m_{{\\max}}={m_max:.2f}$")
    else:
        ax2.plot([], [], " ")
        ax2.text(
            0.5, 0.06,
            "no single line crosses every error bar\nat this uncertainty",
            transform=ax2.transAxes, ha="center", va="bottom",
            color="tab:red", fontsize=11, weight="bold",
        )

    ax2.set_xlabel("$U$ [V]")
    ax2.set_ylabel("$I$ [mA]")
    ax2.set_title(f"Slope uncertainty, $u(I)={u_I.value:.2f}$ mA")
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=9, loc="upper left")
    fig2
    return


@app.cell
def _(feasible, m_best, m_max, m_min, mo, u_I):
    if feasible:
        u_m = (m_max - m_min) / 2
        report = f"""
With $u(I) = {u_I.value:.2f}$ mA the acceptable slopes run from
$m_{{\\min}} = {m_min:.2f}$ to $m_{{\\max}} = {m_max:.2f}$ mA/V, so

$$\\Delta m = \\frac{{m_{{\\max}} - m_{{\\min}}}}{{2}} = {u_m:.2f}\\ \\text{{mA/V}}$$

and the slope is quoted as $m = {m_best:.1f} \\pm {u_m:.1f}$ mA/V.

Shrink the slider: below about 2.2 mA **no** straight line passes through every
error bar, which is the method correctly telling you that the uncertainty you
claimed is too small to explain your own scatter.
"""
    else:
        report = f"""
At $u(I) = {u_I.value:.2f}$ mA there is **no** straight line that passes through
every error bar — the points are more scattered than the quoted uncertainty
allows, so the slope is not bracketed at all. Widen the error bars until a line
fits.
"""
    mo.md(report)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Where the bound comes from

    Write the candidate line as $I = b + m\,U$. Reading $I$ at $U$ means
    interpolating within a rectangle of half-widths $d_U$ in voltage and $d_I$ in
    current. The line enters the rectangle at its left edge and leaves at its
    right edge, so it crosses that rectangle exactly when

    $$
    I_i - d_I \;\le\; b + m\,(U_i + d_U)
    \qquad\text{and}\qquad
    b + m\,(U_i - d_U) \;\le\; I_i + d_I ,
    $$

    that is, when some intercept $b$ satisfies

    $$
    (I_i - d_I) - m\,(U_i + d_U) \;\le\; b \;\le\; (I_i + d_I) - m\,(U_i - d_U).
    $$

    A single line must satisfy this for *every* point at once, so the best any
    intercept can do must sit above every lower bound and below every upper bound.
    Pairing a lower bound from point $i$ with an upper bound from point $j$ gives

    $$
    (I_i - d_I) - (I_j + d_I) \;\le\; m\,\big[(U_i + d_U) - (U_j - d_U)\big].
    $$

    When the bracket is positive this is a **lower** bound on the slope; when it is
    negative it is an **upper** bound. Collecting every pair and keeping the
    strongest of each kind,

    $$
    m_{\min} = \max_{i \ne j} \frac{(I_i - d_I) - (I_j + d_I)}{(U_i + d_U) - (U_j - d_U)},
    \qquad
    m_{\max} = \min_{i \ne j} \frac{(I_i - d_I) - (I_j + d_I)}{(U_i + d_U) - (U_j - d_U)}
    $$

    over the pairs where the denominator has the required sign. A pair $i = j$ is
    excluded, since a box never constrains itself.

    Note which points survive. Only the pair that produces the largest lower bound
    actually sets $m_{\min}$, and only the pair producing the smallest upper bound
    sets $m_{\max}$ — every other point merely has to stay consistent. *That* is
    the "ignore some of the points" step: the extreme slopes are pinned down by two
    readings, not by a fit to all six.

    ## Reporting

    The interval is not a statistical confidence interval, so it is quoted as a
    half-width rather than as a standard uncertainty, and with the correct number
    of significant figures:

    $$
    m = m_{\text{best}} \pm \frac{m_{\max} - m_{\min}}{2},
    $$

    both terms rounded to the same decimal place — $7.3 \pm 1.9$ mA/V, not
    $7.28 \pm 1.874$ mA/V.

    ## Two cautions

    - This construction assumes a single line really is the right model. If the
      scatter is *curved* rather than random, no line will cross every error bar
      at any width, and you have found a hysteresis or a nonlinearity instead of
      an uncertainty.
    - The bound widens as the error bars grow, so quoting an uncertainty makes the
      method agree with it. Judge it against a second, independent method — a
      weighted least-squares fit with its own residual estimate, or a Monte Carlo
      propagation.
    """)
    return


if __name__ == "__main__":
    app.run()
