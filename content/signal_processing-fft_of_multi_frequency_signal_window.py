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
    ## FFT demo of a real, periodic signal
    a) naive way
    b) windowing with DC treatment
    """)
    return


@app.cell
def _():
    from matplotlib.pyplot import annotate, figure, grid, legend, plot, show, title, xlabel, xlim, ylabel
    from numpy import arange, ceil, cos, fix, loadtxt, log2, mean, pi, sin, sqrt, zeros
    from numpy.fft import fft

    # redefine default figure size and fonts
    import matplotlib as mpl
    # mpl.rc('text', usetex = True)
    mpl.rc('font', family = 'sans serif',size=16)
    mpl.rc('figure',figsize=(12,8))
    mpl.rc('lines', linewidth=1, color='lightblue',linestyle=':',marker='o')
    return (
        annotate,
        arange,
        ceil,
        cos,
        fft,
        figure,
        fix,
        grid,
        legend,
        loadtxt,
        log2,
        mean,
        pi,
        plot,
        show,
        sin,
        sqrt,
        title,
        xlabel,
        xlim,
        ylabel,
        zeros,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Given periodic signal, sampling frequency and total time
    """)
    return


@app.cell
def _(loadtxt):
    f_s = 100.0 # sampling frequency (Hz)
    T = 3.0 # total actual sample time (s)
    g = loadtxt('data/FFT_Example_data_with_window.txt')
    # first few values
    g[:5]
    return T, f_s, g


@app.cell
def _(T, arange, f_s, g, plot, show, title, xlabel, ylabel):
    # first, visualize the signal
    del_t = 1/f_s   # time resolution [s]
    t = arange(0.0,T+del_t,del_t)  # time, t (s)

    # plotSignal(t,g,f_s)
    plot(t,g,marker='o',markerfacecolor='b',linestyle=':',color='lightgrey')
    xlabel('$t$ (s)')
    ylabel('$g_i$ (V)')
    title('Periodic time signal sample')
    show()
    return (t,)


@app.cell
def _(g):
    # does it have a non-zero mean, DC value
    DC = g.mean()
    print ('DC = %f [V]' % DC)
    return (DC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Calculate the necessary parameters: $N, \Delta t, \Delta f, f_{fold},N_{freq}$
    """)
    return


@app.cell
def _(T, f_s):
    N = f_s * T  # number of data points
    del_t_1 = 1.0 / f_s  # time resolution (s)
    del_f = 1.0 / T  # frequency resolution(Hz)
    f_fold = f_s / 2.0  # folding frequency = Nyquist frequency of FFT (Hz)
    N_freq = int(N / 2.0)  # number of useful frequency points
    return N, N_freq, del_f, del_t_1, f_fold


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Frequency analysis using naive FFT
    """)
    return


@app.cell
def _(arange, del_f, f_fold, fft, g):
    frequency = arange(0,f_fold,del_f)  #frequency (Hz)
    G = fft(g) # FFT 
    print( G[:10])
    print( G.shape)
    return G, frequency


