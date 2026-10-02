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
    # Micrometer calibration using gage block
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. A Federal Grade 2 accuracy gage block  is used to calibrate the measurements of a micrometer. A gage block is a calibration standard for thickness measurement, it is a block of material, steel in this case, machined to a very high accuracy of thickness.

    2. A Federal Grade 2 accuracy gage block is used, it meets certain tolerances for length, flatness and parallelism. Read more on https://www.nist.gov/system/files/documents/calibrations/mono180.pdf

    3. The calibrated accuracy of the micrometer can be no greater than the total error of this standard accuracy.

    4. The total error $e_{\text{calibration}}$ from the calibration will be the root sum of the squares (RSS) of the bias and precision errors.
    """)
    return


@app.cell
def _():
    from IPython.display import Image
    # Image('https://www.higherprecision.com/images/blog_images/higherprecision_gageblocks.jpg',width=500)
    return (Image,)


@app.cell
def _(Image):
    Image(url='https://cdn.mscdirect.com/global/media/images/tech-essentials/outside-micrometer.jpg')
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### We performed multiple measurements and checked that the histogram is close to normal distribution
    """)
    return


@app.cell
def _(Image):
    Image(url='https://www.mathsisfun.com/data/images/histogram.gif')
    return


@app.cell
def _():
    N = 40 # 40 measurements
    mean_x = 0.12621 # inch
    s_x = 0.000146317 # inch
    t_39_95 = 2.02268893 # t-statistic for N-1 degrees of freedom
    true_x = 0.12620 # inch - true value for calibration
    return N, mean_x, s_x, t_39_95, true_x


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ e_{\text{bias}} = | \overline{x} - x_{\text{true}} | $$
    """)
    return


@app.cell
def _(mean_x, np, true_x):
    # bias error
    e_bias  = np.abs(mean_x - true_x)
    print(f"Bias error = {e_bias:g} inch")
    return (e_bias,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $e_{p} = t_{39,95\%} \frac{S_x}{\sqrt{N}}$
    """)
    return


@app.cell
def _(N, np, s_x, t_39_95):
    # precision error
    e_precision = t_39_95*s_x/np.sqrt(N)
    print(f"Precision error = {e_precision:g} inch")
    return (e_precision,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ e_{\text{resolution}} = \frac{1}{2} \text{resolution} $$
    """)
    return


@app.cell
def _():
    # micrometer resolution
    resolution = 0.00005 # inch

    e_resolution = resolution/2
    print(f"Resolution error = {e_resolution:g} inch")
    return (e_resolution,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Standard gage blocks are not ideal, they have known tolerances and errors

    $$ e_{\text{standard, total}} = \sqrt{e_{\text{standard},L}^2 + e_{\text{standard},\perp}^2 e_{\text{standard},\parallel}^2 } $$
    """)
    return


@app.cell
def _(np):
    # Manufacturer supplied information about the gage 
    # accuracy. We have chosen only grade 2 accuracy ( higher more expensive )
    e_standard_length = 4e-6 # inch
    e_standard_flattness = 4e-6 # inch
    e_standard_parallelism = 4e-6 # inch
    e_standard_total = np.sqrt(e_standard_length**2  + e_standard_flattness**2 + e_standard_parallelism**2)
    print(f"standard gage grade 2 error = {e_standard_total:g} inch")
    return (e_standard_total,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ \large{e_{\text{calibration, total}} = \sqrt{e_{\text{bias}}^2 + e_{\text{precision}}^2 + e_{\text{standard, total}}^2 + e_{\text{resolution}}^2 } }$$
    """)
    return


@app.cell
def _(e_bias, e_precision, e_resolution, e_standard_total, np):
    # note that even if we'd use an ideal measurement system with e = 0
    # we will never get the true value as there uncertainty of the standard gage block itself

    # note that standard gage block uncertainty is smaller than other values
    # otherwise you need to choose a better grade of the gage block

    e_calibration_total = np.sqrt(e_bias**2 + e_precision**2 + e_standard_total**2 + e_resolution**2)
    return (e_calibration_total,)


@app.cell
def _(e_calibration_total):
    print(f"Calibration error = {e_calibration_total:g} inch")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Accuracy is mesured relative to the true value

    $$ \text{accuracy} = 1 - \frac{e_{\text{calibration,total}}}{x_{\text{true}} }   \times 100\% $$
    """)
    return


@app.cell
def _(e_calibration_total, true_x):
    # our accuracy measure is 
    accuracy = (1 - e_calibration_total/true_x)
    print(f"Accuracy (relative) = {accuracy*100:.3f} %")
    return


@app.cell
def _():
    # from this moment and on we can use the micrometer, but we have to use its # calibration error as a bias error for all the measurements
    # remember that it already includes the resolution error, so don't repeat it.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Second half: use the calibrated micrometer to measure the diameter of a cylinder
    """)
    return


@app.cell
def _(Image):
    Image(url='https://static1.bigstockphoto.com/8/3/3/large2/338282026.jpg')
    return


@app.cell
def _():
    d_mean = 0.32512  # inch
    N_1 = 40
    s_d = 0.0003  # inch
    from scipy.stats import t as student_t
    confidence_level = 0.95
    # for the 95 confidence level
    alpha = 1 - confidence_level  # 95%
    degrees_of_freedom = N_1 - 1
    t_value = student_t.ppf(1 - alpha / 2.0, degrees_of_freedom)
    print(f't value = {t_value}')
    return N_1, s_d, t_value


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Confidence interval of the diameter measurement is:

    $$ e_{d,\,\text{cylinder}} = \sqrt{e_{\text{calibration, total}}^2 + \left(t_{39,95\%} \frac{S_x}{\sqrt{N}} \right)^2 } $$
    """)
    return


@app.cell
def _(N_1, e_calibration_total, np, s_d, t_value):
    e_cylinder = np.sqrt(e_calibration_total ** 2 + t_value * s_d / np.sqrt(N_1))
    print(f'e_cylinder = {e_cylinder:g} inch with 95% probability')
    return (e_cylinder,)


@app.cell
def _(e_cylinder):
    e_cylinder/2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cylinder diameter is

    $$ d_{\text{cylinder}} = 0.325 \pm 0.00489 \;\text{inch} $$
    """)
    return


if __name__ == "__main__":
    app.run()
