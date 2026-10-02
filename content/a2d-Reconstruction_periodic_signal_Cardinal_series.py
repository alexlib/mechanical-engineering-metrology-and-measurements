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
    # Analog to digital (A/D) and Digital to Analog (d/A) conversion example
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    def reconstruct_with_sinc(ts,fd,t): 
        n, = ts.shape 
        dt = ts[1] - ts[0] 
        fr = [] 
        for k,ti in enumerate(t): 
            # for each time point 
            sumf = 0.0 
            for i in range(n): 
            # for each point in a sampled set 
                sumf += fd[i]*np.sin(np.pi*(ti/dt-i))/(ti/dt-i) 
        
            fr.append((1./np.pi)*sumf) 
        
        return np.asarray(fr)

    return np, plt, reconstruct_with_sinc


@app.cell
def _(np):
    t = np.arange(0.0,0.6,0.001) 
    fa = 1.0*np.sin(2*np.pi*10*t)+0.2*np.sin(2*np.pi*6*t) 
    fs = 30 # Hz 
    ts = np.arange(0.0,0.6,1./fs) # sampling time 
    fd = 1.0*np.sin(2*np.pi*10*ts)+0.2*np.sin(2*np.pi*6*ts) # sampled data
    return fa, fd, t, ts


@app.cell
def _(fa, fd, plt, t, ts):
    plt.figure(figsize=(10,8)) 
    plt.plot(ts,fd,':ro',markersize=10)
    plt.plot(t,fa,'c--',linewidth=0.2)
    plt.xlabel('$t$ [sec]',fontsize=16) 
    plt.ylabel('$y$ [V]',fontsize=16) 
    plt.legend(('Original','Sampled'))
    return


@app.cell
def _(fd, reconstruct_with_sinc, t, ts):
    fr = reconstruct_with_sinc(ts,fd,t)
    return (fr,)


@app.cell
def _(fa, fd, fr, plt, t, ts):
    plt.figure(figsize=(10,8)) 
    plt.plot(t,fa,'c--',ts,fd,'ro',t,fr,'r-')
    plt.xlabel('$t$ [sec]',fontsize=16) 
    plt.ylabel('$y$ [V]',fontsize=16) 
    plt.legend(('Original','Sampled','Reconstructed'))
    return


if __name__ == "__main__":
    app.run()
