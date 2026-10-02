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
    # Self-training exercises
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Question 1

    In our laboratory you will not use the **distance** measurements. There is a tool for this, called **linear variable differential transformer (LVDT)**.

    1. Read and summarize the principle of action of LVDT
    2. An engineer wants to calibrate the LVDT tool, using micrometer. The system looks like this:
    """)
    return


@app.cell
def _():
    from IPython.display import Image
    Image('images/lvdt.png',width=600)
    return (Image,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Please, describe the system according to the general system scheme:
    - what is the sensor in Figure 1.12?
    - what is the signal of the sensor output ?
    - what is the transducer?
    - what is the signal after transducer?
    - what kind of signal conditioning the LVDT does?
    - what kind of output there is after the system?
    - is there a feedback?
    """)
    return


@app.cell
def _(Image):
    Image('images/generalized_measurement_system.png',width=600)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Question 2

    **Calibration and regression**

    Each group runs the notebook to get their own original set of data in terms of two arrays (at least 5-6 samples long): concentration $c$ (in particles per million, ppm) versus transmissivity $T$ (in percents, 100% is completely transparent, i.e. clear water): [LINK](unsorted-random_data_for_hw_1.md) (** use Cell -> Run All **)

    1. This is a calibration data, the process temperature depends on the concentration. Plot the data $c = f(T)$
    1. Find the sensitivity, the input range, the output range (full scale output) and the relevant errors.
    1. Find out what would be the concentration if in the experiment we measure $T = 35.6\%$
    """)
    return


if __name__ == "__main__":
    app.run()
