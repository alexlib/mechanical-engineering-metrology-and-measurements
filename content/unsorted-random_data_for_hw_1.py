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
    # Run the random data generator and plot the scatter
    """)
    return


@app.cell
def _():
    from random import random as _random

    def create_random_set(N=6):
        """ creates _random data set of concentration versus temperature """
        c = []
        w = []
        T = []
        k = _random()*0.05
        b = _random()*0.002

        for i in range(N):
            c.append(_random()*55)
            w.append(_random()*10)

        c.sort()

        T = []
        for i in range(N):
            T.append(100*10**(-(c[i]*k + b))+ w[i])


        return c,T

    return (create_random_set,)


@app.cell
def _(create_random_set):
    from random import randint
    c, T = create_random_set(randint(5,20))
    print('\n'.join('{0:.3f} {1:.3f}'.format(*k) for k in zip(c,T)))
    return T, c


@app.cell
def _(T, c):
    import matplotlib.pyplot as plt
    plt.plot(c,T,'o',markersize=10)
    plt.xlabel('c',fontsize=14)
    plt.ylabel('T',fontsize=14)
    return


if __name__ == "__main__":
    app.run()
