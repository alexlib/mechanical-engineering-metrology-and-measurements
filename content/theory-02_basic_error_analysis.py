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
    # Basic error analysis

    This part is the simplified error analysis that we will extend through the course with the more precise definitions
    and analysis using regressions, calibration, statistics, dynamics, etc.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Errors
    1. Systematic errors
    1. Random errors

    ### Systematic errors:
    1. equipment/tool precision error
    1. human error
    1. external environmental effects

    ### Random errors:
    1. tool precision (below the resolution)
    1. statistical errors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Accuracy vs precision

    Low systematic errors make a measurement *accurate* (centered on the true value).
    Low random errors make it *precise* (tightly grouped). You need both:

    ![Accuracy vs precision, random vs systematic error](../images/accuracy_vs_precision.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example:

    Digital voltemeter measures 10.32 kV, its precision is 0.01kV.

    However the equipment has a sticker with the
    statement of the basic calibrated errors and it says 1% of the measured value, i.e. 0.1kV for the given case.

    We use the maximum error contribution between the resolution and systematic error:

    $$ \Delta = max ( x_i ) = max(0.1, 0.01) = 0.1 [kV] $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Random errors are statistical errors

    We will study the basics of the statistical analysis (histograms, distributions, statistical tests) but for beginning
    we can use the simple terms.

    If we assume that the random errors are distributed randomly from the normal distribution (Gaussian distribution), then
    we can believe that the expected value $ x_0 $ and the deviations $ \sigma $ will describe well the distribution such
    that in 68% of cases our measured sample is within the range $(x_0 -\sigma, x_0 + \sigma)$. So we believe that our central value is the $x_0$ .

    Since we always measure only $N$ samples (finite number) we can at best estimate the arithmetic average $\overline{x}$ and standard deviation $S_x$ of the sample. So what we can measure is

    $$ x_0 \approx \overline{x} = \frac{1}{N} \sum\limits_{i=1}^{N} x_i $$

    $$S_x = \sqrt{\frac{\sum\limits_{i=1}^{N} \left( x_i - \overline{x} \right)^2}{N-1} } $$

    Note that the mean standard deviation is not sample standard deviation. It's also called standard uncertainty **type A**:

    $$u_A = \sigma \approx S_x/\sqrt{N}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Total error estimate

    If we can assume that only these two error sources are present, i.e. the equipment error $\Delta$ and the statistical,
    random error $\sigma/\sqrt{N}$, then we can estimate the total error using the root-of-sum-squares method (there are also other methods too): $$ \Delta(x) = \sqrt{\Delta^2 + \sigma/N^2 } $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example

    Use the linear scale to measure in [cm]:

        10.0, 10.0, 9.9, 10.1, 9.6, 9.9, 10.3, 10.1, 10.0

    precision of the scale is 0.1 cm

    We get in units of (cm):

    $$ \overline{x} = 9.99, \qquad S = 0.179\,$$

    Then the statistical analysis error is

    $$S/\sqrt{N} = 0.00566\ \mathrm{cm}$$

    And the total error estimate is (in cm):

    $$\Delta(x) = \sqrt{0.1^2 + 0.00566^2} = 0.1149\,$$

    and the output of the measurement is

    $$x = \left( 9.99 \pm 0.012 \right)\,$$

    note the use of the *significant digits* (we cannot report what we cannot know)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Use of measured values in estimating parameters

    Typically we use several measurements and use functions to combine them into parameters, i.e. $y = f(x_1, x_2)$

    Then if we measured $x$ with the error $\Delta_x$, how large would be the error of $\Delta(y)$?

    The answer is simple $$\Delta_y = \Delta(f) = \left|\frac{df}{dx}\right|\Delta_x$$

    if it's a function of several variables: $y = f(x_1,x_2)$, then: $$\Delta_y=\sqrt{\left(\frac{\partial f}{\partial x_1} \Delta x_1 \right)^2 + \left(\frac{\partial f}{\partial x_2} \Delta x_2 \right)^2}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example

    Volume of a cylinder is measured using the radius $r = 5.0 \pm 0.1$ cm and its height, $h = 1.30 \pm 0.1$ cm. The volume is estimated using $$V = \pi r^2 h $$

    Therefore we got $ V = 1020.98 $ cm$^3$ and the error is estimated according to the derivatives.

    $ \frac{\partial V}{\partial r} = 2 \pi r h$

    $ \frac{\partial V}{\partial h} = \pi r^2 $

    $\Delta(V) = \sqrt{(2\pi r \Delta r)^2 + (\pi r^2 \Delta h)^2}  = 41.58\,$ cm$^3$

    $ V = 1021.0 \pm 41.6 \,$ cm$^3$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note: if $x_1$ and $x_2$ are dependent, then

    $$\Delta_y=\left|\frac{\partial f}{\partial x_1} \Delta x_1 \right| + \left|\frac{\partial f}{\partial x_2} \Delta x_2 \right| $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note: $P$ and $B$ notation

    Some labs (e.g. Bluestein's Lab A) write Type A as *probability* $P$ (or $u_P$) and
    Type B as *bias* $B$ (or $u_B$). It is the same idea in shorter symbols:

    $$ u = \sqrt{B^2 + P^2} = \sqrt{u_B^2 + u_P^2} $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note: fewer than 30 readings — use Student $t$

    The factors above (68% for $1\sigma$, 1.96 for 95%) come from the normal distribution
    and hold for many readings ($m > 30$). With fewer readings, replace $z$ by Student $t$
    with $\nu = m - 1$ degrees of freedom:

    $$ u_y = (t_{1-c, \, \nu = m-1}/\sqrt{m}) \left[ \sum (y_j - \bar{y})^2/(m-1) \right]^{0.5} $$

    (See the Statistics chapter for the $t$-distribution and how to look up $t$.)
    """)
    return


if __name__ == "__main__":
    app.run()
