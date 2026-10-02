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
    # Calibration of non-linear (logarithmic) function
    """)
    return


@app.cell
def _():
    from pylab import linspace, loadtxt, loglog, np, ones, plot, polyfit
    from io import StringIO

    return StringIO, linspace, loadtxt, loglog, np, ones, plot, polyfit


@app.cell
def _(StringIO, loadtxt):
    # create two signals: concentration and temperature
    c = StringIO("""
    1.095406121 3.887032952 6.956500526 9.486921797 \
    13.96944459 14.86018043 23.19810833 24.53008787 \
    24.72311112 37.44113657 38.05523491 54.1881169""")


    T = StringIO("""91.72763561 70.60278306 \
    53.0039356 45.03419592 32.45847839 29.03763728 13.49252686 \
    12.0641877 18.91647307 12.01351046 11.49379565 9.671537342 """)

    c = loadtxt(c)
    T = loadtxt(T)
    return T, c


@app.cell
def _(T, c, plot):
    plot(c,T,'o')
    return


@app.cell
def _(T, c, np, plot):
    a = -np.log10(T)
    plot(c,a,'o')
    return (a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### see the linear part and the "saturated part", use only the linear one
    """)
    return


@app.cell
def _(a, c, plot):
    ind = c < 24
    plot(c[ind],a[ind],':o')
    return (ind,)


@app.cell
def _(a, c, ind, polyfit):
    polyfit(c[ind],a[ind],1)
    return


@app.cell
def _(a, c, linspace, plot):
    plot(c, a, 'o')
    c1 = linspace(0, 60, 100)
    _a1 = 0.037 * c1 - 2.0
    plot(c1, _a1, '--')
    return (c1,)


@app.cell
def _(T, c, c1, plot):
    plot(c, T, 'o')
    _a1 = 0.037 * c1 - 2.0
    plot(c1, 10 ** (-_a1), '--')
    return


@app.cell
def _(T, c):
    print(f'c = {c}')
    print(f'T = {T}')
    return


@app.cell
def _(T, c, plot):
    plot(c,T,'bo',c[6:8],T[6:8],'rs')
    return


@app.cell
def _(T, c, ones, plot):
    c2 = c.copy()
    T2 = T.copy()
    mask = ones(c2.shape[0],dtype=bool)
    mask[[6,7]] = False
    plot(c2[mask],T2[mask],'o')
    return T2, c2, mask


@app.cell
def _(T2, c2, mask, plot):
    plot(c2[mask]-c2[0],T2[mask]-T2[0],'o')
    return


@app.cell
def _(T2, c2, mask):
    c3 = c2[mask] - c2[0]
    T3 = T2[0] - T2[mask]
    return T3, c3


@app.cell
def _(c3):
    c3
    return


@app.cell
def _(T3, c3, loglog):
    loglog(c3,T3,'o')
    return


if __name__ == "__main__":
    app.run()
