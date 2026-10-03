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
 
    """)
    return
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Cylinder Volume: Nominal Values and Uncertainty
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Problem Statement: Volume of a Cylinder

    This example follows the video tutorial on YouTube: [Uncertainty Propagation Example: Volume of a Cylinder by Dr. Joshua Paul Steimel](https://www.youtube.com/watch?v=NHSOMNM6Wqk).

    A tube of circular cross-section has a **nominal length ($L$) of $50 \text{ m} \pm 0.5 \text{ m}$** and a **radius ($R$) of $15 \text{ m} \pm 0.1 \text{ m}$**. Determine the total uncertainty in the volume.

    ### 1.1 Given Nominal Values (Mean Values)

    The nominal values (mean values, denoted $\bar{R}$ and $\bar{L}$ in standard notation, or $r$ and $l$ in the equations) are:

    $$r = 15 \text{ m}$$
    $$l = 50 \text{ m}$$

    ### 1.2 Given Uncertainties ($\mu$ or $u$)

    The stated $\pm$ values are the **Bias Uncertainties** (or standard uncertainty $u$ if a coverage factor is not explicitly used, as is often the case in this type of problem, represented as $u_r$ and $u_l$):

    $$u_r = 0.1 \text{ m}$$
    $$u_l = 0.5 \text{ m}$$

    ### 1.3 Total Uncertainty Equation

    The total uncertainty ($\omega_V$) is the root sum of the squares of the Bias Uncertainty ($B_V$) and the Precision Uncertainty ($P_V$):

    $$\omega_V = \sqrt{B_V^2 + P_V^2}$$

    As explained in the video (0:09, 2:35), since there is no information given about the number of samples or standard deviation, the **Precision Uncertainty ($P_V$) is zero**.

    Therefore, the **Total Uncertainty ($\omega_V$) is equal to the Bias Uncertainty ($B_V$)**:

    $$\omega_V = B_V$$

    ## 2. Methodology: Uncertainty Propagation (Bias Error $B_V$)

    The Volume ($V$) of the cylinder is a function of two independent variables, radius ($r$) and length ($l$).

    $$V(r, l) = \pi r^2 l$$

    The Bias Uncertainty ($B_V$) is calculated using the standard method for uncorrelated variables:

    $$B_V = \sqrt{\left(\frac{\partial V}{\partial r} u_r\right)^2 + \left(\frac{\partial V}{\partial l} u_l\right)^2}$$

    ### 2.1 Calculate Partial Derivatives (Sensitivity Coefficients)

    We first calculate the partial derivatives of the volume equation with respect to each independent variable. These are the **sensitivity coefficients** ($c_i$):

    1.  **Sensitivity with respect to Radius ($c_r$):**
        $$c_r = \frac{\partial V}{\partial r} = \frac{\partial}{\partial r}(\pi r^2 l) = 2 \pi r l$$

    2.  **Sensitivity with respect to Length ($c_l$):**
        $$c_l = \frac{\partial V}{\partial l} = \frac{\partial}{\partial l}(\pi r^2 l) = \pi r^2$$

    ### 2.2 Numerical Calculations for Total Uncertainty ($B_V$)

    Now, we plug the nominal/mean values ($\bar{r}=15 \text{ m}$, $\bar{l}=50 \text{ m}$) into the partial derivatives to find the numerical sensitivity coefficients, and then calculate the total uncertainty $B_V$.

    ```python
    import numpy as np

    # Nominal (Mean) Values
    r = 15.0  # meters
    l = 50.0  # meters

    # Uncertainties (u_i or mu_i)
    u_r = 0.1  # meters
    u_l = 0.5  # meters
    pi = np.pi

    # 1. Calculate Nominal Volume (V)
    V = pi * r**2 * l
    print(f"Nominal Volume (V): {V:.3f} m^3")

    # 2. Calculate Sensitivity Coefficients (c_r, c_l)
    c_r = 2 * pi * r * l
    c_l = pi * r**2

    # 3. Calculate Squared Uncertainty Contributions (c_i * u_i)^2
    term_r_squared = (c_r * u_r)**2
    term_l_squared = (c_l * u_l)**2

    # 4. Calculate Bias Uncertainty (B_V)
    B_V = np.sqrt(term_r_squared + term_l_squared)

    print(f"\nSensitivity Coefficient for Radius (c_r = 2πrl): {c_r:.3f}")
    print(f"Sensitivity Coefficient for Length (c_l = πr²): {c_l:.3f}")
    print(f"\nBias Uncertainty (B_V) in Volume: {B_V:.3f} m^3")
    ```

    The calculated **Bias Uncertainty ($B_V$) is approximately $589.845 \text{ m}^3$**, which is the **Total Uncertainty** ($\omega_V$) for this problem.

    ## 3. Alternative Method: Fractional (Relative) Uncertainty

    The video also suggests calculating the fractional uncertainty ($\frac{B_V}{V}$) first, as it helps with units consistency (7:11). The result is a unitless fraction (or percentage).

    The fractional uncertainty equation is:
    $$\frac{B_V}{V} = \sqrt{\left(\frac{1}{V} \frac{\partial V}{\partial r} u_r\right)^2 + \left(\frac{1}{V} \frac{\partial V}{\partial l} u_l\right)^2}$$

    ### 3.1 Simplified Fractional Terms

    By dividing the partial derivatives by the volume formula $V = \pi r^2 l$, the terms simplify significantly:

    1.  **Fractional Sensitivity for Radius:**
        $$\frac{1}{V} \frac{\partial V}{\partial r} = \frac{2 \pi r l}{\pi r^2 l} = \frac{2}{r}$$

    2.  **Fractional Sensitivity for Length:**
        $$\frac{1}{V} \frac{\partial V}{\partial l} = \frac{\pi r^2}{\pi r^2 l} = \frac{1}{l}$$

    ### 3.2 Numerical Calculation of Fractional Uncertainty

    The new unitless formula is:
    $$\frac{B_V}{V} = \sqrt{\left(\frac{2}{r} u_r\right)^2 + \left(\frac{1}{l} u_l\right)^2}$$

    ```python
    # 1. Calculate Fractional Uncertainty (Unitless)
    frac_r_squared = (2 * u_r / r)**2
    frac_l_squared = (u_l / l)**2

    frac_B_V = np.sqrt(frac_r_squared + frac_l_squared)

    print(f"Fractional Uncertainty (B_V/V): {frac_B_V:.6f}")

    # 2. Check: Reconvert to absolute uncertainty (B_V = V * (B_V/V))
    B_V_check = V * frac_B_V

    print(f"Absolute Uncertainty Check (V * (B_V/V)): {B_V_check:.3f} m^3")
    ```

    The fractional uncertainty is approximately $0.016667$, or $1.67\%$. Multiplying this by the Nominal Volume ($35342.9 \text{ m}^3$) yields $589.048 \text{ m}^3$, confirming the result from the direct calculation method.

    ## 4. Final Uncertainty Budget Summary

    | Quantity | Nominal Value | Uncertainty ($\mu_i$ or $u_i$) | Sensitivity Coeff. ($c_i$) | Uncertainty Contrib. ($c_i u_i$) | Squared Contrib. ($c_i u_i$)^2 |
    | :--- | :---: | :---: | :---: | :---: | :---: |
    | Radius ($r$) | $15.0 \text{ m}$ | $0.1 \text{ m}$ | $1500 \pi$ | $150 \pi$ | $22500 \pi^2$ |
    | Length ($l$) | $50.0 \text{ m}$ | $0.5 \text{ m}$ | $225 \pi$ | $112.5 \pi$ | $12656.25 \pi^2$ |
    | **Volume ($V$)**| **$35342.9 \text{ m}^3$**| **$589.845 \text{ m}^3$**| **-** | **-** | **$35156.25 \pi^2$**|

    The total uncertainty in the volume of the cylinder is:

    $$V = (35342.9 \pm 589.8) \text{ m}^3$$

    or in fractional terms:

    $$V = 35342.9 \text{ m}^3 \pm 1.67\%$$
    """)
    return


if __name__ == "__main__":
    app.run()
