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
    # Log decrement method
    based on lectures of Prof. Cimbala, ME341
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##  The log-decrement method
    The log-decrement is based on the following analysis:
        $$ \frac{q_o}{Kq_{is}} = 1-e^{-\zeta \omega_n t} \left[ \frac{1}{\sqrt{1-\zeta^2}}\sin\left(\omega_n t \sqrt{1-\zeta^2} + \sin^{-1} \left(\sqrt{1-\zeta^2} \right) \right) \right]$$

    and the damped natural frequency:
    $$\omega_d = \omega_n \sqrt{1-\zeta^2}$$

    Using the output of the system in time (step function response) we need to solve for $\omega_n$ and $\zeta$ simultaneously. The practical solution is the *log-decrement method*.

    When $\zeta \sim 0.1\div 0.3$, then the sine function is approximately $\pm 1$ and the magnitude only (peaks of the oscillating function) behave approximately as:

    $$ \left| \frac{q_o}{Kq_{is}} - 1 \right| \approx \left| -e^{-\zeta \omega_n t} \frac{1}{\sqrt{1-\zeta^2}} \right| $$

    Therefore we plot the normalized step founction output minus 1, obtain a function that oscillates around zero, and try to extract the peaks. We can use only positive peaks and mark them as $y^*_i, \quad i=1\dots n$ and their time instants, $t^*$. From these values we can obtain:

    1. The period of oscillations if we measure the time $t$ of $n$ cycles (e.g. $n=3$ in our example), $$ T = t/n $$

    2. If we define the $\log$ of the reduction of amplitude between each peak as $\delta$: $$ \ln \left(\frac{y^*_i}{y^*_{i+n}}\right) = n\delta$$, then the damping factor is recovered as: $$ \zeta = \frac{\delta}{\sqrt{(2\pi)^2+\delta^2}}$$ and the rest is straightforward: $$ \omega_d = \frac{2\pi}{T} = 2\pi f_d$$ and $$ \omega_n = 2\pi f_n = \frac{\omega_d}{\sqrt{1-\zeta^2}} $$
    """)
    return


@app.cell
def _():
    from IPython.core.display import Image 
    Image(filename='images/log-decrement.png',width=600)
    return


@app.cell
def _():
    from pylab import arange, array, asarray, isscalar, log, np, pi, plot, sqrt, title, xlabel, ylabel

    return (
        arange,
        array,
        asarray,
        isscalar,
        log,
        np,
        pi,
        plot,
        sqrt,
        title,
        xlabel,
        ylabel,
    )


@app.cell
def _(plot, title, xlabel, ylabel):
    from scipy import signal

    # Define transfer function
    k = 1 		# sensitivity
    wn = 546.72 # rad/s
    z=0.2     # damping

    sys = signal.lti(k*wn**2,[1,2*z*wn, wn**2])

    # step function output
    t,y = sys.step(N=1000)

    plot(t,y)
    title('Step response')
    xlabel('$t$ [sec]')
    ylabel('E [V]')
    return sys, t, y


@app.cell
def _():
    # note that sampling is sufficient, if not we need to apply the D/A reconstruction
    # or interpolations, which will add more noise and uncertainty to the system identification
    return


@app.cell
def _(plot, t, title, xlabel, y, ylabel):
    # plot the data as a decrement

    ts = t[::15]
    ys = y[::15]

    plot(ts,ys-1,'o')
    title('Step response')
    xlabel('$t$ [sec]')
    ylabel('E [V]')
    return ts, ys


@app.cell
def _(arange, array, asarray, isscalar, np, sys):
    # we will use the open source peakdetect function from 

    def peakdet(v, delta, x = None):
        """
        Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
        Returns two arrays
    
        function [maxtab, mintab]=peakdet(v, delta, x)
        # None
        # None
        # None
        # None
        # None
        # None
        # None
        # None
        # None
        # None
        # None
        # None
        # None
    
        # None
        # None
    
        """
        maxtab = []
        mintab = []
       
        if x is None:
            x = arange(len(v))
    
        v = asarray(v)
    
        if len(v) != len(x):
            sys.exit('Input vectors v and x must have same length')
    
        if not isscalar(delta):
            sys.exit('Input argument delta must be a scalar')
    
        if delta <= 0:
            sys.exit('Input argument delta must be positive')
    
        mn, mx = np.inf, -np.inf
        mnpos, mxpos = np.nan, np.nan

        lookformax = True
    
        for i in arange(len(v)):
            this = v[i]
            if this > mx:
                mx = this
                mxpos = x[i]
            if this < mn:
                mn = this
                mnpos = x[i]
        
            if lookformax:
                if this < mx-delta:
                    maxtab.append((mxpos, mx))
                    mn = this
                    mnpos = x[i]
                    lookformax = False
            else:
                if this > mn+delta:
                    mintab.append((mnpos, mn))
                    mx = this
                    mxpos = x[i]
                    lookformax = True

        return array(maxtab), array(mintab)

    # if __name__=="__main__":
    #     from matplotlib.pyplot import plot, scatter, show
    #     series = [0,0,0,2,0,0,0,-2,0,0,0,2,0,0,0,-2,0]
    #     maxtab, mintab = peakdet(series,.3)
    #     plot(series)
    #     scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
    #     scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
    #     show()
    return (peakdet,)


@app.cell
def _(peakdet, ts, ys):
    maxtab, mintab = peakdet(ys-1,.01,ts)
    return (maxtab,)


@app.cell
def _(maxtab):
    # we need only positive peaks, maxima:
    maxtab
    return


@app.cell
def _(maxtab, plot, title, ts, xlabel, ylabel, ys):
    # We see 4 peaks and therefore n = 4
    tstar = maxtab[:,0]
    ystar = maxtab[:,1]

    # plot the data with the peaks

    plot(ts,ys-1,'x',tstar,ystar,'ro',markersize=8)
    title('Step response')
    xlabel('$t$ [sec]')
    ylabel('E [V]')
    return tstar, ystar


@app.cell
def _(tstar):
    n = len(tstar)-1
    print("cycles = %d" % n)
    return (n,)


@app.cell
def _(n, tstar):
    T = (tstar[-1] - tstar[0])/(n)
    print ("period T= %4.3f sec" % T)
    return (T,)


@app.cell
def _(log, n, ystar):
    # delta 
    d = log(ystar[0]/ystar[-1])/(n)
    print ("delta = %4.3f " % d)
    return (d,)


@app.cell
def _(T, d, pi, sqrt):
    # recover the damping and the frequency:
    zeta= d/(sqrt((2*pi)**2 + d**2))
    omegad = 2*pi/T
    omegan = omegad/(sqrt(1-zeta**2))
    # output
    print ("natural frequency = %4.3f" % omegan)
    print ("damping factor = %4.3f" % zeta)
    print ("compare to the original: 546.72, 0.2")
    return


if __name__ == "__main__":
    app.run()
