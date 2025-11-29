This example demonstrates two distinct approaches for measuring the volume of a cylinder, rigorously applying the principles of uncertainty analysis established by the Guide to the Expression of Uncertainty in Measurement (GUM). This process requires formulating the measurement model, evaluating all input standard uncertainties (Type A and Type B), propagating those uncertainties using sensitivity analysis, and reporting a final result with expanded uncertainty.

## Example: Volume Measurement Uncertainty Budget

The core measurement result format must be: Result = best estimate $\pm$ uncertainty (confidence level).

### Method A: Direct Geometric Measurement

This method calculates volume ($V$) based on measurements of the cylinder's diameter ($D$) and length ($L$) using high-precision dimensional instruments like a micrometer and caliper. The measurement model is an explicit measurement equation $Y=f(X_i)$.

#### Step 1: Formulation and Calculation of Best Estimate

The measurement model for the volume of a cylinder is:

$$V = f(D, L) = \frac{\pi}{4} D^2 L$$

**Assumed Values:**
*   $L = 150.00 \text{ mm}$
*   $D = 50.00 \text{ mm}$

**Best Estimate:**
$$V = \frac{\pi}{4} (50.00 \text{ mm})^2 (150.00 \text{ mm}) \approx 294,524.3 \text{ mm}^3$$

#### Step 2: Evaluating Standard Uncertainties ($u(x_i)$)

Input uncertainties are evaluated either statistically (Type A) or non-statistically (Type B). The standard deviation of the mean ($s_{\bar{x}} = s_x / \sqrt{N}$) is used for Type A components. Type B components often derive from rectangular distributions (e.g., resolution limits).

| Source | Type | Input Quantity ($X_i$) | Standard Uncertainty ($u(x_i)$) | Distribution |
| :--- | :--- | :--- | :--- | :--- |
| Length Repeatability | A | $u(L)_A$ | $0.015 \text{ mm}$ | Normal |
| Caliper Resolution | B | $u(L)_{B1}$ | $0.0029 \text{ mm}$ | Rectangular |
| Micrometer Resolution | B | $u(D)_{B1}$ | $0.00029 \text{ mm}$ | Rectangular |
| Calibration Bias ($k=2$) | B | $u(L)_{B2}, u(D)_{B2}$ | $0.005 \text{ mm}$ | Normal |

**Combined Standard Uncertainty for Inputs (RSS):**

$$u(L) = \sqrt{(0.015)^2 + (0.0029)^2 + (0.005)^2} \approx 0.016 \text{ mm}$$
$$u(D) = \sqrt{(0.00029)^2 + (0.005)^2} \approx 0.005 \text{ mm}$$

#### Step 3: Sensitivity Coefficients ($C_i$)

The sensitivity coefficients are the partial derivatives of the model:

$$C_L = \frac{\partial V}{\partial L} = \frac{\pi}{4} D^2 \approx 1963.5 \text{ mm}^2$$
$$C_D = \frac{\partial V}{\partial D} = \frac{\pi}{2} D L \approx 11,781.0 \text{ mm}^2$$

#### Step 4: Combining Standard Uncertainties ($u_c$)

Assuming the input errors ($D$ and $L$) are independent (uncorrelated), the combined standard uncertainty is calculated using the Root-Sum-Squares (RSS) method (Law of Propagation of Uncertainty, LPU):

$$u_c(V) = \sqrt{\left[C_L \cdot u(L)\right]^2 + \left[C_D \cdot u(D)\right]^2}$$
$$u_c(V) = \sqrt{\left(1963.5 \cdot 0.016\right)^2 + \left(11,781.0 \cdot 0.005\right)^2} \approx \sqrt{(31.4)^2 + (58.9)^2} \approx 66.8 \text{ mm}^3$$

| Input Variable | Uncertainty Contribution ($C_i \cdot u(x_i)$) ($\text{mm}^3$) | Contribution Squared ($\text{mm}^6$) |
| :--- | :--- | :--- |
| Length ($L$) | $31.4$ | $985.96$ |
| Diameter ($D$) | $58.9$ | $3469.21$ |
| **Combined** | **N/A** | $\mathbf{4455.17}$ |
| $u_c(V)$ | $66.8 \text{ mm}^3$ | N/A |

The dominant contributor to the volume uncertainty in this geometric method is the uncertainty in the Diameter ($D$), as evidenced by the significantly larger squared contribution term.

#### Step 5: Expanded Uncertainty and Reporting

The expanded uncertainty ($U$) is calculated using a coverage factor ($k$). Using $k=2$ provides a confidence level of approximately 95%.

$$U = k \cdot u_c(V) = 2 \cdot 66.8 \text{ mm}^3 \approx 134 \text{ mm}^3$$

