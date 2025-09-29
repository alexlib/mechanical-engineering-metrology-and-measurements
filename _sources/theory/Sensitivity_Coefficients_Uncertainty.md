# Sensitivity Coefficients in Uncertainty Budgets

From the blog of https://www.engineering.com/sensitivity-coefficients-in-uncertainty-budgets/

## Introduction to Sensitivity Coefficients 

```{admonition} Key Concept
When analyzing measurement uncertainty, sensitivity coefficients tell us how much an error in an input affects the final result.
```

### Simple Case: Direct Measurements

For a measurement with three error sources:

```{math}
Y = y + x_1 + x_2 + x_3
```

where:
- Y is the measurement result
- y is the true value (unknown)
- x₁, x₂, x₃ are errors from different sources

In this case, sensitivity coefficients = 1 because each error directly maps to the result.

The law of propagation of uncertainty states:

```{math}
U_C = \sqrt{\sum_{i=1}^{n} c_i^2u_i^2}
```

where:
- U_C is combined uncertainty
- c_i is sensitivity coefficient for each source
- u_i is standard uncertainty for each source

## Practical Example: Building Height Measurement

```{figure} building_measurement.png
---
height: 300px
name: building-height
---
Measuring building height using clinometer and tape measure
```

The height H is calculated as:

```{math}
H = h_1 + L \times \tan(\theta)
```

where:
- h₁ = height of clinometer
- L = horizontal distance
- θ = measured angle

### Sensitivity Coefficients

1. For clinometer height (h₁):
   ```{math}
   \frac{\partial H}{\partial h_1} = 1
   ```

2. For horizontal distance (L):
   ```{math}
   \frac{\partial H}{\partial L} = \tan(\theta)
   ```

3. For angle (θ):
   ```{math}
   \frac{\partial H}{\partial \theta} = L \times \sec^2(\theta)
   ```

### Example Calculations

For measurements:
- h₁ = 1.65 m
- L = 10 m  
- θ = 58°

Results:
- ΔL = 10mm → ΔH = 16mm (sensitivity = 1.6)
- Δθ = 0.5° → ΔH = 316mm (sensitivity = 632 mm/deg)

## Special Case: Temperature Effects

For thermal expansion:

```{math}
\frac{\partial L}{\partial T} = \alpha L
```

Where:
- α = coefficient of thermal expansion (e.g., 12×10⁻⁶/°C for steel)
- L = measured length

```{figure} cosine_error.png
---
height: 250px
name: cosine-error
---
Non-linear sensitivity in cosine error
```

## Key Points to Remember

1. Sensitivity coefficients = 1 when:
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

```{admonition} Best Practice
When sensitivity is not constant, evaluate at the uncertainty value to get worst-case scenario, but be careful to:
1. Check if sensitivity keeps increasing with error
2. Consider using expanded uncertainty value
```

## Uncertainty Budget Example

| Source | Value | Distribution | Divisor | Sensitivity | Standard Uncertainty |
|--------|--------|--------------|----------|-------------|-------------------|
| L | ±50.5mm | Normal (95%) | 2 | 1.6 | 40.4mm |
| h₁ | ±8.75mm | Normal (95%) | 2 | 1.0 | 4.4mm |
| θ | ±1° | Normal | 1 | 632mm/deg | 632mm |

The combined standard uncertainty:
```{math}
u_c = \sqrt{(40.4)^2 + (4.4)^2 + (632)^2} = 633.4\text{ mm}
```