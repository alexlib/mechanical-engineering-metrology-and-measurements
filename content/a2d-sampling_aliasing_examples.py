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
    # Sampling, clipping and aliasing
    """)
    return


@app.cell
def _():
    from scipy.interpolate import interp1d
    import matplotlib.pyplot as plt
    import numpy as np
    def sampling(t,y,fs):
        """ sampling of a signal y(t) at frequency fs [Hz]
        inputs:
            t  - time signal [s], array of floats, dense sampled
            y  - signal [Volt], array of floats
            fs  - sampling frequency [Hz], float
        """
        dt = 1./fs
        ts = np.arange(t[0],t[-1],dt)
        # ts = np.linspace(t[0],t[-1],(t[-1]-t[0])/dt)
        ys = np.interp(ts,t,y,left=0.0,right=0.0)

        return ts,ys

    return interp1d, np, plt, sampling


@app.cell
def _(np):
    def quantization(ys,N):
        """quantization of a signal
        inputs:
            ts - time signal [s], array
            ys - signal [Volt], array
            N  - number of bits, scalar (2,4,8,12,...)
        outputs:
            yq - digitized signal at N bits
        """
            #quantization
        # N = 4 # number of bits
        max_value = 2**(N-1) - 1
        yq = (ys*(max_value)).astype(np.int32)/(max_value)
        return yq

    return (quantization,)


@app.function
def clipping(y,miny=-5,maxy=5):
    """ clipping of signal 
    inputs: 
        y - signal [V] array of floats
        miny, maxy - lowest, highest values [V], scalar floats, default -5 ..+5 [Volt]
    outputs:
        y - clipped signal [V]
    better use: numpy.clip 
    """
    y[y < miny] = miny
    y[y > maxy] = maxy
    return y


@app.cell
def _(interp1d, np, quantization, sampling):
    def adc(t,y,fs=1.,N=4,miny=-5.,maxy=5.,method=None):
        """ A/D conversion
        Inputs:
            t - time [s] array of floats,
            y - signal [V] array of floats,
            fs - sampling frequency [Hz], scalar float,
            N - number of bits of the A/D converter, (2,4,8,12,14,...)
            miny, maxy - lowest, highest values [V], scalar floats, default -5 ..+5 [Volt]
            method - the reconstruction method: 'zoh' = zero-and-hold, 'soh' - sample and hold or None
        outputs:
            ts - sampled times [s]
            yq - sampled and digitized signal [V]
            yr - reconstructed, sample-and-hold signal [V]
        Usage:
            t = np.linspace(0,10, 10000)
            y = 5+np.sin(2*np.pi*1*t)
            ts,yq,yr = adc(t,y,fs=4,N=14,miny=0,maxy=10) # monopolar
            plt.figure()
            plt.plot(t,y,'k--',lw=0.1)
            plt.plot(ts,yq,'ro')
            plt.plot(t, yr,'b-')
        """
        # first sample
        ts,ys = sampling(t,y,fs)
        # clipping
        ys = clipping(ys,miny,maxy)
        # digitize
        yq = quantization(ys,N)
        # sample and hold reconstruction
        if method == 'soh':
            tr = t
            soh = interp1d(ts, yq, kind='zero', bounds_error=False,fill_value=yq[-1])
            yr = soh(tr)
        elif method == 'zoh':
            tr = t
            yr = np.zeros_like(tr)
            index = np.abs(np.subtract.outer(tr, ts)).argmin(0)
            yr[index] = yq
        elif method is None:
            tr = ts
            yr = yq
        else:
            raise(ValueError)
        
        return ts,yq,tr,yr

    return (adc,)


@app.cell
def _(adc, np, plt):
    # example
    t = np.linspace(0, 10, 10000)  # almost continuous
    y = 9 + np.sin(2 * np.pi * 0.1 * t)
    _ts, _yq, _tr, _yr = adc(t, y, fs=1, N=4, miny=0, maxy=10, method='soh')
    plt.figure()  # monopolar
    plt.plot(t, y, 'k--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-')
    return


@app.cell
def _(np):
    # an example from the A/D lecture
    t_1 = np.linspace(0, 1, 1000)  # almost continuous
    y_1 = 3 + 3 * np.sin(2 * np.pi * 10 * t_1)  # - np.pi/2.)
    return t_1, y_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### sample at 15 Hz
    """)
    return