**Reported Result (Method A):**
$$V = (294,524 \pm 134) \text{ mm}^3 \quad (k=2, 95\% \text{ confidence})$$

***

### Method B: Indirect Gravimetric Measurement (Archimedes)

This method relates the volume ($V$) to the measured mass ($m$) and known density ($\rho$) of the cylinder material. The fidelity of the final uncertainty statement depends entirely on establishing a complete measurement equation and meticulously evaluating the uncertainty of all input quantities.

#### Step 1: Formulation and Calculation of Best Estimate

The measurement model for volume is:

$$V = f(m, \rho) = \frac{m}{\rho}$$

**Assumed Values:**
*   $m = 1570.00 \text{ g}$
*   $\rho = 5.33 \text{ g/cm}^3$

**Best Estimate:**
$$V = \frac{1570.00}{5.33} \approx 294.55 \text{ cm}^3$$

#### Step 2: Evaluating Standard Uncertainties ($u(x_i)$)

| Source | Type | Input Quantity ($X_i$) | Standard Uncertainty ($u(x_i)$) | Distribution |
| :--- | :--- | :--- | :--- | :--- |
| Mass Repeatability | A | $u(m)_A$ | $0.020 \text{ g}$ | Normal |
| Balance Calibration | B | $u(m)_{B1}$ | $0.025 \text{ g}$ | Normal |
| Density Reference | B | $u(\rho)_{B1}$ | $0.0058 \text{ g/cm}^3$ | Rectangular |
| Thermal Expansion | B | $u(\rho)_{B2}$ | $0.0029 \text{ g/cm}^3$ | Rectangular |

**Combined Standard Uncertainty for Inputs (RSS):**
$$u(m) = \sqrt{(0.020)^2 + (0.025)^2} \approx 0.032 \text{ g}$$
$$u(\rho) = \sqrt{(0.0058)^2 + (0.0029)^2} \approx 0.0065 \text{ g/cm}^3$$

#### Step 3: Sensitivity Coefficients ($C_i$)

$$C_m = \frac{\partial V}{\partial m} = \frac{1}{\rho} \approx 0.1876 \text{ cm}^3/\text{g}$$
$$C_\rho = \frac{\partial V}{\partial \rho} = -\frac{m}{\rho^2} \approx -55.26 \text{ cm}^6/\text{g}^2$$

#### Step 4: Combining Standard Uncertainties ($u_c$)

$$u_c(V) = \sqrt{[C_m \cdot u(m)]^2 + [C_\rho \cdot u(\rho)]^2}$$
$$u_c(V) = \sqrt{(0.1876 \cdot 0.032)^2 + (-55.26 \cdot 0.0065)^2} \approx \sqrt{(0.0060)^2 + (-0.359)^2} \approx 0.359 \text{ cm}^3$$

| Input Variable | Uncertainty Contribution ($C_i \cdot u(x_i)$) ($\text{cm}^3$) | Contribution Squared ($\text{cm}^6$) |
| :--- | :--- | :--- |
| Mass ($m$) | $0.0060$ | $3.6 \times 10^{-5}$ |
| Density ($\rho$) | $-0.359$ | $0.12888$ |
| **Combined** | **N/A** | $\mathbf{0.128916}$ |
| $u_c(V)$ | $0.359 \text{ cm}^3$ | N/A |

#### Step 5: Expanded Uncertainty and Reporting

Using $k=2$ for approximately 95% confidence:

$$U = k \cdot u_c(V) = 2 \cdot 0.359 \text{ cm}^3 \approx 0.72 \text{ cm}^3$$

**Reported Result (Method B):**
$$V = (294.55 \pm 0.72) \text{ cm}^3 \quad (k=2, 95\% \text{ confidence})$$

### Method Comparison and Interpretation

By quantifying the specific contributions of each input quantity via sensitivity coefficients, the uncertainty budget functions as the definitive engineering tool for optimization.

1.  **Precision:** Converting Method B's uncertainty to $\text{mm}^3$ ($0.72 \text{ cm}^3 = 720 \text{ mm}^3$), we see that Method A ($U \approx 134 \text{ mm}^3$) is significantly more precise than Method B ($U \approx 720 \text{ mm}^3$) under these assumptions.
2.  **Dominant Errors:** In Method B, the density reference ($u(\rho)$) contributes overwhelmingly to the total uncertainty ($0.12888 \text{ cm}^6$) compared to the mass measurement ($3.6 \times 10^{-5} \text{ cm}^6$). To improve Method B, efforts must be focused on increasing the precision of the density value, not the precision of the mass balance.

Would you like to explore another metrological example, such as evaluating uncertainty for a thermocouple calibration system, or dive deeper into the use of tools like the NIST Uncertainty Machine (NUM) for Monte Carlo simulations?