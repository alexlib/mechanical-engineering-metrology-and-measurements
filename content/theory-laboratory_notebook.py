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
    # Laboratory Notebook
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It is strongly recommended to keep a good laboratory notebook for the course. Please consult a couple of sources on the meaning, importance, requirements, tips and tricks of keeping a notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. [MIT](https://web.mit.edu/me-ugoffice/communication/labnotebooks.pdf)
    2. [Science buddies](https://www.sciencebuddies.org/science-fair-projects/science-fair/laboratory-notebooks-stem)
    3. [University of British Columbia](https://phas.ubc.ca/~phys259/2012-13Term1/pickyTA_ENPH259example.htm)
    4. [Wikipedia](https://phas.ubc.ca/~phys259/2012-13Term1/pickyTA_ENPH259example.htm)
    5. [Marie Sklodowska Curie notebook](https://twitter.com/NobelPrize/status/1589638816310050816/photo/1)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