@app.cell
def _(adc, plt, t_1, y_1):
    _ts, _yq, _tr, _yr = adc(t_1, y_1, fs=15.0, N=24, miny=0, maxy=10, method=None)
    plt.figure(figsize=(10, 8))
    plt.plot(t_1, y_1, 'm--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-')
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel('$y$ [V]', fontsize=18)
    plt.xlim([0, 1.0])
    plt.title('$f_s = 15 $ Hz ', fontsize=22)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### sample at 11 Hz
    """)
    return


@app.cell
def _(adc, plt, t_1, y_1):
    _ts, _yq, _tr, _yr = adc(t_1, y_1, fs=11.0, N=24, miny=0, maxy=10)
    plt.figure(figsize=(10, 8))
    plt.plot(t_1, y_1, 'k--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-', lw=0.5)
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel('$y$ [V]', fontsize=18)
    plt.xlim([0, 1.0])
    plt.title('$f_s = 11$ Hz', fontsize=22)
    return


@app.cell
def _(adc, plt, t_1, y_1):
    _ts, _yq, _tr, _yr = adc(t_1, y_1, fs=9.0, N=24, miny=0, maxy=10)
    plt.figure(figsize=(10, 8))
    plt.plot(t_1, y_1, 'k--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-', lw=0.5)
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel('$y$ [V]', fontsize=18)
    plt.xlim([0, 1.0])
    plt.title('$f_s = 9$ Hz', fontsize=22)
    return


@app.cell
def _(adc, plt, t_1, y_1):
    _ts, _yq, _tr, _yr = adc(t_1, y_1, fs=6.0, N=24, miny=0, maxy=10)
    plt.figure(figsize=(10, 8))
    plt.plot(t_1, y_1, 'k--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-', lw=0.5)
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel('$y$ [V]', fontsize=18)
    plt.xlim([0, 1.0])
    plt.title('$f_s = 6$ Hz', fontsize=22)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Estimate the aliasing using the folding diagram or the formula:
    if $f_s > 2 f$ , no aliasing

    if $2/3 f < f_s < 2 f$, $f_a = |f_s - f|$

    if $f_s < 2/3 f$, $f_a = (f/f_f)f_f$, where $f_f = f_s/2$

    in most cases:
        $$f_a = \left|f- f_s \cdot NINT (f/f_s) \right|$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### How do we use it? we use trial/error and smart guesses:

    let's check different options:

    if it's aliasing we could be in one of the two regions, either 6 Hz < 2/3 f, i.e. f > 1.5*6, f > 9 or

    it can be that 6Hz is above 2/3f and below 2f, i.e. f is between 3 and 9 Hz

    theoretically speaking if f is below 3Hz, then we're above the Nyquist frequency.

    So, we see 2 Hz (2 peaks in 1 second) so it can be that we sampled correctly using 6 Hz or incorrectly and got aliasing.

    Therefore we could test few things, but first let's prepare some options:

    1. if we are fine and 2Hz is there, so we just see not a nice sine signal and we can increase the sampling frequency and get it nice

    2. if we are aliasing, then it can be what? 2Hz = |f - 6Hz * NINT(f/6Hz)|, so f = 6Hz * NINT(f/6Hz) + 2Hz. Let's see if 10 Hz is reasonable: 10/6 = 1.6667 and the nearest integer is 2 and it means that 10 - 6*2 = 2 Hz.

    3. it can be also lower than 6Hz and we got 2Hz for instance if we sampled f = 4Hz
    """)
    return


@app.cell
def _(np):
    np.abs(10 - 6 * np.round(10./6.))
    return


@app.cell
def _(adc, plt, t_1, y_1):
    _ts, _yq, _tr, _yr = adc(t_1, y_1, fs=4.0, N=24, miny=0, maxy=10)
    plt.figure(figsize=(10, 8))
    plt.plot(t_1, y_1, 'k--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-', lw=0.5)
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel('$y$ [V]', fontsize=18)
    plt.xlim([0, 1.0])
    plt.title('$f_s = 4$ Hz', fontsize=22)
    return


if __name__ == "__main__":
    app.run()
