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
    # LVDT Calibration Curve and Its Uncertainty
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## LVDT example

    Use of static calibration curve and estimate of uncertainty.

    1. Measure several (at least 3) calibration points and fit a regression line to the calibration curve.
    2. Linear calibration curves are desirable because they result in the best accuracy and precision. If the data is non-linear, try logarithmic approach
    3. A plot of the calibration data and the fitted line should always be examined to check for outliers and to verify linear behavior.

    In this example we use the residuals to calculate standard errors of the point estimates. The assumption is that the noise is uniform and random and it's not always a valid one.

    ### Example 2: LVDT calibration

    Linear variable differential transformer (LVDT) is used to measure position and . The Linear Variable Differential Transformer is a position-sensing device that provides an AC output voltage proportional to the displacement of its core passing through its windings. LVDTs provide linear output for small displacements where the core remains within the primary coils. The exact distance is a function of the geometry of the LVDT.

    <img src ="http://www.ni.com/cms/images/devzone/tut/a/f841fe69729.gif">
    From: NI reference <http://www.ni.com/white-paper/3638/en>

    Principle:

    The LVDT will allow use to see the changing in voltage due to deflection. We will be able to find the change in AC voltage with the use of an oscilloscope. We will find several data point and plot them. From these points, we should be able to find a slope witch will be sensitivity of the LVDT. From this we can determine the voltage based on displacement or vise versa. After finding the sensitivity equation, we are able to calculate the experimental output voltage. We substitute the input, displacement in to our sensitivity equation and find the output voltage.

    The system is set up. We set the five-kilohertz oscillator to give one and a half volts for peak-to-peak. The beam is moved from minimum to maximum and a sketch of the output form the oscilloscope is drawn. The beam is set to minimum and peak-to-peak voltage is taken. The beam is moved one millimeter and voltage is taken again. This is done for fifteen reading. We will then find the residual voltage or the minimum output voltage.

    Finally, we plot our data on a graph and find the sensitivity with the slop equation. We then can find and graph our percent error over the entire distance.
    """)
    return
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # LVDT Calibration Curve and Its Uncertainty
    """)
    return




@app.cell
def _():
    import matplotlib.pyplot as plt
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

    return linreg, np, plt


@app.cell
def _():
    # Peak-Peak Voltage (mV)
    V = [98.8, 86.0, 74.0, 61.2, 47.2, 32.8, 20.4, 5.2, 8.4, 21.2, 35.2, 49.2, 63.2, 75.2, 88.4, 100.8]
    # Displacement
    x  = range(0,16)
    # (mm)
    # % Error
    err = [1, 0, -3, -5, -7, -8, -21, -57, 3, 4, 0, -1, -2, 0, 0, 1]
    return V, err, x


@app.cell
def _(V, plt, x):
    plt.plot(x,V,'--o')
    plt.xlabel('$x$ [mm]')
    plt.ylabel('$V$ [V]')
    return


@app.cell
def _(err, plt, x):
    plt.plot(x, err,'--o')
    plt.xlabel('$x$ [mm]')
    plt.ylabel('$error$ [%]')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## DC type of LVDT

    The LVDT will allow use to see the changing in voltage due to deflection. We will
    be able to find the change in DC voltage with the use of a multi-meter. We will find several
    data point and plot them. From these points, we should be able to find a slope witch will be
    sensitivity of the LVDT. From this we can determine the voltage based on displacement or
    vise versa. After finding the sensitivity equation, we are able to calculate the experimental
    output voltage.
    """)
    return


@app.cell
def _():
    # Peak-Peak Votage (mV)
    V_1 = [0.013, 0.997, 1.992, 2.997, 3.247, 3.499, 3.75, 4.0, 4.251, 4.5, 4.753, 5.003, 5.254, 5.56, 5.75, 6.01, 7.076]
    # Displacement (mm)
    x_1 = [0.0, 0.1, 0.2, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.56, 0.575, 0.6, 0.7]
    # % Error
    err_1 = [-23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1]
    return V_1, err_1, x_1


@app.cell
def _(V_1, plt, x_1):
    plt.plot(x_1, V_1, '--o')
    plt.xlabel('$x$ [mm]')
    plt.ylabel('$V$ [V]')
    return


@app.cell
def _(err_1, plt, x_1):
    plt.plot(x_1, err_1, '--o')
    plt.xlabel('$x$ [mm]')
    plt.ylabel('$error$ [%]')
    return


@app.cell
def _(V_1, linreg, x_1):
    K, b, RR, sxy = linreg(x_1, V_1)
    # a, b, RR, sxy
    print(K, b, RR)
    return K, b


@app.cell
def _(K, V_1, b, np, plt, x_1):
    V_est = np.array(x_1) * K + b
    plt.plot(x_1, V_1, 'o', x_1, V_est)
    plt.xlabel('$x$ [mm]')
    plt.ylabel('$V$ [mV]')
    # plt.legend(('$x$','$c^{0.047}$'),loc='best')
    plt.title('best fit')
    return


if __name__ == "__main__":
    app.run()
