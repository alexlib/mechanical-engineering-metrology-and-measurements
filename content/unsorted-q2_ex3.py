import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as pl

    return np, pl


@app.cell
def _(np):
    data = np.loadtxt('data/sizedistribution.dat');
    vals = data[:,1]
    num = data[:,0]
    return num, vals


@app.cell
def _(num, pl, vals):
    pl.plot(num,vals)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Isn't it clear that the plot is not like "random variable" ?
    """)
    return
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise: Question 2, Example 3
    """)
    return




@app.cell
def _(pl, vals):
    pl.hist(vals,21)
    return


@app.cell
def _(np, pl, vals):
    pl.hist(np.log(vals),21)
    return


@app.cell
def _(np, vals):
    newvals = np.log(vals)
    return (newvals,)


@app.cell
def _(newvals, num, pl):
    pl.plot(num,newvals)
    return


@app.cell
def _(newvals, np, vals):
    print("Wrong:")
    print ("Average =  %.3f" %np.mean(vals))
    print ("Standard Deviation = %.3f" %np.std(vals))

    print ("Correct:")
    print ("Average =  %.3f" % np.exp(np.mean(newvals)))
    print ("Standard Deviation = %.3f" % np.exp(np.std(newvals,ddof=1)))
    return


@app.cell
def _(newvals):
    from scipy.stats import lognorm, norm
    param = norm.fit(newvals)
    return norm, param


@app.cell
def _(newvals, norm, np, param):
    x = np.linspace(np.min(newvals),np.max(newvals),100)
    # fitted distribution
    pdf_fitted = norm.pdf(x,loc=param[0],scale=param[1])
    return pdf_fitted, x


@app.cell
def _(newvals, pdf_fitted, pl, x):
    pl.figure()
    pl.plot(x,pdf_fitted,'r-')
    pl.hist(newvals,density=1,alpha=.3)
    return


@app.cell
def _(np, param):
    print(param) # log normal
    print(np.exp(param))
    return


if __name__ == "__main__":
    app.run()
