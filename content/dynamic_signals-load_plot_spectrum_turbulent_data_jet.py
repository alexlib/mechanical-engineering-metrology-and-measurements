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
    # Plot power spectrum of experimental data
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pylab as p

    return np, p


@app.cell
def _(np):
    # u = np.loadtxt('data/data_for_FFT.txt')
    data = np.loadtxt('data/p40_20.ts')
    # data source:
    # http://ldvproc.nambis.de/data/ektdata.html
    return (data,)


@app.cell
def _(data, p):
    p.plot(data[:500,0],data[:500,1])
    return


@app.cell
def _(data, p):
    p.hist(data[:,1],101,density=True);
    return


@app.cell
def _(data):
    u = data[:,1]

    meanu = u.mean()
    uf = u - meanu
    return (uf,)


@app.cell
def _(p, uf):
    p.plot(uf[:100])
    return


@app.cell
def _(np):
    def powerspectrum(x):
        s = np.fft.fft(x)
        return np.real(s*np.conjugate(s))

    return (powerspectrum,)


@app.cell
def _(powerspectrum, uf):
    specu = powerspectrum(uf)
    lenu, = specu.shape
    return lenu, specu


@app.cell
def _(lenu, p, specu):
    p.plot(specu[2:int(lenu/2)])
    return


if __name__ == "__main__":
    app.run()
