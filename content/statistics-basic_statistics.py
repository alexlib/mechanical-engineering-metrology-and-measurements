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
    # Very basic review of some statistics terms

    **Engineering Testing and Measurements**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Review of _basic statistics_

    1. Population -- the entire collection of measurements, not all of
    which will be analyzed statistically. Some variable $ x$, anything
    that is measurable, such as a length, time, voltage, current, resistance,
    etc.

    2. Sample -- a subset of the population that is analyzed statistically.
    A sample consists of  $n$ measurements: $x_1,x_2, x_3,...,x_n$

    3. Statistic -- a numerical attribute of the sample (e.g., mean,
    median, standard deviation).

    4. Population mean is denoted as:  $\mu$

    5. Sample mean is an arithmetic average:

    $$
    x_{\mathrm{avg}}=\overline{x}=\frac{1}{n}\sum_{i=1}^{n}x_{i}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Deviations

    *  Deviation is the difference between a particular measurement and the
    mean, $ d = x_i - \overline{x} $

    *  Deviation of one particular measurement is the same as the **precision
    error**  or **random error**  of that measurement.

    *  Deviation is **not**  the same as **inaccuracy -**  difference between a particular measurement and the **true value**

    *  Because of bias (systematic) error, $ x_{true}$ is often not even
    known, and the mean is not equal to $x_{true}$ as there are bias errors.

    * Average deviation -- averaging all the deviations is zero, $ \overline{d} = 0$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    plainSample standard deviation
    * **Average absolute deviation**  -- a better measure of deviation
    is the average absolute deviation (also called the average positive
    error), defined as the average of the absolute value of each deviation.
    $$
    \left|\overline{d}\right|=\frac{1}{n}\sum_{i=1}^{n}\left|d_{i}\right|$$

    * **Sample standard deviation**  -- measure of how much deviation
    or scatter is in the data is obtained by calculating the sample standard
    deviation. For \$ n measurements:
    $$
    S=\sqrt{\frac{\sum_{i=1}^{n}d_{i}^{2}}{n-1}}=\sqrt{\frac{\sum_{i=1}^{n}(x_{i}-\overline{x})^{2}}{n-1}}$$
    \par
    * **Notice the use of:** $n - 1$, it means we have only $n-1$ degrees of freedom as one degree is taken by the $\overline{x}$
    """)
    return


if __name__ == "__main__":
    app.run()
