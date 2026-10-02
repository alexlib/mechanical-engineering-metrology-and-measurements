import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import scipy.stats

    return matplotlib, np, plt, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Statistical distribution
    ========================

    Let's have a look how different statistical distributions look like, to have a better
    idea what to use as prior on our inference bayesian exploration.

    All the distributions available in scipy can be found on the docs here: http://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats

    Let's start with Discrete distributions

    Discrete Distributions
    ----------------------

    * bernoulli:	A Bernoulli discrete random variable.
    * binom:	A binomial discrete random variable.
    * poisson:	A Poisson discrete random variable.
    * ...
    """)
    return
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exploring Different Probability Distributions
    """)
    return




@app.cell
def _():
    from scipy.stats import bernoulli, poisson, binom

    return bernoulli, binom, poisson


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Bernoulli distribution
    -----------------------

    Given a certain probability $p$, the Bernoulli distribution takes value $k=1$, meanwhile
    it takes $k=0$ in all the other cases $1-p$.

    In other words:

    $$
    f(k;p) = \begin{cases}
        p & \text{if } k=1 \\\\
        1-p & \text{if } k=0
    \end{cases}
    $$
    """)
    return


@app.cell
def _(bernoulli):
    bernoulli.rvs(0.6, size=100)
    return


@app.cell
def _(bernoulli, matplotlib, np, plt):
    _a = np.arange(2)
    colors = matplotlib.rcParams['axes.prop_cycle'].by_key()['color']
    plt.figure(figsize=(12, 8))
    for _i, _p in enumerate([0.1, 0.2, 0.6, 0.7]):
        ax = plt.subplot(1, 4, _i + 1)
        plt.bar(_a, bernoulli.pmf(_a, _p), label=_p, color=colors[_i], alpha=0.5)
        ax.xaxis.set_ticks(_a)
        plt.legend(loc=0)
        if _i == 0:
            plt.ylabel('PDF at $k$')
    plt.suptitle('Bernoulli probability')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Poisson Distribution
    --------------------

    Another discrete distribution, the *Poisson Distribution* is defined for all the integer positive number as

    $$P(Z=k)=\frac{λ^ke^{−λ}}{k!}, k=0,1,2, \ldots$$
    """)
    return


@app.cell
def _(matplotlib, np, plt, poisson):
    _k = np.arange(20)
    colors_1 = matplotlib.rcParams['axes.prop_cycle'].by_key()['color']
    plt.figure(figsize=(12, 8))
    for _i, _lambda_ in enumerate([1, 4, 6, 12]):
        plt.bar(_k, poisson.pmf(_k, _lambda_), label=_lambda_, color=colors_1[_i], alpha=0.4, edgecolor=colors_1[_i], lw=3)
        plt.legend()
    plt.title('Poisson distribution')
    plt.xlabel('$k$')
    plt.ylabel('PDF at k')
    return (colors_1,)


@app.cell
def _(colors_1, np, plt, poisson):
    _k = np.arange(15)
    plt.figure(figsize=(12, 8))
    for _i, _lambda_ in enumerate([1, 2, 4, 6]):
        plt.plot(_k, poisson.pmf(_k, _lambda_), '-o', label=_lambda_, color=colors_1[_i])
        plt.fill_between(_k, poisson.pmf(_k, _lambda_), color=colors_1[_i], alpha=0.5)
        plt.legend()
    plt.title('Poisson distribution')
    plt.ylabel('PDF at $k$')
    plt.xlabel('$k$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Binomial distribution
    ---------------------

    Last but not least, the binomial distribution which is defined as:

    $$f(k;n,p) = Pr(X = k) = {n \choose k} p^k (1-p)^{(n-k)}$$

    where

    $${n \choose k} = \frac{n!}{k!(n-k)!}$$

    with $k={1, 2, 3, \ldots}$
    """)
    return


@app.cell
def _(binom, colors_1, np, plt):
    plt.figure(figsize=(12, 6))
    _k = np.arange(0, 22)
    for _p, color in zip([0.1, 0.3, 0.6, 0.8], colors_1):
        rv = binom(20, _p)
        plt.plot(_k, rv.pmf(_k), lw=2, color=color, label=_p)
        plt.fill_between(_k, rv.pmf(_k), color=color, alpha=0.5)
    plt.legend()
    plt.title('Binomial distribution')
    plt.tight_layout()
    plt.ylabel('PDF at $k$')
    plt.xlabel('$k$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Continous Probability Distribution
    ----------------------------------

    They are defined for any value of a positive $x$. A lot of distribution are defined on `scipy.stats`, so I will explore only som:

    * alpha	An alpha continuous random variable.
    * beta	A beta continuous random variable.
    * gamma	A gamma continuous random variable.
    * expon	An exponential continuous random variable.
    * ...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Alpha
    -----

    The Alpha distribution is defined as

    $$
    alpha.pdf(x,a) = \frac{1}{x^2 \Phi(a) \sqrt{2*pi}} * exp(-\frac{1}{2} (\frac{a-1}{x})^2), \,\, with \, x > 0, a > 0
    $$
    """)
    return


