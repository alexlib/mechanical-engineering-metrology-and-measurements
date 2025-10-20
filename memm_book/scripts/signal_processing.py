from scipy import fft
import numpy as np
import matplotlib.pyplot as plt
# redefine default figure size and fonts
import matplotlib as mpl
mpl.rc('font', size=14)
mpl.rc('figure', figsize=(12, 10))


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
    frq = frq[range(np.int(n/2))]  # one side frequency range
    Y = 2*fft.fft(y)/n  # fft computing and normalization
    Y = Y[range(np.int(n/2))]
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
