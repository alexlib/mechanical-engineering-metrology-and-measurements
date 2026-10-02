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
    # Outliers

    ## example of outlier test using modified Thompson technique
    """)
    return


@app.cell
def _():
    from pylab import arange, argmax, array, np, plot, sqrt, xlabel, xlim, ylabel
    import matplotlib as mpl
    mpl.rcParams['lines.linewidth']=2
    mpl.rcParams['lines.color']='r'
    mpl.rcParams['figure.figsize']=(8,6)
    mpl.rcParams['font.size']=14
    mpl.rcParams['axes.labelsize']=20
    return arange, argmax, array, np, plot, sqrt, xlabel, xlim, ylabel


@app.cell
def _(arange, array, plot, xlabel, xlim, ylabel):
    x = array([48.9, 49.2, 49.2, 49.3, 49.3, 49.8, 49.9, 50.1, 50.2, 50.7])
    plot(arange(1,11),x,'o'),xlim([0,11]),xlabel('$n$'),ylabel('$T\; [^\circ C \,]$');
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### is there an outlier?
    Sort, look at the lowest and largest and plot to visualize
    """)
    return


@app.cell
def _(arange, plot, x, xlabel, xlim, ylabel):
    plot(arange(2,10),x[1:-1],'o'), plot(1,x[0],'rs',markersize=10,linewidth=2),plot(10,x[-1],'gs',markersize=10)
    xlim([0,11])
    xlabel('$\hat{n}$'),ylabel('Sorted $T\; [^\circ C \,]$');
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The sample mean and standard deviation, $\bar{x}$, $S_x$
    """)
    return


@app.cell
def _(np, x):
    meanx = np.mean(x)
    stdx = np.std(x,ddof=1)
    print('mean = %6.2f,  std = %6.2f' % (meanx,stdx))
    return meanx, stdx


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defivations for each suspicious point, take the largest $\delta_i = |x_i - \bar{x}|$
    """)
    return


@app.cell
def _(argmax, meanx, x):
    delta = abs(x - meanx)
    print ('suspicious points are first and last:')
    print ('%4.3f %4.3f' % (delta[0],delta[-1]))
    print ('suspicious point is:',  argmax(delta), 'deviation is = %4.3f' % max(delta))
    return (delta,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modified Thompson technique, $\tau$

    Define the confidence level (95%), therefore $\alpha = 5\%$. Because we deal with outliers, the DOF is smaller:

    $$ \tau = \frac{t_{\alpha/2} (n-1)}{\sqrt{n} \sqrt{n-2+t_{\alpha/2}^2}}, \qquad \alpha = 0.05, \quad df = n - 2 $$

    if:

    $$\delta_i  > \tau S$$

    then the point is an **outlier**

    remove it, estimate **new** $\bar{x}, S, \delta_i$ and **repeat** the test. until there is no outlier in the set.
    """)
    return


@app.cell
def _(delta, sqrt, stdx, x):
    from scipy.stats import t
    _n = len(x)
    _tv = t.isf(0.05 / 2, _n - 2)
    _tau = _tv * (_n - 1) / (sqrt(_n) * sqrt(_n - 2 + _tv ** 2))
    print('n = %d, t = %6.4f, tau = %6.4f' % (_n, _tv, _tau))
    print('compare: %6.3f vs. %6.3f ' % (max(delta), _tau * stdx))
    print('Is max() above $t_{\\nu,95}S$? %s ' % (max(delta) > _tau * stdx))
    return (t,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### So we remove the outlier and repeat the test (from the beginning)
    """)
    return


@app.cell
def _(argmax, np, sqrt, t, x):
    xnew = x[:-1].copy()
    meanx_1 = np.mean(xnew)
    stdx_1 = np.std(xnew, ddof=1)
    print('x: ', xnew)
    print('mean = %6.2f,  std = %6.2f\n' % (meanx_1, stdx_1))
    delta_1 = abs(xnew - meanx_1)
    print('deviations: ', delta_1)
    print('\n')
    print('suspicious point is: %f, its deviation is = %f \n' % (argmax(delta_1), max(delta_1)))
    _n = len(xnew)
    _tv = t.isf(0.05 / 2, _n - 2)
    _tau = _tv * (_n - 1) / (sqrt(_n) * sqrt(_n - 2 + _tv ** 2))
    print('n = %d, t = %6.4f, tau = %6.4f\n' % (_n, _tv, _tau))
    print('compare: %6.3f vs. %6.3f \n' % (max(delta_1), _tau * stdx_1))
    print('Is it outlier? :', max(delta_1) > _tau * stdx_1)
    return


if __name__ == "__main__":
    app.run()
