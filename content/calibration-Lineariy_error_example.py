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
    # Linearity error example
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as pl

    pl.rcParams['figure.figsize'] = 10, 8 
    pl.rcParams['font.size'] = 18
    return np, pl


@app.cell
def _(np):
    x = np.r_[np.linspace(20,220,10), np.linspace(180,0,9)]
    y = np.array([20,40,59,77,97,117,137,156,175,195,176,156,136,117,97,78,58,39,20])
    return x, y


@app.cell
def _(x, y):
    print(f'x = {x}')
    print(f'y = {y}')
    return


@app.cell
def _(pl, x, y):
    pl.plot(x,y,'--o')
    pl.xlabel(r'$x$')
    pl.ylabel(r'$y$')
    return


@app.cell
def _(np, x, y):
    # create best fit
    p = np.polyfit(x,y,1)
    print (p)
    y_fit = np.polyval(p,x)
    return (y_fit,)


@app.cell
def _(pl, x, y, y_fit):
    pl.plot(x,y,'ro',x,y_fit,'b--')
    pl.xlabel(r'$x$')
    pl.ylabel(r'$y$')
    pl.legend(('data','fit'),loc='best')
    return


@app.cell
def _(y, y_fit):
    print (f'measured y = {y}')
    print (f'estimated y = {y_fit}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Linearity error
    $\epsilon_L = |y_L - y|$

    $\epsilon_{L_{max}} = max(\epsilon_L)$

    $r_0 = y_{max} - y_{min}$

    $\% \epsilon_{L_{max}} = \frac{\epsilon_{L_{max}}}{r_0}\times 100$
    """)
    return


@app.cell
def _(y, y_fit):
    epsilon_L = abs(y - y_fit)
    epsilon_L_max = max(epsilon_L)
    r0 = max(y) - min(y)
    percent_epsilon_L_max = epsilon_L_max/r0 * 100.
    return epsilon_L, epsilon_L_max, percent_epsilon_L_max, r0


@app.cell
def _(epsilon_L, epsilon_L_max, percent_epsilon_L_max, pl, r0, x, y_fit):
    pl.errorbar(x,y_fit,10*epsilon_L)
    pl.xlabel(r'$x$')
    pl.ylabel(r'$y$')

    print ('max error is %4.3f' % epsilon_L_max)
    print ('the range is %4.3f' % r0)
    print ('Linearity error is %3.2f%s' % (percent_epsilon_L_max,'%'))
    return


if __name__ == "__main__":
    app.run()
