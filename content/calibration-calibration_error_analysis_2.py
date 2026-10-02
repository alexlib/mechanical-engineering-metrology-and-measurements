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
    # Hysteresis example

    Given calibration of an instrument for an increasing and decreasing input $x$ [mV] and output of the instrument $y$ [mV]
    """)
    return


@app.cell
def _():
    import numpy as np
    import pylab as pl

    return np, pl


@app.cell
def _():
    from IPython.core.display import Image 
    Image(filename='images/hysteresis_example.png')
    return (Image,)


@app.cell
def _(np):
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0])
    y = np.array([0.1, 1.1, 2.1, 3.0, 4.1, 5.0, 5.0, 4.2, 3.2, 2.2, 1.2, 0.2])
    return x, y


@app.cell
def _(pl, x, y):
    pl.plot(x,y,'o')
    pl.xlabel('$x$ [mV]')
    pl.ylabel('$y$ [mV]')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. We see the error, but we do not know if it is a random or not
    2. In order to see the hysteresis, we have to set the plot with the lines connecting points:
    """)
    return


@app.cell
def _(pl, x, y):
    pl.plot(x,y,'--o')
    pl.xlabel('$x$ [mV]')
    pl.ylabel('$y$ [mV]')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Estimate the hysteresis error:

    $e_h = y_{up} - y_{down}$

    $e_{h_{max}} = max(|e_h|)$

    $e_{h_{max}}\% = 100\% \cdot \frac{e_{h_{max}}}{y_{max}-y_{min}} $
    """)
    return


@app.cell
def _(np, y):
    e_h = y[:6]-np.flipud(y[6:]) 
    print(f"e_h = {e_h} [mV]")
    return (e_h,)


@app.cell
def _(e_h, np):
    e_hmax = np.max(np.abs(e_h))
    print("e_hmax= %3.2f %s" % (e_hmax,"[mV]"))
    return (e_hmax,)


@app.cell
def _(e_hmax, np, y):
    e_hmax_p = 100*e_hmax/(np.max(y) - np.min(y))
    print("Relative error = %3.2f%s FSO" % (e_hmax_p,"%"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sensitivity error example
    """)
    return


@app.cell
def _(Image):
    Image(filename='images/sensitivity_error_example.png')
    return


@app.cell
def _(np):
    x_1 = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0])
    y_1 = np.array([0.4, 1.0, 2.3, 6.9, 15.8, 36.4, 110.1, 253.2])
    return x_1, y_1


@app.cell
def _(pl, x_1, y_1):
    pl.plot(x_1, y_1, '--o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Calibration curve')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sensitivity, $K$ is:

    $ K_i  = \left( \frac{\partial y}{\partial x} \right)_{x_i} $
    """)
    return


@app.cell
def _(np, x_1, y_1):
    K = np.diff(y_1) / np.diff(x_1)
    print(f'K={K}')
    return (K,)


@app.cell
def _(K, pl, x_1):
    pl.plot(x_1[1:], K, '--o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$K$ [V/cm]')
    pl.title('Sensitivity')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead of working with non-linear curve of sensitivity we can use the usual trick: the logarithmic scale
    """)
    return


@app.cell
def _(pl, x_1, y_1):
    pl.loglog(x_1, y_1, '--o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Logarithmic scale')
    return


@app.cell
def _(np, pl, x_1, y_1):
    logK = np.diff(np.log(y_1)) / np.diff(np.log(x_1))
    print(f'$\\log(K)$ = {logK}')
    pl.plot(x_1[1:], logK, '--o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$K$ [V/cm]')
    pl.title('Logarithmic sensitivity')
    # pl.hold(True)
    pl.plot([x_1[1], x_1[-1]], [1.2, 1.2], 'r--')
    return


@app.cell
def _(pl, x_1, y_1):
    pl.loglog(x_1, y_1, 'o', x_1, x_1 ** 1.2)
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Logarithmic scale')
    pl.legend(('$y$', '$x^{1.2}$'), loc='best')
    return


@app.cell
def _(pl, x_1, y_1):
    pl.plot(x_1, y_1 - x_1 ** 1.2, 'o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y - y_c$ [V]')
    # pl.legend(('$y$','$x^{1.2}$'),loc='best')
    pl.title('Deviation plot')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Regression analysis
    Following the recipe of http://www.answermysearches.com/how-to-do-a-simple-linear-regression-in-python/124/
    """)
    return


@app.cell
def _(np):
    from scipy.stats import t
    def linreg(X, Y):
        """
        Summary
            Linear regression of y = ax + b
        Usage
            real, real, real = linreg(list, list)
        Returns coefficients to the regression line "y=ax+b" from x[] and y[], and R^2 Value
        """
        N = len(X)

        if N != len(Y):  raise(ValueError, 'unequal length')

        Sx = Sy = Sxx = Syy = Sxy = 0.0
        for x, y in zip(X, Y):
            Sx = Sx + x
            Sy = Sy + y
            Sxx = Sxx + x*x
            Syy = Syy + y*y
            Sxy = Sxy + x*y

        det =  Sx * Sx - Sxx * N # see the lecture

        a,b = (Sy * Sx - Sxy * N)/det, (Sx * Sxy - Sxx * Sy)/det

        meanerror = residual = residualx = 0.0

        for x, y in zip(X, Y):
            meanerror = meanerror + (y - Sy/N)**2
            residual = residual + (y - a * x - b)**2
            residualx = residualx + (x - Sx/N)**2

        RR = 1 - residual/meanerror
        # linear regression, a_0, a_1 => m = 1
        m = 1
        nu = N - (m+1)

        sxy = np.sqrt(residual / nu)

        # Var_a, Var_b = ss * N / det, ss * Sxx / det

        Sa = sxy * np.sqrt(1/residualx)
        Sb = sxy * np.sqrt(Sxx/(N*residualx))


        # We work with t-distribution, ()
        # t_{nu;\alpha/2} = t_{3,95} = 3.18
        tvalue = t.ppf(1-(1-0.95)/2, nu)

        print("Estimate: y = ax + b")
        print("N = %d" % N)
        print("Degrees of freedom $\\nu$ = %d " % nu)
        print("a = %.2f $\\pm$ %.3f" % (a, tvalue*Sa/np.sqrt(N)))
        print("b = %.2f $\\pm$ %.3f" % (b, tvalue*Sb/np.sqrt(N)))
        print("R^2 = %.3f" % RR)
        print("Syx = %.3f" % sxy)
        print("y = %.2f x + %.2f $\\pm$ %.3f V" % (a, b, tvalue*sxy/np.sqrt(N)))
        return a, b, RR, sxy

    return (linreg,)


@app.cell
def _(linreg, np, x_1, y_1):
    print(linreg(np.log(x_1), np.log(y_1)))
    return


@app.cell
def _(pl, x_1, y_1):
    pl.loglog(x_1, y_1, 'o', x_1, x_1 ** 1.21 - 0.0288)
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Logarithmic scale')
    pl.legend(('$y$', '$x^{1.2}$'), loc='best')
    return


@app.cell
def _(pl, x_1, y_1):
    pl.plot(x_1, y_1 - (x_1 ** 1.21 - 0.0288), 'o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y - y_c$ [V]')
    # pl.legend(('$y$','$x^{1.2}$'),loc='best')
    pl.title('Deviation plot')
    return


if __name__ == "__main__":
    app.run()
