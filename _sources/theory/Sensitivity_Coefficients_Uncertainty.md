# Sensitivity Coefficients in Uncertainty Budgets

_Source: [engineering.com](https://www.engineering.com/sensitivity-coefficients-in-uncertainty-budgets)_

## Introduction to Sensitivity Coefficients

> **Key Concept:**  
> When analyzing measurement uncertainty, sensitivity coefficients tell us how much an error in an input affects the final result.

---

### Simple Case: Direct Measurements

For a measurement with three error sources:

$$
Y = y + x_1 + x_2 + x_3
$$

where:

- $Y$ is the measurement result  
- $y$ is the true value (unknown)  
- $x_1$, $x_2$, $x_3$ are errors from different sources

In this case, sensitivity coefficients $c_i = 1$ because each error directly maps to the result.

The law of propagation of uncertainty states:

$$
U_C = \sqrt{\sum_{i=1}^{n} c_i^2 u_i^2}
$$

where:

- $U_C$ is combined uncertainty  
- $c_i$ is sensitivity coefficient for each source  
- $u_i$ is standard uncertainty for each source

---

## Practical Example: Building Height Measurement

![Measuring building height using clinometer and tape measure](building_measurement.png){ height=300px }

The height $H$ is calculated as:

$$
H = h_1 + L \cdot \tan(\theta)
$$

where:

- $h_1$ = height of clinometer  
- $L$ = horizontal distance  
- $\theta$ = measured angle

### Sensitivity Coefficients

1. For clinometer height ($h_1$):

   $$
   \frac{\partial H}{\partial h_1} = 1
   $$

2. For horizontal distance ($L$):

   $$
   \frac{\partial H}{\partial L} = \tan(\theta)
   $$

3. For angle ($\theta$):

   $$
   \frac{\partial H}{\partial \theta} = L \cdot \sec^2(\theta)
   $$

### Example Calculations

Given:

- $h_1 = 1.65$ m  
- $L = 10$ m  
- $\theta = 58^\circ$

Results:

- $\Delta L = 10$ mm $\rightarrow$ $\Delta H = 16$ mm (sensitivity = 1.6)
- $\Delta \theta = 0.5^\circ \rightarrow \Delta H = 316$ mm (sensitivity = 632 mm/deg)

---

## Special Case: Temperature Effects

For thermal expansion:

$$
\frac{\partial L}{\partial T} = \alpha L
$$

Where:

- $\alpha$ = coefficient of thermal expansion (e.g., $12 \times 10^{-6}/^\circ$C for steel)
- $L$ = measured length

![Non-linear sensitivity in cosine error](cosine_error.png){ height=250px }

---

## Key Points to Remember

1. Sensitivity coefficients $= 1$ when:
   - Measuring directly
   - Using Type A evaluations (repeatability studies)

2. Must calculate sensitivity coefficients when:
   - Combining multiple measurements mathematically
   - Dealing with temperature effects
   - Working with angular measurements
   - Considering environmental influences

3. Units must be consistent:
   - Dimensionless when input/output units match
   - Include proper conversion when units differ

> **Best Practice:**  
> When sensitivity is not constant, evaluate at the uncertainty value to get worst-case scenario, but be careful to:  
> 1. Check if sensitivity keeps increasing with error  
> 2. Consider using expanded uncertainty value

---

## Uncertainty Budget Example

| Source | Value      | Distribution | Divisor | Sensitivity | Standard Uncertainty |
|--------|------------|--------------|---------|-------------|---------------------|
| $L$    | $\pm 50.5$ mm | Normal (95%) | 2       | 1.6         | 40.4 mm             |
| $h_1$  | $\pm 8.75$ mm | Normal (95%) | 2       | 1.0         | 4.4 mm              |
| $\theta$ | $\pm 1^\circ$ | Normal      | 1       | 632 mm/deg  | 632 mm              |

Combined standard uncertainty:

$$
u_c = \sqrt{(40.4)^2 + (4.4)^2 + (632)^2} = 633.4~\text{mm}
$$