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
    # Outlier Detection: Modified Thompson Test, Second Version


    ## example of outlier test using modified Thompson technique
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import t

    import matplotlib as mpl
    mpl.rcParams['lines.linewidth']=2
    mpl.rcParams['lines.color']='r'
    mpl.rcParams['figure.figsize']=(8,6)
    mpl.rcParams['font.size']=14
    mpl.rcParams['axes.labelsize']=20
    return np, plt, t


@app.cell
def _(np, plt):
    x = np.array([28, 31, 27, 28, 29, 25, 29, 28, 18, 27])
    plt.plot(1+np.arange(len(x)),x,'o',markersize=10),
    plt.xlim([0,11])
    plt.xlabel('$n$')
    plt.ylabel('$T\; [^\circ C \,]$');
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### is there an outlier?
    Sort, look at the lowest and largest and plot to visualize
    """)
    return


@app.cell
def _(np, x):
    # Sort x
    x_1 = np.sort(x)
    print(x_1)
    return (x_1,)


@app.cell
def _(np, plt, x_1):
    plt.plot(np.arange(2, 10), x_1[1:-1], 'o', markersize=10)
    plt.plot(1, x_1[0], 'rs', markersize=10, linewidth=2)
    plt.plot(10, x_1[-1], 'rs', markersize=10)
    plt.xlim([0, 11])
    plt.xlabel('$\\hat{n}$')
    plt.ylabel('Sorted $T\\; [^\\circ C \\,]$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The sample mean and standard deviation, $\bar{x}$, $S_x$
    """)
    return


@app.cell
def _(np, x_1):
    meanx = np.mean(x_1)
    stdx = np.std(x_1, ddof=1)
    print('mean = %6.2f,  std = %6.2f' % (meanx, stdx))
    return meanx, stdx


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defivations for each suspicious point, take the largest $\delta_i = |x_i - \bar{x}|$
    """)
    return


@app.cell
def _(meanx, np, x_1):
    delta = np.abs(x_1 - meanx)
    # print ('suspicious points are with \\delta %.1f %.1f' % (delta[0],delta[-1]))
    print('suspicious point is:', x_1[np.argmax(delta)], 'deviation is = %.1f' % np.max(delta))
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
def _(delta, np, stdx, t, x_1):
    _n = len(x_1)
    _tv = t.isf(0.05 / 2, _n - 2)
    _tau = _tv * (_n - 1) / (np.sqrt(_n) * np.sqrt(_n - 2 + _tv ** 2))
    print('n = %d, t = %.2f, tau = %.2f' % (_n, _tv, _tau))
    print('compare: %.2f to %.2f ' % (np.max(delta), _tau * stdx))
    print('Is max() above $t_{\\nu,95}S$? %s ' % (np.max(delta) > _tau * stdx))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### So we remove the outlier and repeat the test (from the beginning)
    """)
    return


@app.cell
def _(np, t):
    x_2 = np.array([28, 31, 27, 28, 29, 25, 29, 28, 27])
    x_2 = np.sort(x_2)
    meanx_1 = np.mean(x_2)
    stdx_1 = np.std(x_2, ddof=1)
    delta_1 = np.abs(x_2 - meanx_1)
    print('suspicious point is:', x_2[np.argmax(delta_1)], 'deviation is = %.1f' % np.max(delta_1))
    _n = len(x_2)
    _tv = t.isf(0.05 / 2, _n - 2)
    _tau = _tv * (_n - 1) / (np.sqrt(_n) * np.sqrt(_n - 2 + _tv ** 2))
    print('n = %d, t = %.2f, tau = %.2f' % (_n, _tv, _tau))
    print('compare: %.2f to %.2f ' % (np.max(delta_1), _tau * stdx_1))
    print('Is max() above $t_{\\nu,95}S$? %s ' % (np.max(delta_1) > _tau * stdx_1))
    return


@app.cell
def _(np, t):
    x_3 = np.array([28, 31, 27, 28, 29, 29, 28, 27])
    x_3 = np.sort(x_3)
    (print('Sorted x:'), print(x_3))
    meanx_2 = np.mean(x_3)
    stdx_2 = np.std(x_3, ddof=1)
    delta_2 = np.abs(x_3 - meanx_2)
    print('suspicious point is:', x_3[np.argmax(delta_2)], 'deviation is = %.1f' % np.max(delta_2))
    _n = len(x_3)
    _tv = t.isf(0.05 / 2, _n - 2)
    _tau = _tv * (_n - 1) / (np.sqrt(_n) * np.sqrt(_n - 2 + _tv ** 2))
    print('n = %d, t = %.2f, tau = %.2f' % (_n, _tv, _tau))
    print('compare: %.2f to %.2f ' % (np.max(delta_2), _tau * stdx_2))
    print('Is max() above $t_{\\nu,95}S$? %s ' % (np.max(delta_2) > _tau * stdx_2))
    return


@app.cell
def _(np, t):
    x_4 = np.array([28, 27, 28, 29, 29, 28, 27])
    x_4 = np.sort(x_4)
    (print('Sorted x:'), print(x_4))
    meanx_3 = np.mean(x_4)
    stdx_3 = np.std(x_4, ddof=1)
    delta_3 = np.abs(x_4 - meanx_3)
    print('suspicious point is:', x_4[np.argmax(delta_3)], 'deviation is = %.1f' % np.max(delta_3))
    _n = len(x_4)
    _tv = t.isf(0.05 / 2, _n - 2)
    _tau = _tv * (_n - 1) / (np.sqrt(_n) * np.sqrt(_n - 2 + _tv ** 2))
    print('n = %d, t = %.2f, tau = %.2f' % (_n, _tv, _tau))
    print('compare: %.2f to %.2f ' % (np.max(delta_3), _tau * stdx_3))
    print('Is max() above $t_{\\nu,95}S$? %s ' % (np.max(delta_3) > _tau * stdx_3))
    return


if __name__ == "__main__":
    app.run()
