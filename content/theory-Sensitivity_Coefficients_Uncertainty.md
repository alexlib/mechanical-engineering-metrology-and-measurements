# Sensitivity Coefficients in Uncertainty Budgets

_Source: [engineering.com](https://www.engineering.com/sensitivity-coefficients-in-uncertainty-budgets/)_

## What Are Sensitivity Coefficients?

Sensitivity coefficients quantify how much a change in an input variable affects the output of a measurement. They are crucial for calculating combined uncertainty when multiple sources of error are present.

> **In other words:**  
> Sensitivity coefficients act as multipliers for each uncertainty source, showing how much each source contributes to the final uncertainty.

---

## Why Are Sensitivity Coefficients Important?

When combining uncertainties from different sources, simply adding them is not enough. Each source may affect the result differently, depending on the measurement equation. Sensitivity coefficients ensure that each uncertainty is weighted correctly.

**Example:**  
If you measure a length directly, the uncertainty in your ruler is applied directly ($c = 1$).  
If you calculate an area ($A = l \times w$), the uncertainty in each dimension is scaled by how much it affects the area.

---

## Direct Measurements: Sensitivity Coefficient = 1

For a simple sum:

$$
Y = y + x_1 + x_2 + x_3
$$

Each error source ($x_i$) affects $Y$ directly, so $c_i = 1$.

Combined uncertainty:

$$
U_C = \sqrt{\sum_{i=1}^{n} c_i^2 u_i^2}
$$

---

## When Sensitivity Coefficients Vary

For more complex equations, the effect of each input is not always direct. Sensitivity coefficients are found by taking the partial derivative of the output with respect to each input.

### Example: Building Height Measurement

![Measuring building height using clinometer and tape measure](https://res.cloudinary.com/engineering-com/image/upload/w_640,h_640,c_limit,q_auto,f_auto/Sensitivity_4_y3whmc.jpg){ height=300px }

The height is calculated as:

$$
H = h_1 + L \cdot \tan(\theta)
$$

- $h_1$ = height of clinometer
- $L$ = horizontal distance
- $\theta$ = measured angle

**Sensitivity coefficients:**

- For $h_1$: $\frac{\partial H}{\partial h_1} = 1$
- For $L$: $\frac{\partial H}{\partial L} = \tan(\theta)$
- For $\theta$: $\frac{\partial H}{\partial \theta} = L \cdot \sec^2(\theta)$

**Interpretation:**  
A small error in $\theta$ can cause a large error in $H$, especially at steep angles.

---

## Visualizing Sensitivity

The blog post shows how the sensitivity coefficient for angle ($\theta$) increases rapidly as the angle increases. This means that at higher angles, even a small error in measuring $\theta$ can lead to a large error in the calculated height.

![Sensitivity coefficient for angle](https://res.cloudinary.com/engineering-com/image/upload/w_640,h_640,c_limit,q_auto,f_auto/Sensitivity_5_oqw9xw.jpg){ height=250px }

---

## Special Case: Temperature Effects

For measurements affected by temperature, such as thermal expansion:

$$
\frac{\partial L}{\partial T} = \alpha L
$$

- $\alpha$ = coefficient of thermal expansion
- $L$ = measured length

A small temperature change can have a significant effect on long measurements.

---

## Practical Tips

- **Always check units:** Sensitivity coefficients may have units. Make sure all uncertainties are in compatible units before combining.
- **Nonlinear equations:** For nonlinear relationships, sensitivity coefficients can change depending on the value of the input. Evaluate them at the expected value or at the uncertainty limit for worst-case analysis.
- **Environmental factors:** Consider temperature, humidity, and other environmental effects in your uncertainty budget.

---

## Uncertainty Budget Example

| Source    | Value         | Distribution | Divisor | Sensitivity | Standard Uncertainty |
|-----------|---------------|--------------|---------|-------------|---------------------|
| $L$       | $\pm 50.5$ mm | Normal (95%) | 2       | 1.6         | 40.4 mm             |
| $h_1$     | $\pm 8.75$ mm | Normal (95%) | 2       | 1.0         | 4.4 mm              |
| $\theta$  | $\pm 1^\circ$ | Normal       | 1       | 632 mm/deg  | 632 mm              |

Combined standard uncertainty:

$$
u_c = \sqrt{(40.4)^2 + (4.4)^2 + (632)^2} = 633.4~\text{mm}
$$

---

## Summary

- Sensitivity coefficients show how much each input affects the output.
- Use partial derivatives to calculate sensitivity coefficients for each input.
- Always include sensitivity coefficients in your uncertainty budget.
- Pay special attention to inputs with large sensitivity coefficients—they dominate the uncertainty.

---


## Uncertainty Budget Analysis example : GUM Framework

### 1. Theoretical Background

The analysis aims to determine the **Combined Standard Uncertainty, $u_c(y)$**, and the **Expanded Uncertainty, $U$**, for a final measurement result ($Y$), which in this case is a dimension in millimeters ($\text{mm}$).

#### A. Standard Uncertainty ($u_i$) Calculation

The standard uncertainty ($u_i$) for each source ($X_i$) is calculated by converting the "Value" ($a_i$, often the half-width of the confidence interval) into a standard deviation using the appropriate **Divisor** based on the probability distribution, and then adjusting by the **Sensitivity Coefficient** ($c_i$).

$$u_i = \left(\frac{\text{Value } a_i}{\text{Divisor } k_i}\right) \times \text{Sensitivity Coefficient } c_i$$

#### B. Combined Standard Uncertainty ($u_c(y)$)

The individual standard uncertainties ($u_i$) are combined using the Root Sum of Squares (RSS) method, assuming the sources are uncorrelated:

$$u_c(y) = \sqrt{\sum_{i=1}^{N} u_i^2}$$
*(Note: In the simplified GUM framework used here, $u_i = c_i u(X_i)$, so the formula is simply the square root of the sum of the squares of the Standard Uncertainty column.)*

#### C. Expanded Uncertainty ($U$)

The expanded uncertainty ($U$) is calculated by multiplying the combined standard uncertainty by a **Coverage Factor ($k$)**. The table specifies $k=2$ for a $95\%$ confidence interval.

$$U = k \cdot u_c(y)$$

---

### 2. Probability Distributions and Divisors

The choice of Divisor ($k_i$) depends on the assumed probability distribution, which relates the available uncertainty information ($a_i$) to the standard uncertainty ($u_i$):

| Distribution | Description | Divisor ($k$) |
| :--- | :--- | :--- |
| **Normal ($k=2$)** | Assumes the Value ($a_i$) is the $95.45\%$ Expanded Uncertainty. Dividing by $k=2$ yields the Standard Uncertainty. | $2$ |
| **Triangular** | Assumes $a_i$ is the limit with high confidence. The best estimate of the standard uncertainty is $a_i / \sqrt{6}$. | $\sqrt{6} \approx 2.45$ |
| **Rectangular** | Assumes $a_i$ is the limit, and any value within $\pm a_i$ is equally probable. The best estimate of the standard uncertainty is $a_i / \sqrt{3}$. | $\sqrt{3} \approx 1.73$ |
| **Normal ($k=1$)** | Assumes the Value ($a_i$) is already the standard uncertainty (i.e., $k=1$ coverage). | $1$ |

---

### 3. Sensitivity Coefficients ($c_i$)

The Sensitivity Coefficient ($c_i$) converts the uncertainty in the unit of the input source ($X_i$) to the final measured unit of the result ($Y$, in $\text{mm}$).

*   **$c_i = 1$**: Used for sources already in $\text{mm}$ (Calibration, Resolution, Repeatability). A 1 $\text{mm}$ change in the source directly results in a 1 $\text{mm}$ change in the result.
*   **$c_i = 0.046$ (for $\text{deg}$)**: Converts uncertainty from **degrees** to **millimeters**. This implies that an input change of $1 \text{ deg}$ results in a $0.046 \text{ mm}$ change in the final measurement.
*   **$c_i = 0.0023$ (for $\text{C}$)**: Converts uncertainty from **Celsius** to **millimeters**. This implies a thermal expansion effect where a temperature change of $1 \text{ C}$ results in a $0.0023 \text{ mm}$ change in the final measurement.

---

### 4. Detailed Uncertainty Budget Calculation

We will verify the individual Standard Uncertainty ($u_i$) and the Combined Standard Uncertainty ($u_c(y)$) using Python.

```python
import numpy as np
import pandas as pd

# Constants
sqrt3 = np.sqrt(3)
sqrt6 = np.sqrt(6)

# Data from the table
data = {
    'Source': ['Calibration Uncertainty', 'Resolution', 'Cosine error', 'Temperature', 'Repeatability'],
    'Value (ai)': [0.01, 0.005, 3.0, 2.0, 0.02],
    'Units': ['mm', 'mm', 'deg', 'C', 'mm'],
    'Divisor (ki)': [2.0, sqrt6, sqrt3, sqrt3, 1.0],
    'Sensitivity Coeff (ci)': [1.0, 1.0, 0.046, 0.0023, 1.0]
}
df = pd.DataFrame(data)

# Calculation of Standard Uncertainty (ui)
df['Standard Uncertainty (ui)'] = (df['Value (ai)'] / df['Divisor (ki)']) * df['Sensitivity Coeff (ci)']
df['Standard Uncertainty (ui)'] = df['Standard Uncertainty (ui)'].round(5) # Round to 5 decimal places for precision

# Calculation of Squared Standard Uncertainty (ui^2)
df['Squared Uncertainty (ui^2)'] = df['Standard Uncertainty (ui)']**2

# Display the calculated budget
print("### Calculated Uncertainty Budget (mm) \n")
display(df.style.format({
    'Value (ai)': '{:.4f}',
    'Divisor (ki)': '{:.3f}',
    'Sensitivity Coeff (ci)': '{:.4f}',
    'Standard Uncertainty (ui)': '{:.5f}',
    'Squared Uncertainty (ui^2)': '{:.8f}'
}))


# 1. Combined Standard Uncertainty Calculation
# Sum of the squared uncertainties
sum_of_squares = df['Squared Uncertainty (ui^2)'].sum()

# u_c(y) is the square root of the sum of squares
uc_y = np.sqrt(sum_of_squares)
uc_y_rounded = round(uc_y, 3)

# 2. Expanded Uncertainty Calculation (k=2)
k_factor = 2
U = k_factor * uc_y
U_rounded = round(U, 3)

# Compare results to the table's values
print(f"\n--- Final Uncertainty Calculations ---\n")
print(f"Sum of Squared Uncertainties (Σu_i²): {sum_of_squares:.8f}")
print(f"Combined Standard Uncertainty u_c(y) (Table: 0.082): {uc_y_rounded:.3f} mm")
print(f"Expanded Uncertainty U (k=2, Table: 0.165): {U_rounded:.3f} mm")
```

### 5. Conclusion

The calculations verify the results presented in the original uncertainty budget table:

1.  **Combined Standard Uncertainty, $u_c(y)$:**
    $$\mathbf{u_c(y)} = \sqrt{0.005^2 + 0.002^2 + 0.080^2 + 0.003^2 + 0.020^2} \approx \mathbf{0.082 \text{ mm}}$$

2.  **Expanded Uncertainty, $U$ (95\% Confidence):**
    $$\mathbf{U} = k \cdot u_c(y) = 2 \times 0.082 \approx \mathbf{0.165 \text{ mm}}$$

The process successfully combines uncertainties from different distributions and units into a single final uncertainty estimate for the measured result.

----

## Further Reading

- [Sensitivity Coefficients in Uncertainty Budgets (engineering.com)](https://www.engineering.com/sensitivity-coefficients-in-uncertainty-budgets/)
- [Guide to the Expression of Uncertainty in Measurement (GUM)](https://www.bipm.org/en/publications/guides/gum.html)

