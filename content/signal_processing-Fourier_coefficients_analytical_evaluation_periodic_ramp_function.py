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
    # Symbolic evaluation of Fourier coefficients
    """)
    return


@app.cell
def _():
    from sympy import cos, integrate, pi, sin, sqrt, symbols
    from sympy.plotting import plot
    # init_printing(pretty_print=True,use_latex=True)
    # %matplotlib inline
    # import matplotlib.pyplot as plt
    from numpy import arange

    return arange, cos, integrate, pi, plot, sin, sqrt, symbols


@app.cell
def _(symbols):
    f,t,T,G = symbols('f t T G')
    return G, T, t


@app.cell
def _(G, t):
    f_1 = G * t - G / 2
    print('f =', f_1)
    return (f_1,)


@app.cell
def _(G, f_1, plot, t):
    p = plot((f_1.subs(G, 25), (t, 0, 1)), ((f_1 - 25).subs(G, 25), (t, 1, 2)), ((f_1 - 50).subs(G, 25), (t, 2, 3)), ylabel='$f = 25 t$ [V]', xlabel='$t$ [sec]', xlim=(0, 3), figsize=(10, 8))
    return


@app.cell
def _(G, T, f_1, integrate, t):
    c0 = integrate(f_1, (t, 0, T)) * (1 / T)
    print(c0)
    print(c0.subs([(G, 25), (T, 1)]))
    return


@app.cell
def _(T, f_1, integrate, pi, sin, t):
    a1 = 2 / T * integrate(f_1 * sin(2 * pi * 1 * t), (t, 0, T))
    return (a1,)


@app.cell
def _(G, T, a1, pi):
    print(a1)
    print( a1.subs([(T,1),(pi, 3.14),(G,25)]))
    return


@app.cell
def _(T, cos, f_1, integrate, pi, sin, t):
    a, b = ([], [])
    for _n in range(10):
        a.append(2 / T * integrate(f_1 * sin(_n * pi * t), (t, 0, T)))
        b.append(2 / T * integrate(f_1 * cos(_n * pi * t), (t, 0, T)))
    return a, b


@app.cell
def _(a, b):
    a[9], b[9]
    return


@app.cell
def _(G, T, a, b, pi, sqrt):
    c = []
    for _n in range(1, 10):
        print(a[_n])
        expr = sqrt(a[_n] ** 2 + b[_n] ** 2)
        expr = expr.subs([(T, 1), (pi, 3.14), (G, 25)])
        c.append(expr)  # print expr  # val = lambdify(t,expr,'numpy')
    return (c,)


@app.cell
def _(arange, c):
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots(figsize=(10,8))
    ax.bar(-.5+arange(1,10),c,alpha=.5)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
    ax.set_xlabel('$n$',fontsize=16)
    ax.set_ylabel('Fourier coefficients $a_n^2 + b_n^2$',fontsize=16)
    return


if __name__ == "__main__":
    app.run()
