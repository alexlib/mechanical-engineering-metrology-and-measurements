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
    # Hysteresis and regression analysis example

    Given a calibration of an instrument for an increasing and decreasing input $q_i$ [kPa] and output of the instrument $q_o$ [kPa]
    """)
    return


@app.cell
def _():
    import pylab
    from scipy.stats import t
    import numpy as np
    from pylab import array, figure, grid, legend, plot, r_, size, title, xlabel, ylabel
    pylab.rcParams['figure.figsize'] = 10, 8 
    pylab.rcParams['font.size'] = 16
    return (
        array,
        figure,
        grid,
        legend,
        np,
        plot,
        r_,
        size,
        t,
        title,
        xlabel,
        ylabel,
    )


@app.cell
def _():
    from IPython.core.display import Image 
    Image(filename='images/pressure_calibration_example.png',width=400)
    return


@app.cell
def _(array):
    # increasing
    xi = array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
    yi = array([-1.12, 0.21, 1.18, 2.09, 3.33, 4.50, 5.26, 6.59, 7.73, 8.68, 9.80])
    # decreasing
    xd = xi.copy()
    yd = array([-0.69, 0.42, 1.65, 2.48, 3.62, 4.71, 5.87, 6.89, 7.92, 9.10, 10.20])
    return xd, xi, yd, yi


@app.cell
def _(figure, grid, legend, plot, xd, xi, xlabel, yd, yi, ylabel):
    figure()
    plot(xi,yi,'r:o',xd,yd,'b:s')
    grid('on')
    xlabel('True $P$ [kPa]')
    ylabel('Measured $P$ [kPa]')
    legend(('increasing','decreasing'))
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
def _(yd, yi):
    e_h = yi-yd 
    print("e_h =", e_h,"[kPa]")
    return (e_h,)


@app.cell
def _(e_h, np):
    e_hmax = np.max(np.abs(e_h))
    print("e_hmax= %3.2f %s" % (e_hmax,"[kPa]"))
    return (e_hmax,)


@app.cell
def _(e_hmax, np, xd, xi):
    e_hmax_p = 100*e_hmax/(np.max(xi) - np.min(xd))
    print("Relative error = %3.2f%s FSO" % (e_hmax_p,"%"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Regression analysis
    Following the recipe of http://www.answermysearches.com/how-to-do-a-simple-linear-regression-in-python/124/
    """)
    return


@app.cell
def _(np, t):
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
def _(linreg, xd, xi, yd, yi):
    print("Increasing")
    ai,bi,Ri,sxyi = linreg(xi,yi)
    print(ai,bi,Ri)
    print("Decreasing")
    ad,bd,Rd,sxd = linreg(xd,yd)
    print(ad,bd,Rd)
    return ad, ai, bd, bi


@app.cell
def _(
    ad,
    ai,
    bd,
    bi,
    figure,
    legend,
    linreg,
    plot,
    r_,
    title,
    xd,
    xi,
    xlabel,
    yd,
    yi,
    ylabel,
):
    figure()
    plot(xi,yi,'ro',xi,xi*ai+bi,'r--',xd,yd,'bs',xd,xd*ad+bd,'b--')
    xlabel('$P_{true}$ [kPa]')
    ylabel('$P_{meas}$ [kPa]')
    title('Regression')
    leg1 = '%3.2f $x$ %3.2f' % (ai,bi)
    leg2 = '%3.2f $x$ %3.2f' % (ad,bd)
    legend(('incr.',leg1,'decr.',leg2),loc='best')

    # all all together:
    a,b,R,_ = linreg(r_[xi,xd],r_[yi,yd])
    plot(xi,xi*a+b,'k-',lw=2)
    leg3 = '$q_o$ = %3.2f $q_i$ %3.2f' % (a,b)
    legend(('incr.',leg1,'decr.',leg2,leg3),loc='best')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$q_0 = m q_i + b$$

    $$q_0 = 1.8 q_i - 0.85$$

    $$\sigma_m^2 = \frac{N \sigma_{q_0}^2}{N\sum q_i^2 - \left(\sum q_i \right)^2}$$

    $$\sigma_b^2 = \frac{\sigma_{q_0}^2\sum q_i^2}{N\sum q_i^2 - \left(\sum q_i \right)^2}$$

    $$\sigma_{q_0}^2 = \frac{1}{N}\sum\left(m\,q_i + b - q_0 \right)^2 $$

    $$\sigma_{q_i}^2 = \frac{1}{N}\sum\left( \frac{q_0 - b}{m} - q_i \right)^2 = \frac{\sigma_{q_0}^2}{m^2} $$
    """)
    return


@app.cell
def _(linreg, size):
    def regression_analysis(qi,qo):
        m,b,R,syx = linreg(qi,qo)
        # print 'qo = %3.2f qi %3.2f' % (m,b)
        N = size(qi)
        d = m*qi + b - qo # deviation
        Sqo = sum(d**2)/N
        Sqi = Sqo/m**2
        Sm = N*Sqo/(N*sum(qi**2) - sum(qi)**2)
        Sb = Sqo*sum(qi**2)/(N*sum(qi**2) - sum(qi)**2)
        return Sm,Sb,Sqi,Sqo

    return (regression_analysis,)


@app.cell
def _(r_, regression_analysis, xd, xi, yd, yi):
    qi = r_[xi,xd]
    qo = r_[yi,yd]

    Sm,Sb,Sqi,Sqo = regression_analysis(qi,qo)
    print('Sm, Sb, Sqi, Sqo = ')
    print('%6.4f, %6.4f %6.4f %6.4f' % (Sm,Sb,Sqi,Sqo))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Taking $3 \sigma$ for $99.7\%$ certainty level:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $m = 1.08 \pm 0.0006$

    $b = -0.85 \pm 0.018$

    When we use calibration curve for the measurement:

    $q_i = (q_o + 0.85)/1.08 = 0.9233 q_0 + 0.785$

    $S_{q_i}^2 = 0.034$

    If we measured for instance 4.32 kPa, we transfer it to 4.79 kPa and write:

    (4.32*0.85)/1.08 = 4.787

    ### The final result is
    $P = 4.79 \pm 0.102$ kPa (99.7\%)
    """)
    return


if __name__ == "__main__":
    app.run()
