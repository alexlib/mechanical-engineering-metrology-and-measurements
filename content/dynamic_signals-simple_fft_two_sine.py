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
    # Fast Fourier Transform (FFT) of a sum of two sine signals
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.fftpack import fft
    N = 600
    # Number of samplepoints
    T = 1.0 / 800.0
    # sample spacing
    x = np.linspace(0.0, N * T, N)
    y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    yf = fft(y)
    halfN = int(N / 2)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), halfN)
    plt.plot(xf, 2.0 / N * np.abs(yf[0:halfN]))
    plt.grid()
    plt.show()
    return N, fft, halfN, np, plt, x, xf, y, yf


@app.cell
def _(np, plt, x, y):
    plt.figure()
    plt.plot(x,y)
    plt.plot(x,0.7*np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x),'r')
    return


@app.cell
def _(N, fft, halfN, np, plt, xf, y, yf):
    from scipy.signal.windows import hann
    w = hann(N)
    ywf = fft(y*w)
    plt.figure()
    plt.plot(xf[1:halfN], 2.0/N * np.abs(yf[1:halfN]), '-b')
    plt.plot(xf[1:halfN], np.sqrt(8/3)*2.0/N * np.abs(ywf[1:halfN]), '-r')
    plt.legend(['FFT', 'FFT w. window'])
    plt.grid()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
