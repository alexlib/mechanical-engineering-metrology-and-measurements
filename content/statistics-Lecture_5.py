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
    ## Lecture 5 - probability and statistics

    In this notebook we will collect all the examples from Lecture 5 ``Probability and statistics''
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Histogram
    """)
    return


@app.cell
def _():
    import numpy as np                   # numerical stuff
    from matplotlib import pyplot as plt # plotting functions
    plt.style.use('fivethirtyeight')
    return np, plt


@app.cell
def _(np):
    # let's create some data
    x = np.array([12.1,12.3,12.2,12.2,12.4,12.3,12.2,12.4,12.2,12.5])
    return (x,)


@app.cell
def _(plt, x):
    # create histogram using matplotlib and store the histogram output
    x_modes = plt.hist(x) #note that we did not specify number of bins
    return (x_modes,)


@app.cell
def _(np, x, x_modes):
    # the output in x_modes

    # which bin has most samples? 
    x_mode_ind = np.argmax(x_modes[0])

    # how many counts in the top column? 
    x_mode_count = x_modes[0][x_mode_ind]

    # what is the value of most frequent sample: 
    x_mode_val = x[x_mode_ind]


    print(f"Data: {x}")
    print(f"Mean: {np.mean(x):.2f}, Median: {np.median(x):.2f} STD: {np.std(x):.2f}")
    print(f"Mode: {x_mode_val} appears {x_mode_count} times" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Let's create our own histogram
    """)
    return


@app.cell
def _(np, x):
    nbins = 7  # better then the default choice 
    hist_vals = np.zeros(nbins)
    min_val = x.min() - 0.05
    max_val = x.max() + 0.05
    for d in x:
        bin_number = int(nbins * ((d - min_val) / (max_val - min_val)))
        hist_vals[bin_number] = hist_vals[bin_number] + 1  # for every item  # find which bin it belongs  # add a counter
    return hist_vals, max_val, min_val, nbins


@app.cell
def _(hist_vals, max_val, min_val, nbins, np, plt):
    # let's plot some columns
    plt.bar(np.linspace(min_val,max_val,nbins),hist_vals,width = 0.05)
    plt.xlim([min_val-.1,max_val+.1]);
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Now we can load some real long sample of turbulent temperature fluctuations
    """)
    return


@app.cell
def _(np, plt):
    data = np.loadtxt('data/thermocouples.dat',skiprows=1)
    t = data[:,0]
    T = data[:,1]

    # visualize the data first
    plt.plot(t,T)
    plt.xlabel('$t$ [sec]')
    plt.ylabel(r'$T^\circ$C')
    return T, t


@app.cell
def _(np, t):
    # what are the recommended number of bins, see wikipedia 

    # for short samples
    print(f" for short samples: {int(1 + 3.3*np.log10(len(t)))}")
    print(f" another rule {int(1.87*(len(t)-1)**(0.4))}")


    # for long samples
    print(f" for long samples: {int(2*len(t)**(0.33))}")
    print(f" for very long ones: {int(np.sqrt(len(t)))}")
    return


@app.cell
def _(T, np, plt):
    _J = 11
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    n, bins, _patches = ax[0].hist(T, _J)
    x_1 = bins[:-1] + 0.5 * np.diff(bins)[0]
    ax[0].plot(x_1, n, 'r')
    ax[0].set_xlabel('$T^\\circ$C')
    ax[0].set_ylabel('Counts')
    ax[0].set_title('11 bins')
    _J = 19
    n, bins, _patches = ax[1].hist(T, _J)
    x_1 = bins[:-1] + 0.5 * np.diff(bins)[0]
    ax[1].plot(x_1, n, 'r')
    ax[1].set_xlabel('$T^\\circ$C')
    ax[1].set_ylabel('Counts')
    ax[1].set_title('19 bins')
    return


@app.cell
def _(T, np, plt):
    _J = 15
    n_1, bins_1, _patches = plt.hist(T, _J)
    x_2 = bins_1[:-1] + 0.5 * np.diff(bins_1)[0]
    plt.plot(x_2, n_1, 'r')
    plt.xlabel('$T^\\circ$C')
    plt.ylabel('Counts')
    plt.title('15 bins')
    return n_1, x_2


@app.cell
def _(n_1, plt, x_2):
    # vertical normalization
    p = n_1 / 1000.0  # data.shape[0]
    plt.plot(x_2, p)
    plt.xlabel('$T^\\circ$C')
    plt.ylabel('Relative counts')
    plt.title('Vertically normalized')
    return (p,)


@app.cell
def _(np, p, plt, x_2):
    # area normalization
    f = p / np.diff(x_2)[0]
    plt.plot(x_2, f, lw=2)
    plt.xlabel('$T^\\circ$C')
    plt.ylabel('Probability Density')
    return (f,)


@app.cell
def _(T, f, plt, x_2):
    # horizontal normalization, transfer to Gaussian z
    z = (x_2 - T.mean()) / T.std()
    plt.plot(z, f)
    plt.xlabel('$x$ ')
    plt.ylabel('$P(x)$')
    plt.title('Final result')
    return (z,)


@app.cell
def _(f, np, plt, z):
    def gaussian(x,mu,sig):
        return 1/(sig*np.sqrt(2*np.pi))*np.exp(-((x-mu)**2)/(2*sig**2))

    plt.plot(z,f,z,gaussian(z,0,1),'r')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$P(x)$')
    plt.title('Blue - original, red - Gaussian')
    return


@app.cell
def _(T, np):
    import scipy.stats as st

    print(("T skewness = %.3f, kurtosis = %.3f" % (st.skew(T), st.kurtosis(T))))
    tmp = np.random.randn(1000)
    print(("Normal distribution skewness = %.3f, kurtosis = %.3f" % (st.skew(tmp), st.kurtosis(tmp))))
    return (st,)


@app.cell
def _(f, np, x_2):
    # area under the curve
    print('Area under the curve = %f ' % np.trapezoid(f, x_2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Chi-square test

    How well does a set of measurements follow an assumed distribution function?
    """)
    return


