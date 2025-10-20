# Engineering Example: Uncertainty Analysis in Mechanical Measurements

## Introduction to the Engineering Problem

In mechanical engineering, precise measurements are critical for ensuring proper component functionality and system reliability. Let's explore a practical example of uncertainty analysis in measuring a precision shaft diameter for an engine bearing.

### The Engineering Context

A precision shaft needs to be measured for an engine bearing assembly:
- Required diameter specification: 25.000 ± 0.010 mm
- Measurement using digital micrometer
- Critical for proper bearing fit and engine performance

```{admonition} Why This Matters
:class: warning
Measurement errors can lead to:
- Oversized shaft: Bearing won't fit
- Undersized shaft: Excessive clearance, potential failure
- Consequences: Engine failure, warranty claims, safety issues
```

## The 8-Step Uncertainty Analysis Process

### Step 1: Define Measurement Needs

**Required Measurement:**
- Shaft diameter at specific location
- Tolerance: ±0.010 mm

**Equipment Selection:**
- Digital micrometer (0-25 mm range)
- Resolution: 0.001 mm
- Calibration uncertainty: ±0.002 mm (k=2)

**Measurement Conditions:**
- Temperature-controlled room (20 ± 1°C)
- Clean measurement surfaces
- Multiple measurements needed

### Step 2: Perform Measurements

**Measurement Data:**

| Reading | Value (mm) | Reading | Value (mm) |
|---------|------------|---------|------------|
| 1 | 24.998 | 6 | 25.001 |
| 2 | 25.001 | 7 | 24.999 |
| 3 | 25.000 | 8 | 25.000 |
| 4 | 24.999 | 9 | 25.001 |
| 5 | 25.000 | 10 | 25.000 |

**Recorded Conditions:**
- Temperature: 20.5°C
- Operator: J. Smith
- Date: 27-10-2024
- Equipment ID: MK-103

### Step 3: Evaluate Uncertainties

#### Type A Uncertainty (Statistical Analysis)

1. Calculate mean:

$$\bar{x} = \frac{\sum x_i}{n} = 24.9999 \text{ mm}$$

2. Calculate standard deviation:

$$s = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n-1}} = 0.001 \text{ mm}$$

3. Calculate standard uncertainty:

$$u_A = \frac{s}{\sqrt{n}} = \frac{0.001}{\sqrt{10}} = 0.00032 \text{ mm}$$

#### Type B Uncertainties (Other Sources)

1. **Calibration Uncertainty:**
   - Given as ±0.002 mm (k=2)
   - Standard uncertainty: $u_{B1} = \frac{0.002}{2} = 0.001 \text{ mm}$

2. **Resolution Uncertainty:**
   - Resolution = 0.001 mm
   - Half-width = 0.0005 mm
   - Standard uncertainty: $u_{B2} = \frac{0.0005}{\sqrt{3}} = 0.00029 \text{ mm}$

3. **Temperature Effect:**
   - Steel expansion coefficient: 11.5 × 10⁻⁶/°C
   - Temperature uncertainty: ±1°C
   - Length effect: $25 \text{ mm} × 11.5 × 10^{-6} × 1°C = 0.00029 \text{ mm}$
   - Standard uncertainty: $u_{B3} = \frac{0.00029}{\sqrt{3}} = 0.00017 \text{ mm}$

### Step 4: Check Independence

**Independent Sources:**
- Random measurement variations (Type A)
- Calibration uncertainty
- Resolution uncertainty

**Potentially Correlated:**
- Temperature effects on shaft and micrometer
- For this example, we'll treat them as independent (simplified case)

```{admonition} Note
:class: tip
In more complex cases, correlation between uncertainty sources must be considered in the calculations.
```

### Step 5: Calculate Results

**Base Result:**
- Mean value: 24.9999 mm
- Calibration correction: 0 mm (included in uncertainty)
- Temperature correction: negligible at 20.5°C
- Final value: 24.9999 mm

**Measurement Conditions Verification:**
- Temperature within specifications
- Proper measurement technique used
- Equipment calibrated and certified

### Step 6: Find Combined Uncertainty

For independent sources, the combined standard uncertainty is calculated as:

$$u_c = \sqrt{u_A^2 + u_{B1}^2 + u_{B2}^2 + u_{B3}^2}$$

Substituting our values:

$$u_c = \sqrt{(0.00032)^2 + (0.001)^2 + (0.00029)^2 + (0.00017)^2}$$
$$= \sqrt{0.0000001024 + 0.000001 + 0.0000000841 + 0.0000000289}$$
$$= \sqrt{0.0000012154} = 0.0011 \text{ mm}$$

### Step 7: Calculate Expanded Uncertainty

Using k = 2 for 95% confidence level:

$$U = k \cdot u_c = 2 × 0.0011 = 0.0022 \text{ mm}$$

```{admonition} Interpretation
:class: note
We are 95% confident that the true diameter lies within ±0.0022 mm of our measured value
```

**Comparison to Tolerance:**
- Tolerance: ±0.010 mm
- Uncertainty: ±0.0022 mm
- Measurement system is capable (Uncertainty < 1/4 tolerance)

### Step 8: Document Results

**Final Result:**
$$(24.9999 ± 0.0022)\text{ mm }(k=2, 95\% \text{ confidence level})$$

**Major Sources of Uncertainty:**
1. Calibration uncertainty (largest contributor)
2. Measurement repeatability
3. Resolution limits
4. Temperature effects

## Engineering Conclusions

### Technical Decisions
- Shaft diameter: 24.9999 ± 0.0022 mm
- Specification: 25.000 ± 0.010 mm
- Part is within tolerance
- Measurement uncertainty is acceptable

### Business Impact
- Part can be accepted
- Manufacturing process is capable
- Documentation supports quality requirements
- No risk to engine assembly

```{admonition} Key Learning Points
:class: important
1. Uncertainty analysis is systematic and quantitative
2. All uncertainty sources must be considered
3. Documentation is crucial
4. Results must be interpreted in context
5. Measurement capability affects decision-making
```

## Practice Questions

1. Why is the expanded uncertainty (k=2) used rather than the standard uncertainty?
2. How would you modify this analysis if the temperature variation was ±2°C instead of ±1°C?
3. What would be the impact if the measurement uncertainty was larger than 1/4 of the tolerance?
4. How would you handle correlated uncertainty sources if temperature effects couldn't be treated as independent?