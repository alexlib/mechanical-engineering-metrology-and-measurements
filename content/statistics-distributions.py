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
    # Probability Distributions and the Central Limit Theorem
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mickey Atwal, Cold Spring Harbor Laboratory

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here we will visualize, in Python, a few important distributions that commonly appear in science and statistics. A more exhaustive list of statistical distributions can be found in the [stats](http://docs.scipy.org/doc/scipy/reference/stats.html) module of SciPy.

    At the end of this IPython Notebook we will demonstrate what is arguably the most famous and profound theorem in statistics: the Central Limit Theorem.
    """)
    return


@app.cell
def _():
    from __future__ import division


    import scipy.stats as stats
    from pylab import arange, exp, np, plt

    return arange, exp, np, plt, stats


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Discrete Distributions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathbf{BINOMIAL}$:The probability of observing $n$ successes, each with a probability $p$, out of $N$ attempts.
    $$
    P(n;N,p)=\displaystyle \left(
    \frac{N!}{n!(N-n)!}
    \right)
    p^n (1-p)^{N-n}
    $$

    * mean=$Np$, variance=$Np(1-p)$
    * Example: what is the probability of getting 2 heads out of 6 flips of a fair coin?
    """)
    return


@app.cell
def _(arange, plt, stats):
    _N = 6
    p = 0.5
    _n = arange(0, 20)
    _y = stats.binom.pmf(_n, _N, p)
    plt.plot(_n, _y, 'o-')
    plt.title('Binomial: N=%i , p=%.2f' % (_N, p), fontsize=15)
    plt.xlabel('n', fontsize=15)
    plt.ylabel('Probability of n', fontsize=15)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathbf{POISSON}$: The probability of observing $n$ low-probability successes when the average number of successes is $\mu$
    $$
    P(n;\mu)=\frac{\mu^n e^{-\mu}}{n!}
    $$

    * mean=$\mu$, variance=$\mu$
    * Example: what is probability of observing 60 new mutations in the genome of a child given that the average number of new mutations is 50?
    """)
    return


@app.cell
def _(arange, plt, stats):
    _u = 3
    _n = arange(0, 15)
    _y = stats.poisson.pmf(_n, _u)
    plt.plot(_n, _y, 'o-')
    plt.title('Poisson: $\\mu$ =%i' % _u, fontsize=15)
    plt.xlabel('n', fontsize=15)
    plt.ylabel('Probability of n', fontsize=15)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Continuous Distributions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathbf{GAUSSIAN (NORMAL)}$:
    $P(x;\mu,\sigma)=\displaystyle \frac{1}{\sqrt{2 \pi \sigma^2}} \exp{\displaystyle \left( -\frac{(x-\mu)^2}{2 \sigma^2} \right) },
    \hspace{1in} x \in [-\infty;\infty]$

    * mean=$\mu$, variance=$\sigma^2$
    * This distribution appears as the large N limit of the binomial distribution and the Central Limit Theorem.
    """)
    return


@app.cell
def _(arange, exp, np, plt):
    _u = 5  # mean
    s = 1  # standard deviation
    _x = arange(0, 15, 0.1)
    _y = 1 / np.sqrt(2 * np.pi * s * s) * exp(-((_x - _u) ** 2 / (2 * s * s)))
    plt.plot(_x, _y, '-')
    plt.title('Gaussian: $\\mu$=%.1f, $\\sigma$=%.1f' % (_u, s), fontsize=15)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('Probability density', fontsize=15)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathbf{EXPONENTIAL}$:
    $P(x;k)=k e^{-kx}, \hspace{1in} x \in [0,\infty], \hspace{0.1in} k>0$

    * mean=$1/k$,  variance=$1/k^2$
    * This distribution describes the time intervals in a homogeneous Poisson process.
    """)
    return


@app.cell
def _(arange, exp, plt):
    k = 0.4
    _x = arange(0, 15, 0.1)
    _y = k * exp(-k * _x)
    plt.plot(_x, _y, '-')
    plt.title('Exponential: $k$ =%.2f' % k, fontsize=15)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('Probability density', fontsize=15)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathbf{BETA}$: $P(x;\alpha,\beta)=\displaystyle \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$, $\hspace{1in} x \in  [0;1], \hspace{0.1in} \alpha>0, \hspace{0.1in}\beta>0$

    * mean=$\displaystyle \frac{\alpha}{\alpha+\beta}$, variance=$\displaystyle \frac{\alpha \beta}{(\alpha + \beta)^2(\alpha + \beta +1)}$
    * This distribution appears often in population genetics and Bayesian inference.
    """)
    return


