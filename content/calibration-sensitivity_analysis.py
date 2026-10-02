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
    # Sensitivity estimate example
    """)
    return


@app.cell
def _():
    import pylab as pl
    from scipy.stats import t
    import numpy as np
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

    return linreg, np, pl


@app.cell
def _(np):
    x = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0])
    y = np.array([0.4, 1.0, 2.3, 6.9, 15.8, 36.4, 110.1, 253.2])
    return x, y


@app.cell
def _(pl, x, y):
    pl.plot(x,y,'--o')
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
def _(np, x, y):
    K = np.diff(y)/np.diff(x)
    print (K)
    return (K,)


@app.cell
def _(K, pl, x):
    pl.plot(x[1:],K,'--o')
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
def _(pl, x, y):
    pl.loglog(x,y,'--o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Logarithmic scale')
    return


@app.cell
def _(np, pl, x, y):
    logK = np.diff(np.log10(y))/np.diff(np.log10(x))
    print( logK)
    pl.plot(x[1:],logK,'--o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$K$ [V/cm]')
    pl.title('Logarithmic sensitivity')
    pl.plot([x[1],x[-1]],[1.2,1.2],'r--')
    return


@app.cell
def _(pl, x, y):
    pl.loglog(x,y,'o',x,x**(1.2))
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Logarithmic scale')
    pl.legend(('$y$','$x^{1.2}$'),loc='best')
    return


@app.cell
def _(pl, x, y):
    pl.plot(x,y-x**(1.2),'o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y - y_c$ [V]')
    pl.title('Deviation plot')
    # pl.legend(('$y$','$x^{1.2}$'),loc='best')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Regression analysis
    Following the recipe of http://www.answermysearches.com/how-to-do-a-simple-linear-regression-in-python/124/
    """)
    return


@app.cell
def _(linreg, np, x, y):
    print (linreg(np.log10(x),np.log10(y)))
    return


@app.cell
def _(pl, x, y):
    pl.loglog(x,y,'o',x,x**(1.21)-0.01252)
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y$ [V]')
    pl.title('Logarithmic scale')
    pl.legend(('$y$','$x^{1.2}$'),loc='best')
    return


@app.cell
def _(pl, x, y):
    pl.plot(x,y-(x**(1.21)-0.01252),'o')
    pl.xlabel('$x$ [cm]')
    pl.ylabel('$y - y_c$ [V]')
    pl.title('Deviation plot');
    # pl.legend(('$y$','$x^{1.2}$'),loc='best')
    return


if __name__ == "__main__":
    app.run()
