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
    # 1st order dynamic system
    Following the example of Prof. Cimbala ME 345 course
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    mpl.rcParams['lines.linewidth']=2
    mpl.rcParams['lines.color']='r'
    mpl.rcParams['figure.figsize']=(10,12)
    mpl.rcParams['font.size']=14
    mpl.rcParams['axes.labelsize']=16
    return np, plt


@app.cell
def _(np):
    T = 1.
    t = np.arange(0,10*T,.0001)
    t_T = t/T

    # Step function

    # for a step function, take user input on final and initial values.
    y_i = 1.0
    y_f = 3.0

    y_step_norm =  (1 - np.exp(-t_T))
    y_step = (y_f-y_i)*y_step_norm + y_i
    return T, t, t_T, y_step, y_step_norm


@app.cell
def _(np, plt, t, t_T, y_step, y_step_norm):
    _fig, _ax = plt.subplots(nrows=2, sharex=True)
    _ax[0].plot(t, y_step)
    _ax[0].set_xlabel('$t$ (sec)')
    _ax[0].set_ylabel('$y_f$')
    _ax[1].plot(t_T, y_step_norm)
    _ax[1].plot(t_T, np.ones(t_T.shape), '--')
    _ax[1].set_xlabel('$t/\tau$ ')
    _ax[1].set_ylabel('$y_f/Ky_i$')
    return


@app.cell
def _(np, plt, t_T, y_step_norm):
    plt.figure(figsize=(6, 5))
    plt.plot(t_T, y_step_norm, lw=2)
    plt.xlim(0, 10)
    plt.ylim(0, 1.05)
    plt.plot(t_T, np.ones(t_T.shape))
    plt.ylabel('$\\frac{q_o}{Kq_{is}}$ ', fontsize=26)
    # plt.savefig('1st_order_step_response.png',dpi=200)
    plt.xlabel('$t/\\tau$', fontsize=26)
    return


@app.cell
def _(T, np, plt, t, t_T):
    y_i_ramp = 1.0
    A = 2.0
    y_ideal_ramp = A * t + y_i_ramp
    # determine actual ramp function. 
    y_ramp_norm = t - T * (1 - np.exp(-t_T))
    y_ramp = A * y_ramp_norm + y_i_ramp
    _fig, _ax = plt.subplots(nrows=2, sharex=True)
    _ax[0].plot(t, y_ideal_ramp, 'k', t, y_ramp, 'r')
    _ax[0].set_xlabel('$t$ (s)')
    # figure(figsize=(10,8))
    _ax[0].set_ylabel('$y$')
    _ax[1].plot(t_T, y_ramp_norm, 'r', t_T, t, 'k')
    _ax[1].set_xlabel('$\\hat{t}$ ')
    _ax[1].set_ylabel('$\\hat{y}$')
    return


@app.cell
def _(T, np, t_T):
    y_i_impulse = 0.;
    y_f_impulse = 5.;

    y_impulse_norm = (1./T)*np.exp(-t_T);
    y_impulse = y_impulse_norm * (y_f_impulse-y_i_impulse) + y_i_impulse;
    return y_f_impulse, y_i_impulse, y_impulse, y_impulse_norm


@app.cell
def _(T, plt, t, t_T, y_f_impulse, y_i_impulse, y_impulse, y_impulse_norm):
    _fig, _ax = plt.subplots(nrows=2, sharex=True)
    # figure(figsize=(10,8))
    _ax[0].plot(t_T, y_impulse_norm)
    _ax[0].set_xlabel('$t$ (s)')
    _ax[0].set_ylabel('$y$')
    _ax[1].plot(t, y_impulse, 'r', [0.0, 0.0], [y_i_impulse, y_f_impulse], 'k')
    _ax[1].set_xlim([-T, 10 * T])
    _ax[1].set_xlabel('$\\hat{t}$ ')
    _ax[1].set_ylabel('$\\hat{y}$')
    return


if __name__ == "__main__":
    app.run()