@app.cell
def _(np):
    data_1 = np.array([0.98, 1.07, 0.86, 1.16, 0.96, 0.68, 1.34, 1.04, 1.21, 0.86, 1.02, 1.26, 1.08, 1.02, 0.94, 1.11, 0.99, 0.78, 1.06, 0.96])
    return (data_1,)


@app.cell
def _(data_1, plt):
    # import matplotlib.pyplot as plt
    plt.plot(data_1, 'o')
    plt.xlabel('$i$')
    plt.ylabel('$x_i$')
    return


@app.cell
def _(data_1, np):
    (np.mean(data_1), np.std(data_1), data_1.shape[0], np.min(data_1), np.max(data_1))
    return


@app.cell
def _(data_1, np):
    n_2 = data_1.shape[0]
    K = int(1.87 * (n_2 - 1) ** 0.4 + 1)
    print(f'best number of bins is {K}')
    bins_2 = np.arange(0.65, 1.45, 0.1)
    print(bins_2)
    return K, bins_2, n_2


@app.cell
def _(bins_2, data_1, plt):
    # let's see the histogram
    plt.hist(data_1, bins=bins_2, width=0.07)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\chi^2 = \sum_{j} (n_j - n'_j)^2 / n'_j \quad j = 1,2, ..., k$  bins

    $n'_j = N (p(x_u) - p(x_l))$

    $p(x_u) = \int\limits_{0}^{x_u} G(x) $
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    the goodness of fit test evaluates the null hypothesis $H_0$ that the data are described by the assumed distribution
    """)
    return


@app.cell
def _(data_1, np, st):
    # calculate probability
    from math import erf, sqrt
    x1 = 0.75
    x2 = 0.85
    mu = data_1.mean()
    sigma = data_1.std()

    def probability(x, mu, sigma):
    # probability from Z=0 to lower bound
        """ Probability is the area under the Gaussian curve which is identical to the 
        cumulative density function value """
        return 0.5 * erf((x - mu) / (sigma * sqrt(2.0)))

    def expected(lower, upper, mu, sigma, n):
        """ Expected number of samples in some bin is the number of samples times the 
        probability of a variable to be between the lower and upper edge of the bin  """
        return np.abs(n * (st.norm(mu, sigma).cdf(lower) - st.norm(mu, sigma).cdf(upper)))
    print(expected(0.75, 0.85, mu, sigma, 20))  # return np.abs(n * (probability(lower,mu,sigma) - probability(upper,mu,sigma)))
    return expected, mu, sigma


@app.cell
def _(bins_2, data_1, expected, mu, n_2, np, plt, sigma):
    oh = np.histogram(data_1, bins=bins_2)
    x_3 = []
    y = []
    for i in range(len(bins_2) - 1):
        x_3.append((oh[1][i] + oh[1][i + 1]) / 2)
        y.append(expected(bins_2[i], bins_2[i + 1], mu, sigma, n_2))
    chisq = []  # middle of the bin
    for a, b in zip(oh[0], y):
        chisq.append((a - b) ** 2 / b)
    plt.bar(x_3, y, width=0.02, color='r', alpha=0.8)
    plt.bar(x_3, oh[0], width=0.05, alpha=0.5)
    plt.legend(('$E_i$', '$O_i$'))
    print(f'chi square = {np.sum(chisq)}')
    return (chisq,)


@app.cell
def _(K):
    # degrees of freedom = K.- 2 because we used mean and std:
    df = K - 2
    return


@app.cell
def _(K, chisq, np, st):
    pval = 1 - st.chi2.cdf(np.sum(chisq), K-2);
    print(f'Confidence level is {(pval*100)} percent')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### From sample to population statistics
    or from a histogram to the probability density function

    1. [Histogram to distribution](statistics-histogram_to_distribution.md)
    1. [chi^2 test of normal distribution using SciPy stats](statistics-chi_square_test_example.md)
    1. [Central limit theorem illustration](statistics-Central_limit_theorem_illustration.md)
    1. [Various probability Distributions and the Central Limit Theorem](statistics-distributions.md)
    1. [Student t-distribution](statistics-t-distribution.md)
    1. [t-test comparing two samples](statistics-t-test.md)
    """)
    return


if __name__ == "__main__":
    app.run()
