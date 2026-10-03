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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _():
    def clipping(y,miny=-5,maxy=5):
        """ clipping of signal
        inputs:
            y - signal [V] array of floats
            miny, maxy - lowest, highest values [V], scalar floats, default -5 ..+5 [Volt]
        outputs:
            y - clipped signal [V]
        better use: numpy.clip
        """
        y = y.copy()
        y[y < miny] = miny
        y[y > maxy] = maxy
        return y

    return (clipping,)


@app.cell(hide_code=True)
def _(clipping, interp1d, np, quantization, sampling):
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


@app.cell(hide_code=True)
def _(adc, np, plt):
    # example
    t = np.linspace(0, 10, 10000)  # almost continuous
    y = 9 + np.sin(2 * np.pi * 0.1 * t)
    _ts, _yq, _tr, _yr = adc(t, y, fs=1, N=4, miny=0, maxy=10, method='soh')
    plt.figure(figsize=(5.1, 3.3))  # monopolar
    plt.plot(t, y, 'k--', lw=0.1)
    plt.plot(_ts, _yq, 'ro')
    plt.plot(_tr, _yr, 'b-')
    return


@app.cell(hide_code=True)
def _(np):
    # an example from the A/D lecture
    t_1 = np.linspace(0, 1, 1000)  # almost continuous
    y_1 = 3 + 3 * np.sin(2 * np.pi * 10 * t_1)  # - np.pi/2.)
    return t_1, y_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interactive: pick a sampling frequency

    The dense signal above is $y = 3 + 3\sin(2\pi \cdot 10 t)$ — a 10 Hz tone.
    Pick $f_s$ below. Red dots are the samples; the blue line joins them, so you see
    the (possibly aliased) frequency the digital system believes in. Nyquist says
    $f_s > 2f = 20$ Hz keeps the true 10 Hz.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    fs_choice = mo.ui.dropdown(
        options=["4 Hz", "6 Hz", "9 Hz", "11 Hz", "15 Hz", "30 Hz (no aliasing)"],
        value="15 Hz",
        label="Sampling frequency $f_s$",
    )
    fs_choice
    return (fs_choice,)


@app.cell(hide_code=True)
def _(adc, fs_choice, mo, np, plt, t_1, y_1):
    # fs_choice.value is the selected label ("15 Hz"); the number leads it.
    _fs = float(str(fs_choice.value).split()[0])
    _f = 10.0
    _fa = abs(_f - _fs * round(_f / _fs))
    _ts, _yq, _tr, _yr = adc(t_1, y_1, fs=_fs, N=24, miny=0, maxy=10, method=None)
    _fig, _ax = plt.subplots(figsize=(5.1, 3.3))
    _ax.plot(t_1, y_1, "k--", lw=0.5, label="true 10 Hz tone")
    _ax.plot(_ts, _yq, "ro", markersize=5, label="samples")
    _ax.plot(_tr, _yr, "b-", lw=1.0, label=f"seen at {_fa:.0f} Hz")
    _ax.set_xlabel("$t$ [s]", fontsize=12)
    _ax.set_ylabel("$y$ [V]", fontsize=12)
    _ax.set_xlim([0, 1.0])
    if _fa == _f:
        _ax.set_title(f"$f_s = {_fs:.0f}$ Hz — no aliasing, true 10 Hz kept", fontsize=12)
    else:
        _ax.set_title(f"$f_s = {_fs:.0f}$ Hz — aliased: 10 Hz appears as {_fa:.0f} Hz", fontsize=12)
    _ax.legend(fontsize=9, loc="upper right")
    _ax.grid(alpha=0.3)
    _fig
    return


@app.cell(hide_code=True)
def _(fs_choice, mo, np):
    _fs = float(str(fs_choice.value).split()[0])
    _fa = abs(10.0 - _fs * round(10.0 / _fs))
    if _fa == 10.0:
        _msg = f"At $f_s = {_fs:.0f}$ Hz you are above Nyquist ($> 20$ Hz): $f_a = {_fa:.0f}$ Hz — the true tone survives."
    else:
        _msg = f"At $f_s = {_fs:.0f}$ Hz: $f_a = |10 - {_fs:.0f} \\times \\mathrm{{NINT}}(10/{_fs:.0f})| = {_fa:.0f}$ Hz — aliasing. Try 30 Hz to fix it, or 4 Hz to see the $2$ Hz twin of the $6$ Hz case."
    mo.md(_msg)
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


if __name__ == "__main__":
    app.run()
