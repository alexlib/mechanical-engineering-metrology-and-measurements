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
    # Fourier transforms

    ## From very naive approximations of the spectrum to more complex examples:
    """)
    return


@app.cell
def _():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import fft

    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Two basic ploting functions that repeat the actuall spectral analysis:
    """)
    return


@app.cell
def _(np, plt):
    # redefine default figure size and fonts


    # create signal
    def create_signal(fs, N, a=[1., 1.5], f=[10.0, 35.7], DC=0):
        """ create a periodic signal with a DC and a Gaussian noise"""
        dt = 1./fs
        t = np.linspace(0, N*dt, N)
        y = np.random.normal(0, 1, N) + DC
        for aa, ff in zip(a, f):
            y += aa*np.sin(2*np.pi*ff*t)

        noise = np.random.normal(0, 1, N)
        y += noise
        return t, y


    def spectrum(y, Fs):
        """
        Plots a Single-Sided Amplitude Spectrum of a sampled
        signal y(t), sampling frequency Fs (length of a signal
        provides the number of samples recorded)

        Following: http://goo.gl/wRoUn
        """
        n = len(y)  # length of the signal
        k = np.arange(n)
        T = n/Fs
        frq = k/T  # two sides frequency range
        frq = frq[range(int(n/2))]  # one side frequency range
        Y = 2*np.fft.fft(y)/n  # np.fft computing and normalization
        Y = Y[range(int(n/2))]
        return (frq, Y)


    def plotSignal(A, ff, fs, N):

        T = N/fs  # sampling period
        t = np.arange(0.0, T, T/N)  # sampling time steps
        y = A*np.sin(2*np.pi*ff*t)  # sampled signal
        frq, Y = spectrum(y, fs)  # FFT(sampled signal)

        # Plot
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))
        ax[0].plot(t, y, 'b.')
        ax[0].set_xlabel('$t$ [s]')
        ax[0].set_ylabel('Y [V]')
        ax[0].plot(t[0], y[0], 'ro')
        ax[0].plot(t[-1], y[-1], 'ro')

        ax[1].plot(frq, abs(Y), 'r')  # plotting the spectrum
        ax[1].set_xlabel('$f$ (Hz)')
        ax[1].set_ylabel('$|Y(f)|$')
        lgnd = str(r'N = %d, f = %d Hz' % (N, fs))
        ax[1].legend([lgnd], loc='best')

    return (plotSignal,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## More elaborate example, demonstration of a leakage effect:
    """)
    return


@app.cell
def _(plotSignal):
    # We sample a signal at fs = 200 Hz and record 256 points"
    A = 1.0
    # true values
    ff = 10.0  # Volt, amplitude
    _fs = 200.0  # Hz, signal frequency, zero harmonics
    _N = 256
    # We will work with different sampling frequencies
    # and different lengths of records:
    plotSignal(A, ff, _fs, _N)  #Hz  # points
    return A, ff


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note:
    1. leakage at around 10 Hz
    2. peak is below 1 Volt
    3. we can get the spectrum up to half of sampling frequency
    4. frequency resolution is $\Delta f = 1/T = 0.781$ Hz

    ### Let us try to minimize the leakage:
    #### Let's first increase the sampling rate, stay with N = 256
    """)
    return


@app.cell
def _(A, ff, plotSignal):
    _fs = 1000.0  #Hz
    _N = 512  # points
    plotSignal(A, ff, _fs, _N)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note:
    1. resolution in time is great BUT:
    1. resolution in frequency is worse, $\Delta f = 1/T = 1/0.25 = 3.91$ Hz
    2. we see up to 500 Hz, but have here only 128 useful points
    3. leakage is severe, the peak amplitude is about 0.66 Volt
    4. peak location is now 11.7 Hz

    <span style="color:red"> **MORE IS NOT NECESSARILY BETTER** </span>

    ###Let us try to minimize the leakage problem sampling closer to the Nyquist frequency
    """)
    return


@app.cell
def _(A, ff, plotSignal):
    _fs = 25.0  #Hz
    _N = 256  # points
    plotSignal(A, ff, _fs, _N)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note:
    1. sine does not seem to be a sine wave, time resolution is bad for Nyquist frequency
    2. frequency resolution is better, about 0.1 Hz
    3. peak is about 0.75 Volt, less leakage but still strong
    4. peak location is close, 9.96 Hz

    ### Let's get more points, keep same sampling frequency
    """)
    return


@app.cell
def _(A, ff, plotSignal):
    _fs = 25.0  #Hz
    _N = 512  # points
    plotSignal(A, ff, _fs, _N)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Note:
    1. time sampling is much longer, $T = N/f_s = 512/(25 Hz) = 20.48$ s
    2. peak is narrow, at 10.01 Hz
    3. resolution is good, much lower leakage, value is close to 0.9 Volt

    ### Still, how to get the *perfect* spectrum? Use tricks, for instance, sample at a specific frequency:
    """)
    return


@app.cell
def _(A, ff, plotSignal):
    _fs = 25.6  #Hz
    _N = 256  # points
    plotSignal(A, ff, _fs, _N)
    return


@app.cell
def _(A, ff, plotSignal):
    # After you know the real value, you can save a lot of time:
    _fs = 25.6  #Hz
    _N = 64  # points
    plotSignal(A, ff, _fs, _N)
    return


if __name__ == "__main__":
    app.run()
