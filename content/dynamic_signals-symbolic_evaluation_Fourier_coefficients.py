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
    # Symbolic evaluation of Fourier series coefficients
    """)
    return


@app.cell
def _():
    from sympy import cos, init_printing, integrate, pi, plot, sin, symbols
    init_printing(pretty_print=True,use_latex=True)
    import matplotlib.pyplot as plt

    return cos, integrate, pi, plot, plt, sin, symbols


@app.cell
def _(symbols):
    f,t,T,G = symbols('f t T G')
    return G, T, t


@app.cell
def _(G, t):
    f_1 = G * t
    print('f = ', f_1)
    return (f_1,)


@app.cell
def _(G, f_1, plot, t):
    plot((f_1.subs(G, 25), (t, 0, 1)), ((f_1 - 25).subs(G, 25), (t, 1, 2)), ((f_1 - 50).subs(G, 25), (t, 2, 3)), ylabel='f = 25 t [V]', xlabel='t [sec]', xlim=(0, 3))
    return


@app.cell
def _(G, T, f_1, integrate, t):
    c0 = integrate(f_1, (t, 0, T)) * (1 / T)
    print(c0)
    print(c0.subs([(G, 25), (T, 1)]))
    return


@app.cell
def _(T, f_1, integrate, pi, sin, t):
    a1 = 2 / T * integrate(f_1 * sin(2 * pi * t), (t, 0, T))
    return (a1,)


@app.cell
def _(G, T, a1, pi):
    print(a1)
    print(a1.subs([(T,1),(pi, 3.14),(G,25)]))
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
def _(G, T, a, b, pi):
    c = []
    for _n in range(1, 10):
        print(a[_n])
        expr = a[_n] ** 2 + b[_n] ** 2
        expr = expr.subs([(T, 1), (pi, 3.14), (G, 25)])
        c.append(expr)  # print expr  # val = lambdify(t,expr,'numpy')
    return (c,)


@app.cell
def _(c, plt):
    plt.figure()
    plt.bar(range(1,10),c)
    plt.xlabel('n')
    plt.ylabel('Fourier coefficients $a_n^2 + b_n^2$')
    return


if __name__ == "__main__":
    app.run()