@app.cell
def _(
    G,
    N_freq,
    annotate,
    f_fold,
    figure,
    frequency,
    grid,
    plot,
    show,
    xlabel,
    xlim,
    ylabel,
):
    Magnitude = abs(G)/(N_freq)  # complex -> amplitude:  |F|/(N/2)

    figure()
    plot(frequency,Magnitude[:N_freq])
    grid('on')
    xlim([-.5,f_fold])
    xlabel('$f$ [Hz]')
    ylabel('$|F|$ [V]')
    annotate('DC', xy=(0,.9), xycoords='data',
                    xytext=(60, 60), textcoords='offset points',
                    size=20,
                    arrowprops=dict(arrowstyle="fancy",
                                    fc="0.6", ec="none",
                                    connectionstyle="angle3,angleA=0,angleB=90"),
                    )
    show()
    return (Magnitude,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Notes
    1. Note the value at 0 Hz, what can we learn from it (we saw it's about 0.45 Volt?
    2. What do we learn from about the frequencies? about 2.1V at 16 Hz and 0.7 Volt at 47 Hz?
    3. Let's remove DC first and see the result
    """)
    return


@app.cell
def _(DC, figure, g, legend, plot, t, xlabel, ylabel):
    figure()
    plot(t,g,t,g-DC,'ms')
    xlabel('$t$ [sec]')
    ylabel('$g$ [V]')
    legend(('original','DC removed'))
    return


@app.cell
def _(
    DC,
    Magnitude,
    N_freq,
    annotate,
    f_fold,
    fft,
    figure,
    frequency,
    g,
    grid,
    legend,
    plot,
    show,
    xlabel,
    xlim,
    ylabel,
):
    # repeat the frequency analysis
    G_1 = fft(g - DC)  # FFT of the signal without DC
    Magnitude1 = abs(G_1) / N_freq  # complex -> amplitude:  |F|/(N/2)
    figure()
    plot(frequency, Magnitude[:N_freq], frequency, Magnitude1[:N_freq], '--ms')
    annotate('DC', xy=(0, 0), xycoords='data', xytext=(60, 60), textcoords='offset points', size=20, arrowprops=dict(arrowstyle='fancy', fc='0.6', ec='none', connectionstyle='angle3,angleA=0,angleB=45'))
    grid('on')
    xlim([-0.5, f_fold])
    xlabel('$f$ [Hz]')
    ylabel('$|F|$ [V]')
    legend(('original', 'DC removed'))
    show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Let's use do it the right way:
    1. use 2^k number of points for faster FFT
    2. multiply the signal by a low-pass filter:
        * assure there is no aliasing
        * get read of the edges and make it less leaking
    """)
    return


@app.cell
def _(fft, g, zeros):
    # let's check how much we gain if we do it right size:
    fft(g)
    fft(g[:256])  # 256 points instead of 301, not waisting much data
    _g1 = zeros((512,))
    _g1[:301] = g.copy()
    # even if it's longer, but the right size with zeros at the end
    fft(_g1)
    return


@app.cell
def _(DC, N, arange, del_t_1, f_fold, f_s, fix, g, log2):
    N_2 = 2 ** fix(log2(N)).astype(int)
    T_2 = N_2 / f_s
    del_f_2 = 1 / T_2
    N_freq_2 = N_2 / 2
    t_2 = arange(0.0, T_2 + del_t_1, del_t_1)
    frequency_2 = arange(0, f_fold, del_f_2)
    len2, = t_2.shape
    _g_uncoupled_2 = g - DC
    return N_2, T_2, del_f_2, frequency_2, len2, t_2


@app.cell
def _(N_2):
    N_2
    return


@app.cell
def _(T_2, cos, figure, g, len2, mean, pi, plot, t_2):
    # create the low pass filter, called Hanning
    _u_Hann_2 = 0.5 * (1 - cos(2 * pi * t_2[:-1] / T_2))  #u_Hanning(t)
    _DC_2 = mean(g[:len2 - 1])  #DC = mean value of input signal (V) (average of all the useful data)
    _g_uncoupled_2 = g[:len2 - 1] - _DC_2  # uncoupled
    g_Hann_2 = _g_uncoupled_2 * _u_Hann_2
    figure()
    plot(_u_Hann_2, 'r--')
    plot(g_Hann_2, 'b-')
    plot(g, 'c:')
    return (g_Hann_2,)


@app.cell
def _(N_2, fft, g_Hann_2, sqrt):
    # take the FFT of the filtered, shorter signal
    G_Hann_2 = fft(g_Hann_2,N_2)  #G(omega) with Hanning window

    Magnitude_Hann_2 = abs(G_Hann_2)*sqrt(8./3.)/(N_2/2)  #|F|*sqrt(8/3)/(N/2)
    # Magnitude_Hann_2[0] = Magnitude_Hann_2[0]/2 + DC_2  #(also divide the first one by 2, and add back the DC value)

    # len_loc, = Magnitude_Hann_2.shape
    # A_2 = Magnitude_Hann_2[0:round(len_loc/2)]
    # Freq_2 = frequency_2[0:round(len_loc/2)]
    return (Magnitude_Hann_2,)


@app.cell
def _(
    Magnitude,
    Magnitude_Hann_2,
    figure,
    frequency,
    frequency_2,
    legend,
    plot,
    title,
    xlabel,
    ylabel,
):
    figure()
    plot(frequency,Magnitude[:frequency.shape[0]],'b:x')
    plot(frequency_2,Magnitude_Hann_2[:frequency_2.shape[0]], 'r-s')
    xlabel('frequency, (Hz)')
    ylabel('abs(F)')
    title('FFT Frequency Spectrum')
    legend(('Simple','Window + DC'))
    return


@app.cell
def _(del_f, del_f_2):
    # the frequency resolution is worse, but the result is better
    del_f, del_f_2
    return


@app.cell
def _(
    DC,
    N,
    N_2,
    T_2,
    arange,
    ceil,
    cos,
    del_t_1,
    f_fold,
    f_s,
    fft,
    figure,
    g,
    len2,
    log2,
    mean,
    pi,
    plot,
    sqrt,
    t_2,
    zeros,
):
    N_3 = 2 ** ceil(log2(N)).astype(int)
    T_3 = N_3 / f_s
    del_f_3 = 1 / T_3
    N_freq_3 = int(N_3 / 2)
    t_3 = arange(0.0, T_3 + del_t_1, del_t_1)
    frequency_3 = arange(0, f_fold, del_f_3)
    len3, = t_3.shape
    _g_uncoupled_2 = g - DC
    _u_Hann_2 = 0.5 * (1 - cos(2 * pi * t_2[:-1] / T_2))
    _DC_2 = mean(g[:int(len2 - 1)])
    _g_uncoupled_2 = g[:int(len2 - 1)] - _DC_2
    g_Hann_2_1 = _g_uncoupled_2 * _u_Hann_2
    g_Hann_3 = zeros((N_3,))
    g_Hann_3[:g_Hann_2_1.shape[0]] = g_Hann_2_1.copy()
    figure()
    plot(g_Hann_3, 'b-')
    G_Hann_3 = fft(g_Hann_3, N_3)
    Magnitude_Hann_3 = abs(G_Hann_3) * sqrt(8.0 / 3.0) / (N_2 / 2)
    len_loc, = Magnitude_Hann_3.shape
    A_3 = Magnitude_Hann_3[0:int(len_loc / 2)]
    Freq_3 = frequency_3[0:int(len_loc / 2)]
    return Magnitude_Hann_3, N_3, frequency_3


@app.cell
def _(N_3):
    N_3
    return


@app.cell
def _(
    Magnitude,
    Magnitude_Hann_2,
    Magnitude_Hann_3,
    figure,
    frequency,
    frequency_2,
    frequency_3,
    legend,
    plot,
    title,
    xlabel,
    ylabel,
):
    figure()
    plot(frequency,Magnitude[:frequency.shape[0]],'b:x')
    plot(frequency_2,Magnitude_Hann_2[:frequency_2.shape[0]], 'g--o')
    xlabel('frequency, (Hz)')
    plot(frequency_3,Magnitude_Hann_3[:frequency_3.shape[0]], 'r-s')
    xlabel('frequency, (Hz)')
    ylabel('abs(F)')
    title('FFT Frequency Spectrum')
    legend(('Simple','256', 'Window + DC'))
    return


@app.cell
def _(Magnitude_Hann_2, frequency_2, plot):
    f = frequency_2
    a = Magnitude_Hann_2[:f.shape[0]]
    plot(f,a)
    return a, f


@app.cell
def _(a, f):
    a1,f1 = a.max(),f[a.argmax()]
    print (a1,f1)
    return a1, f1


@app.cell
def _(a, f):
    b = a.copy()
    b[:a.argmax()+10] = 0 # remove the first peak
    a2,f2 = b.max(),f[b.argmax()]
    print( a2,f2)
    return a2, f2


@app.cell
def _(DC, T, a1, a2, arange, del_t_1, f1, f2, g, pi, plot, sin):
    t_1 = arange(0.0, T + del_t_1, del_t_1)
    _g1 = DC + a1 * sin(2 * pi * f1 * t_1) + a2 * sin(2 * pi * f2 * t_1)
    plot(t_1, g, 'b--', t_1, _g1, 'r-')
    return


if __name__ == "__main__":
    app.run()