@app.cell
def _(colors_1, np, plt, scipy):
    _x = np.linspace(0.1, 2, 100)
    alpha = scipy.stats.alpha
    alphas = [0.5, 1, 2, 4]
    plt.figure(figsize=(12, 6))
    for _a, _c in zip(alphas, colors_1):
        label = '$\\alpha$ = {0:.1f}'.format(_a)
        plt.plot(_x, alpha.pdf(_x, _a), lw=2, color=_c, label=label)
        plt.fill_between(_x, alpha.pdf(_x, _a), color=_c, alpha=0.33)
    plt.ylabel('PDF at $x$')
    plt.xlabel('$x$')
    plt.title('Alpha distribution')
    plt.legend()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Beta distribution
    -----------------

    The Beta distribution is defined for a variabile rangin between 0 and 1.

    The pdf is defined as:

    $$
    beta.pdf(x, \alpha, \beta) = \frac{1}{B(\alpha, \beta)}x^{\alpha-1}(1 - x)^{\beta-1}, \; with \;  0≤x≤1, \alpha>0, \beta>0
    $$
    """)
    return


@app.cell
def _(colors_1, np, plt, scipy):
    beta = scipy.stats.beta
    _x = np.linspace(0, 1, num=200)
    fig = plt.figure(figsize=(12, 6))
    for _a, b, _c in zip([0.5, 0.5, 1, 2, 3], [0.5, 1, 3, 2, 5], colors_1):
        plt.plot(_x, beta.pdf(_x, _a, b), lw=2, c=_c, label='$\\alpha = {0:.1f}, \\beta={1:.1f}$'.format(_a, b))
        plt.fill_between(_x, beta.pdf(_x, _a, b), color=_c, alpha=0.1)
    plt.legend(loc=0)
    plt.ylabel('PDF at $x$')
    plt.xlabel('$x$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Gamma distribution
    ------------------

    The gamma distribution uses the Gamma function (http://en.wikipedia.org/wiki/Gamma_function) and it has two shape parameters.

    $$
    gamma.pdf(x, \alpha, scale) = \lambda^\alpha * x^{(\alpha-1)} * \frac{exp(-\lambda * x)}{\gamma(\alpha)}, \, with \, x >= 0, \alpha> 0, \lambda > 0
    $$

    The scale parameter is equal = $1.0/\lambda$
    """)
    return


@app.cell
def _(colors_1, np, plt, scipy):
    gamma = scipy.stats.gamma
    plt.figure(figsize=(12, 6))
    _x = np.linspace(0, 10, num=200)
    for _a, _c in zip([0.5, 1, 2, 3, 10], colors_1):
        plt.plot(_x, gamma.pdf(_x, _a), lw=2, c=_c, label='$\\alpha = {0:.1f}$'.format(_a))
        plt.fill_between(_x, gamma.pdf(_x, _a), color=_c, alpha=0.1)
    plt.legend(loc=0)
    plt.title('Gamma distribution with scale=1')
    plt.ylabel('PDF at $x$')
    plt.xlabel('$x$')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exponential
    -----------

    The Exponantial probability function is

    $$ f_X(x|λ) = λ e^{−λx} , \, x≥0$$

    Therefore, the random variable X has an exponential distribution with parameter λ, we say X is exponential and write

    $$ X∼Exp(λ) $$

    Given a specific λ, the expected value of an exponential random variable is equal to the inverse of λ, that is:

    $$ E[X|λ]= \frac{1}{λ} $$
    """)
    return


@app.cell
def _(colors_1, np, plt, scipy):
    _x = np.linspace(0, 4, 100)
    expo = scipy.stats.expon
    _lambda_ = [0.5, 1, 2, 4]
    plt.figure(figsize=(12, 4))
    for l, _c in zip(_lambda_, colors_1):
        plt.plot(_x, expo.pdf(_x, scale=1.0 / l), lw=2, color=_c, label='$\\lambda = %.1f$' % l)
        plt.fill_between(_x, expo.pdf(_x, scale=1.0 / l), color=_c, alpha=0.33)
    plt.legend()
    plt.ylabel('PDF at $x$')
    plt.xlabel('$x$')
    plt.title('Probability density function of an Exponential random variable; differing $\\lambda$')
    return


if __name__ == "__main__":
    app.run()
