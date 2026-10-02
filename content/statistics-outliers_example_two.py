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
    # Outlier Detection: Comparing Tests

    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as pl

    import matplotlib as mpl
    mpl.rcParams['lines.linewidth']=2
    mpl.rcParams['lines.color']='r'
    mpl.rcParams['figure.figsize']=(10,8)
    mpl.rcParams['font.size']=14
    mpl.rcParams['axes.labelsize']=20
    return np, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Single variable, $x$
    """)
    return


@app.cell
def _(np):
    x = np.array([49.3,50.2,49.2,49.8,50.5,49.3,48.9,49.9,50.1,49.2])
    return (x,)


@app.cell
def _(pl, x):
    pl.figure()
    pl.plot(x,'o')
    pl.xlim([-1,8])
    pl.ylim([48,52])
    pl.ylabel('$x$')
    pl.xlabel('$n$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## We use modified Thompson test (based on Student's t-distribution)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sort the values
    """)
    return


@app.cell
def _(x):
    x.sort()
    return


@app.cell
def _(x):
    x
    return


@app.cell
def _(pl, x):
    pl.plot(x,'o')
    pl.xlim([-1,8])
    pl.ylim([48,52])
    pl.ylabel('$x$')
    pl.xlabel('$n$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: we suspect in the sorted list of values the first and the last
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### get the sample mean and sample standard deviation, get deviations
    """)
    return


@app.cell
def _(np, x):
    x_mean = np.mean(x)
    x_std = np.std(x,ddof=1)
    print( x_mean)
    print (x_std)
    return (x_mean,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\delta_i = | x - x_i |$
    """)
    return


@app.cell
def _(pl, x, x_mean):
    delta = abs(x - x_mean)
    pl.plot(delta,'o')
    pl.xlim([-1,8])
    pl.ylim([-.5,1])
    pl.ylabel('$\delta$')
    pl.xlabel('$n$')
    print (delta[0],delta[-1])
    return


if __name__ == "__main__":
    app.run()
