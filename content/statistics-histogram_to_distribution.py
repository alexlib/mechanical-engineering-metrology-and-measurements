import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import numpy.random as random
    from pylab import arange, bar, diff, hist, plot, xlabel, ylabel

    return arange, bar, diff, hist, plot, random, xlabel, ylabel


@app.cell
def _(random):
    x = random.normal(10.0, 3.0,size=200)
    return (x,)


@app.cell
def _(plot, x, xlabel, ylabel):
    plot(x)
    xlabel('time',fontsize=16)
    ylabel(r'$x$',fontsize=16)
    return


@app.cell
def _(hist, x, xlabel, ylabel):
    h = hist(x)
    xlabel('bins of x')
    ylabel('frequency of x')
    return (h,)


@app.cell
def _(bar, diff, h):
    # make it yourself
    pos = h[1][:-1]+diff(h[1])/2.
    frequency = h[0]
    bar(pos,frequency,width=1.4)
    return frequency, pos


@app.cell
def _(bar, frequency, pos, xlabel, ylabel):
    # now we can normalize:
    probability = frequency/sum(frequency)
    bar(pos,probability,width=1.4)
    xlabel('bins of x')
    ylabel('probability')
    return (probability,)


@app.cell
def _(diff, pos):
    dx = diff(pos)[0]
    print(('{:.2f}'.format(dx)))
    return (dx,)


@app.cell
def _(bar, dx, pos, probability, xlabel, ylabel):
    density = probability/dx
    bar(pos,density,width=1.4)
    xlabel('bins of x')
    ylabel('probability density')
    return (density,)


@app.cell
def _(pos, x):
    z = (pos - x.mean())/x.std()
    return (z,)


@app.cell
def _(density, x):
    # probability density function 
    pdf = x.std() * density
    return (pdf,)


@app.cell
def _(arange, bar, pdf, plot, xlabel, ylabel, z):
    from scipy.stats import norm

    y = norm.pdf( z, 0, 1)
    bar(z,pdf,alpha=.3,width=.4),
    zi = arange(-3,3,.1)
    yi = norm.pdf( zi, 0, 1)
    plot(zi, yi, 'k--', linewidth=2)
    xlabel(r'$z$',fontsize=16)
    ylabel(r'pdf', fontsize=16);
    return


if __name__ == "__main__":
    app.run()