@app.cell
def _(arange, plt, stats):
    _a = 0.5
    _b = 0.5
    _x = arange(0.01, 1, 0.01)
    _y = stats.beta.pdf(_x, _a, _b)
    plt.plot(_x, _y, '-')
    plt.title('Beta: a=%.1f, b=%.1f' % (_a, _b), fontsize=15)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('Probability density', fontsize=15)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Central Limit Theorem
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Take the mean of $n$ random samples from ANY arbitrary distribution with a well defined standard deviation $\sigma$ and mean $\mu$. As $n$ gets bigger the distribution of the sample mean will always converge to a Gaussian (normal) distribution with mean $\mu$ and standard deviation $\sigma/\sqrt{n}$.

    Colloquially speaking, the theorem states that the average (or sum) of a set of random measurements will tend to a bell-shaped curve no matter the shape of the original meaurement distribution. This explains the ubiquity of the Gaussian distribution in science and statistics. We can demonstrate the Central Limit Thereom in Python by sampling from three different distributions: flat, exponential, and beta.
    """)
    return


@app.cell
def _(exp, np, plt):
    from functools import partial  # provides capability to define function with partial arguments
    _N = 10000
    nobb = 101  # number of times n samples are taken. Try varying this number.
    _n = np.array([1, 2, 3, 5, 10, 100])  # number of bin boundaries on plots
    exp_mean = 3  # number of samples to average over
    _a, _b = (0.7, 0.5)
    dist = [partial(np.random.random), partial(np.random.exponential, exp_mean), partial(np.random.beta, _a, _b)]  # mean of exponential distribution
    title_names = ['Flat', 'Exponential (mean=%.1f)' % exp_mean, 'Beta (a=%.1f, b=%.1f)' % (_a, _b)]  # parameters of beta distribution
    drange = np.array([[0, 1], [0, 10], [0, 1]])
    means = np.array([0.5, exp_mean, _a / (_a + _b)])
    var = np.array([1 / 12, exp_mean ** 2, _a * _b / ((_a + _b + 1) * (_a + _b) ** 2)])
    binrange = np.array([np.linspace(p, q, nobb) for p, q in drange])  # ranges of distributions
    ln, ld = (len(_n), len(dist))  # means of distributions
    plt.figure(figsize=(ld * 4 + 1, ln * 2 + 1))  # variances of distributions
    for i in range(ln):
        for j in range(ld):
            plt.subplot(ln, ld, i * ld + 1 + j)
            plt.hist(np.mean(dist[j]((_N, _n[i])), 1), binrange[j], density=True)
            plt.xlim(drange[j])
            if j == 0:  # loop over number of n samples to average over
                plt.ylabel('n=%i' % _n[i], fontsize=15)  # loop over the different distributions
            if i == 0:
                plt.title(title_names[j], fontsize=15)
            else:
                clt = 1 / np.sqrt(2 * np.pi * var[j] / _n[i]) * exp(-((binrange[j] - means[j]) ** 2 * _n[i] / (2 * var[j])))
                plt.plot(binrange[j], clt, 'r', linewidth=2)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the graphs above the red curve is the predicted Gaussian distribution from the Central Limit Thereom. Notice that the rate of convergence of the sample mean to the Gaussian depends on the original parent distribution. Also,

    - the mean of the Gaussian distribution is the same as the original parent distribution,
    - the width of the Gaussian distribution scales as $1/\sqrt{n}$.
    """)
    return


if __name__ == "__main__":
    app.run()
