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
    # Statistical parameters using probability density function
    ### Given probability density function, $p(x)$

    $ p = 2x/b^2$, $0 < x < b$

    ### The mean value of $x$ is estimated analytically:
    $\overline{x} = \int\limits_0^b x\, p(x)\, dx = \int\limits_0^b 2x^2/b^2 = \left. 2x^3/3b^2\right|_0^b =2b^3/3b^2 = 2b/3$

    ### the median
    median: $ \int\limits_0^m p(x)\,dx = 1/2 = \int\limits_0^m 2x/b^2\,dx = \left. x^2/b^2 \right|_0^m = m^2/b^2 = 1/2$, $m = b/\sqrt(2)$

    ### the second moment
    second moment: $x^{(2)} = \int\limits_0^b x^2\, p(x)\, dx = \int\limits_0^b 2x^3/b^2 = \left. x^4/2b^2\right|_0^b =b^4/2b^2 = b^2/2$

    ### the variance is the second moment less the squared mean value
    $var(x) = x^{(2)} - \overline{x}^2 = b^2/2 - 4b^2/9 = b^2/18$
    """)
    return


@app.cell
def _():
    from pylab import linspace, plot, xlabel, ylabel
    import numpy as np

    return linspace, np, plot, xlabel, ylabel


@app.function
def p(x,b):
    return 2*x/(b**2)


@app.cell
def _(linspace):
    b = 2
    x = linspace(0,b,200)
    y = p(x,b)
    return b, x, y


@app.cell
def _(plot, x, xlabel, y, ylabel):
    plot(x,y)
    xlabel('$x$')
    ylabel('$p(x)$')
    return


@app.cell
def _(b, np, x, y):
    # approximate using the numerical integration
    print(np.trapezoid(y*x,x))
    print(2.*b/3)
    return


@app.cell
def _(b, np, x, y):
    print(np.trapezoid(y*x**2,x))
    print(b**2/18)
    return


@app.cell
def _():
    import sympy

    return (sympy,)


@app.cell
def _(sympy):
    x_1, b_1, p_1, m = sympy.symbols('x,b,p,m')
    p_1 = 2 * x_1 / b_1 ** 2
    print(p_1)
    return b_1, m, p_1, x_1


@app.cell
def _(b_1, p_1, sympy, x_1):
    sympy.integrate(p_1 * x_1, (x_1, 0, b_1))
    return


@app.cell
def _(b_1, p_1, sympy, x_1):
    sympy.integrate(p_1 * x_1 ** 2, (x_1, 0, b_1))
    return


@app.cell
def _(m, p_1, sympy, x_1):
    sympy.integrate(p_1, (x_1, 0, m))
    return


@app.cell
def _(b_1, m, sympy):
    sympy.solve(m ** 2 / b_1 ** 2 - 0.5, m)
    return


if __name__ == "__main__":
    app.run()
