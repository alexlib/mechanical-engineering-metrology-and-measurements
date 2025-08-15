# Mars Rover Temperature Measurement & Uncertainty Analysis

## 1. Introduction: The Challenge of Measurement in Extreme Environments

The Mars rover engineering team requires **precise temperature measurements** to ensure the proper functioning of mechanical parts in **extreme environmental conditions**, ranging from **-150°C to +60°C**. As research engineers, our task is to select the right instrument and design a robust testing and analysis plan on Earth, ultimately quantifying the measurement uncertainty.

**Why is Uncertainty Important?**
No measurement, however carefully made, can be completely free of uncertainties. The word 'error' in this context is not a mistake or blunder, but an **inevitable part of any measurement**. Our task is to **quantify this uncertainty** to understand the possible range of values within which the true value of the measured property lies. A measurement result is truly complete only when accompanied by a quantitative statement of its uncertainty, providing confidence in engineering decisions, especially for critical applications like space exploration.

This notebook will guide you through the process, providing a structured approach that integrates theoretical concepts with practical considerations for the Mars Rover case.

## 2. Instrument Selection and Justification

For this demanding application, I would choose a **Thermocouple**.

### Justification:

*   **Wide Temperature Range**: Thermocouples can operate across a very wide temperature range, typically from **-200°C to 2000°C**. This comfortably covers the required **-150°C to +60°C** extreme conditions for the Mars rover, providing ample margin.
*   **Robustness**: Thermocouples are generally **robust and durable** due to their simple construction, consisting of two dissimilar metal wires joined at one end. This makes them well-suited for **harsh environments** where mechanical stresses, vibration, and radiation might be a concern, such as on Mars.
*   **Signal Output**: Thermocouples produce a **voltage signal**, which can be easily processed by the rover's electronic systems after appropriate signal conditioning.
*   **Dynamic Response**: While not explicitly stated as a primary selection criterion for the Mars Rover in the sources, thermocouples typically have a **faster response time** compared to other common temperature sensors like PRTs, which is beneficial for tracking rapidly changing environmental temperatures.

### Comparison to Alternatives:
While Platinum Resistance Thermometers (PRTs) offer higher accuracy and a range of -250°C to 600°C (also covering the required range), their **fragility compared to thermocouples makes them less ideal** for the highly demanding and potentially abrasive environment of a Mars rover. Given the paramount need for reliable functioning of mechanical parts in "extreme conditions," robustness and broad operational range are key considerations.

## 3. Experiment Design for Earth-Based Testing

The goal is to test the chosen thermocouple under **simulated Mars extreme temperature conditions (-150°C to +60°C)** to characterize its performance and estimate measurement uncertainty.

### Simulated Environment:

*   A **temperature-controlled chamber** capable of reaching and maintaining stable temperatures within the range of **-150°C to +60°C** will be used. This chamber must allow for precise control of the temperature set points.
*   A **high-accuracy reference thermometer**, traceable to national standards (e.g., NPL for the UK), will be placed alongside the thermocouple under test to provide the "true value" for calibration and verification. This reference instrument should have significantly lower uncertainty than the thermocouple being tested.

### Variables:

*   **Independent Variable**: The **known temperature** set within the temperature-controlled chamber, as measured by the reference thermometer.
*   **Dependent Variable**: The **voltage output** of the thermocouple, which will then be converted to a temperature reading.
*   **Extraneous Variables**: These are variables that are not directly controlled but could affect the measurement. Examples include:
    *   **Room temperature/humidity** outside the chamber.
    *   **Power supply fluctuations** to the measurement system.
    *   **Electromagnetic interference (EMI)** affecting the low-voltage thermocouple signal.
    *   **Vibration** from the cooling/heating system of the chamber.
    *   **Aging effects** on the thermocouple or electronics over time.
    *   **Wire length/resistance** of the thermocouple leads.

### Measurement System Diagram (Conceptual Description):
The temperature measurement system for the thermocouple would generally follow this flow:
1.  **Desired Property (Temperature)**: The Mars environment temperature.
2.  **Sensor**: The thermocouple junction.
3.  **Transducer**: The thermocouple itself, which converts temperature into an electromotive force (EMF) or voltage.
4.  **Signal Conditioning**: This block handles critical aspects for thermocouples, primarily **cold junction compensation** (to account for the reference junction temperature) and **amplification** (as thermocouple signals are typically small). This could also include **filtering** to reduce noise.
5.  **Analog-to-Digital Converter (ADC)**: Converts the analog voltage signal from the signal conditioning unit into a digital value. This introduces **quantization error** or **resolution error**.
6.  **Digital Processing Unit**: The rover's computer system, which receives the digital signal, applies calibration corrections, performs calculations (e.g., converting voltage to temperature using lookup tables or polynomials), and stores/transmits the data.
7.  **Output**: The final temperature reading.

## 4. Calibration Design

**Calibration** establishes the relationship between the instrument's input and output and quantifies its errors and uncertainties.

### a. Static Calibration
**Purpose**: To develop a **functional relationship (correlation)** between the known input temperature and the thermocouple's output voltage, typically a voltage-to-temperature lookup table or a polynomial curve. This also helps identify **systematic errors** like linearity, zero error, and hysteresis.

**Procedure**:
1.  **Reference Standard**: Use a high-accuracy reference thermometer (e.g., a calibrated PRT) to measure the "true" temperature inside the chamber. The reference thermometer itself will be traceable to international standards (e.g., ITS-90 via NPL).
2.  **Controlled Temperature Points**: Set the chamber to a series of **stable, discrete temperature points** across the entire operational range (-150°C to +60°C). These points should include multiple steps in both increasing (upscale) and decreasing (downscale) directions to assess **hysteresis**.
3.  **Data Collection**: At each stable temperature point, allow the system to reach **thermal equilibrium**. Record multiple readings from both the reference thermometer and the thermocouple's voltage output.
4.  **Correction for Cold Junction**: Ensure the thermocouple system includes proper cold junction compensation, as this is critical for accurate temperature measurement with thermocouples.
5.  **Data Analysis**:
    *   Plot the thermocouple's output voltage against the reference temperature to create a **static calibration curve**.
    *   Determine the **static sensitivity** (slope of the curve).
    *   Assess **linearity error** if a linear relationship is expected (deviation from a best-fit line).
    *   Quantify **hysteresis error** by comparing upscale and downscale readings at the same temperature.
    *   Determine **zero error** (offset at 0°C or reference point).
    *   The **range of the errors** (deviations from the fitted curve) will provide an initial estimate of the **uncertainty in the calibration**.

### b. Dynamic Calibration
**Purpose**: To characterize the thermocouple's **time-dependent response** to changing temperatures, identifying parameters like **time constant (τ)**, natural frequency ($\omega_n$), and damping (ζ). This is vital for a rover experiencing non-static temperature conditions.

**Procedure**:
1.  **Step Response Test**:
    *   Rapidly change the temperature in the chamber from one stable temperature to another (e.g., a **step change** in temperature).
    *   Record the thermocouple's output voltage over time as it responds to this step change.
    *   Analyze the transient response to determine the **time constant** ($\tau$), which indicates how quickly the thermocouple reacts to a temperature change. For a first-order system (a common model for thermocouples), the output will reach approximately 63.2% of its final value after one time constant.
2.  **Frequency Response Test (Optional but Ideal)**:
    *   If feasible, expose the thermocouple to **sinusoidally varying temperatures** at different frequencies.
    *   Measure the **gain (amplitude ratio)** and **phase shift** of the thermocouple's output relative to the input temperature oscillations.
    *   Plot these results as a **Bode plot** to identify the system's **bandwidth or cutoff frequency**, which indicates the range of frequencies it can accurately measure. This helps ensure the sensor can track the expected rate of temperature changes on Mars.
3.  **Data Analysis**: The dynamic calibration data will allow us to quantify dynamic errors that would occur if the temperature is not static (e.g., if the thermocouple responds too slowly to rapid changes), providing a Type B uncertainty component for dynamic conditions.

## 5. Uncertainty Analysis: The 8-Step Process

This process follows the guidelines to quantify the overall uncertainty of the temperature measurement for the Mars rover.

### Step 1: Decide what you need to find out from your measurement

*   **Measurement Goal**: Obtain a **precise and accurate temperature measurement** for the Mars rover's mechanical parts, ensuring functionality within **-150°C to +60°C**, with a **quantified uncertainty**.
*   **Measurement Function**: The final temperature reading ($T_{rover}$) will be a function of several input quantities. It can be expressed as:
    $T_{rover} = f(V_{out}, T_{cold\_junction}, C_{cal}, R_{ADC}, T_{env\_effect}, Noise, ...)$
    where:
    *   $V_{out}$: Thermocouple voltage output.
    *   $T_{cold\_junction}$: Reference junction temperature.
    *   $C_{cal}$: Calibration corrections.
    *   $R_{ADC}$: ADC resolution.
    *   $T_{env\_effect}$: Impact of other environmental factors on the sensor itself.
    *   $Noise$: Electrical interference.

### Step 2: Carry out and record the measurements needed

*   **Execution**: Perform **repeated measurements** during static and dynamic calibration tests in the controlled chamber. Ensure the thermocouple is properly installed and connected.
*   **Good Practice**:
    *   **Calibration Status**: Verify the calibration of the reference thermometer used in the test.
    *   **Procedure Adherence**: Follow a clearly defined measurement procedure for each test type (static, dynamic, repeatability).
    *   **Multiple Readings**: Take **multiple readings** at each stable condition to assess **repeatability**. This is crucial for Type A uncertainty evaluation.
    *   **Notebook Record-keeping**: Maintain a **detailed laboratory notebook**, including date, initials, instrument used, calibration details, environmental conditions (e.g., ambient lab temperature), and **raw data**.
    *   **Outlier Detection**: Visually inspect data for outliers and statistically evaluate suspicious points (e.g., using Chauvenet's or Thompson's $\tau$ method) before excluding them.

*Example of a detailed notebook entry (hypothetical data, adapted from):*
```
Date: 2024-11-02
Initials: [Your Initials]
Thermocouple ID: Type K, TC-001
Reference Thermometer: NPL Calibrated PRT, Serial #XYZ-456 (Calibrated: 2024-10-15)
Chamber Temperature: -150.0 °C (Set Point)
Ambient Lab Temperature: 22.5 °C

Temperature Readings (mV, after initial conversion and approximate CJC):
Reading 1: -5.82 mV
Reading 2: -5.80 mV
Reading 3: -5.83 mV
Reading 4: -5.79 mV
Reading 5: -5.81 mV
... (continue for 20-30 readings)
Reading 25: -5.82 mV

Notes: Reading 12 was -6.15 mV. Suspected outlier due to momentary power fluctuation.
```

### Step 3: Evaluate the uncertainty of each input quantity (Type A and Type B evaluations)

All uncertainties must be expressed in **standard uncertainty ($u_i$)** terms.

*   **Type A Uncertainty Evaluation (Statistical)**:
    *   **Source**: **Repeatability** of the thermocouple readings. This accounts for **random variations** in the measurement process.
    *   **Method**: From the repeated readings, calculate the **standard deviation of the mean** ($s_x / \sqrt{n}$ or $u_{rep}$). This standard uncertainty is associated with the average value obtained from the readings, representing how well we know the true mean.
    *   **Probability Distribution**: Generally assumed to be **normal (Gaussian)** for Type A evaluations, especially with sufficient data points ($n \ge 20$).

    *Example Calculation (hypothetical):*
    *   Assume 25 readings are taken at a steady -150°C.
    *   Mean of readings: $\bar{V} = -5.81 \text{ mV}$ (example, converted to temperature later).
    *   Sample standard deviation ($S_x$) of individual readings: $0.015 \text{ mV}$ (hypothetical).
    *   **Standard uncertainty of the mean (Type A)**: $u_{rep} = S_x / \sqrt{n} = 0.015 \text{ mV} / \sqrt{25} = \mathbf{0.003 \text{ mV}}$.

*   **Type B Uncertainty Evaluation (Non-Statistical)**:
    *   **Source**: **Calibration Uncertainty ($u_{cal}$)**. This comes from the calibration certificate of the reference thermometer and the static calibration of the thermocouple. It quantifies how well the thermocouple's readings match the reference values.
        *   **Method**: Often provided with an expanded uncertainty at a given confidence level (e.g., 95%) and a coverage factor (k=2). Divide the expanded uncertainty by the coverage factor to get the standard uncertainty.
        *   **Probability Distribution**: Typically assumed to be **normal**.
        *   *Example:* If a calibration certificate states $\pm 0.05 \text{ °C}$ at k=2 for the reference thermometer, then $u_{cal, ref} = 0.05 \text{ °C} / 2 = \mathbf{0.025 \text{ °C}}$. Similarly, the uncertainty from the thermocouple's own static calibration (deviation from the fitted curve) is a Type B component.
    *   **Source**: **Resolution Error ($u_{res}$)**. This arises from the finite resolution of the ADC in the measurement system.
        *   **Method**: For a digital instrument, the resolution error is often estimated as $\pm \frac{1}{2}$ of the least significant digit (LSD). For a **rectangular distribution** (equal probability within limits, typical for resolution errors), the standard uncertainty is the half-range divided by $\sqrt{3}$. So, $u_{res} = \frac{\text{half-range of resolution}}{\sqrt{3}}$.
        *   **Probability Distribution**: **Rectangular**.
        *   *Example:* If the ADC resolution is $0.001 \text{ mV}$, the half-range is $0.0005 \text{ mV}$. So, $u_{res} = 0.0005 \text{ mV} / \sqrt{3} = \mathbf{0.000289 \text{ mV}}$.
    *   **Source**: **Cold Junction Compensation Error ($u_{CJC}$)**. The accuracy of the cold junction temperature measurement directly affects the thermocouple's reading.
        *   **Method**: Based on the specifications of the cold junction sensor or its own calibration.
        *   **Probability Distribution**: Typically rectangular or normal, depending on available information.
        *   *Example:* Assume CJC sensor has $\pm 0.1 \text{ °C}$ accuracy, rectangular distribution. $u_{CJC} = 0.1 \text{ °C} / \sqrt{3} = \mathbf{0.0577 \text{ °C}}$.
    *   **Source**: **Thermal EMFs/Noise ($u_{noise}$)**. Spurious voltages caused by temperature gradients in the wiring or electromagnetic interference.
        *   **Method**: Estimated from manufacturer's specifications, previous experience, or by observing signal fluctuations under stable conditions.
        *   **Probability Distribution**: Often assumed rectangular or normal.
        *   *Example:* Assume noise level causes $\pm 0.005 \text{ mV}$ fluctuation, rectangular. $u_{noise} = 0.005 \text{ mV} / \sqrt{3} = \mathbf{0.00289 \text{ mV}}$.
    *   **Source**: **Material Inhomogeneity/Aging ($u_{mat}$)**. Variations in the thermocouple wire material or changes over time can affect its Seebeck coefficient.
        *   **Method**: From manufacturer's data or long-term stability tests.
        *   **Probability Distribution**: Often rectangular.
        *   *Example:* Assume this contributes $\pm 0.02 \text{ °C}$ over a year, rectangular. $u_{mat} = 0.02 \text{ °C} / \sqrt{3} = \mathbf{0.0115 \text{ °C}}$.
    *   **Source**: **Dynamic Response Error ($u_{dyn}$)**. If the temperature changes faster than the thermocouple can respond, it will introduce a lag or amplitude distortion.
        *   **Method**: Determined from dynamic calibration results (e.g., from the steady-state error in ramp response or amplitude/phase errors in frequency response).
        *   *Example:* If a dynamic test shows a potential lag of $0.05 \text{ °C}$ under expected Mars temperature change rates, and this is considered a bias, then $u_{dyn} = 0.05 \text{ °C}$ (if directly quantifiable as a fixed error, otherwise, depends on the error's distribution).

*   **Sensitivity Coefficients ($c_i$)**:
    *   Sensitivity coefficients allow for combining sources with **different units or functional relationships**. The GUM (Guide to the Expression of Uncertainty in Measurement) defines this as a partial differential equation, where the partial differential $\partial T_{rover} / \partial x_i$ describes the rate at which the measurement result will change if one of the input quantities ($x_i$) changes.
    *   For example, if the thermocouple output is in mV and the final result is in °C, a sensitivity coefficient (e.g., the Seebeck coefficient in °C/mV, which is the slope of the calibration curve) would be applied.
    *   If $T = f(V)$, then $c_V = \partial T / \partial V$.
    *   **Thermal Expansion Example**: For a length measurement, if temperature ($T$) affects length ($L$) via thermal expansion ($\Delta L = L_{nominal} \cdot \alpha \cdot \Delta T$), then the sensitivity coefficient for temperature's contribution to length uncertainty is $c_T = L_{nominal} \cdot \alpha$.
    *   **Cosine Error Example (Angular Misalignment)**: For a nominal length of $100 \text{ mm}$, an angular error of $\pm 3^\circ$ could result in an error of $100(1-\cos 3^\circ) = 0.137 \text{ mm}$. The sensitivity coefficient is $0.137 \text{ mm} / 3^\circ = 0.046 \text{ mm/degree}$.
    *   For many of our temperature uncertainty components (like resolution or CJC error already in °C), the sensitivity coefficient relative to the final temperature reading might simplify to **1**, assuming they directly add to the final temperature value. However, for voltage-based errors, this conversion is crucial.

### Step 4: Decide whether the errors of the input quantities are independent of each other

*   In most cases, for measurement uncertainties like those listed (calibration, resolution, repeatability, noise), they are considered **independent (uncorrelated)**. This is a common assumption that allows for simpler combination methods (RSS).
*   **Caution**: If correlation were suspected (e.g., if a single environmental factor simultaneously biases multiple parts of the measurement chain), extra, more complex calculations would be required. For this analysis, we will **assume independence**.

### Step 5: Calculate the result of your measurement (including any known corrections)

*   The **best estimate of the temperature** will be the **mean of the repeated thermocouple readings** (after converting voltage to temperature using the static calibration curve/lookup table) plus any **known corrections**. These corrections might come from the static calibration certificate (e.g., if the calibration shows a consistent offset or a non-linearity that can be modeled and applied).

*Example Calculation:*
*   Assume the average voltage from Step 3 ($\bar{V} = -5.81 \text{ mV}$) corresponds to $-150.0 \text{ °C}$ according to the thermocouple's calibration curve.
*   If the calibration certificate also specifies a known systematic correction (e.g., +0.02 °C at -150°C), then:
    **Best Estimate ($T_{best}$) = $-150.0 \text{ °C} + 0.02 \text{ °C} = \mathbf{-149.98 \text{ °C}}$**.

### Step 6: Find the combined standard uncertainty from all the individual uncertainty contributions

*   Since errors are assumed independent, the combined standard uncertainty ($u_c$) is calculated using the **root sum of the squares (RSS)** method, also known as "adding in quadrature".
*   The formula for combined standard uncertainty is:
    $u_c = \sqrt{ \sum (c_i u_i)^2 }$
    This means each standard uncertainty ($u_i$) is multiplied by its sensitivity coefficient ($c_i$), squared, summed, and then the square root is taken.

*Hypothetical Combined Standard Uncertainty Calculation (values converted to °C via sensitivity coefficients):*
*   $u_{rep} = 0.01 \text{ °C}$ (e.g., $0.003 \text{ mV}$ from Step 3 converted to °C)
*   $u_{cal} = 0.025 \text{ °C}$
*   $u_{res} = 0.0005 \text{ °C}$ (e.g., $0.000289 \text{ mV}$ from Step 3 converted to °C)
*   $u_{CJC} = 0.0577 \text{ °C}$
*   $u_{noise} = 0.002 \text{ °C}$ (e.g., $0.00289 \text{ mV}$ from Step 3 converted to °C)
*   $u_{mat} = 0.0115 \text{ °C}$
*   $u_{dyn} = 0.05 \text{ °C}$

$u_c = \sqrt{ (0.01)^2 + (0.025)^2 + (0.0005)^2 + (0.0577)^2 + (0.002)^2 + (0.0115)^2 + (0.05)^2 }$
$u_c = \sqrt{ 0.0001 + 0.000625 + 0.00000025 + 0.00332929 + 0.000004 + 0.00013225 + 0.0025 }$
$u_c = \sqrt{ 0.00669079 }$
$\mathbf{u_c \approx 0.0818 \text{ °C}}$.

### Step 7: Calculate expanded uncertainty for a particular level of confidence

*   The combined standard uncertainty ($u_c$) is equivalent to one standard deviation, giving about **68% confidence** that the true value lies within $\pm u_c$ of the measurement result.
*   To achieve a higher confidence level, such as the widely accepted **95% confidence level**, the combined standard uncertainty is multiplied by a **coverage factor (k)**.
*   For a **normal distribution**, the coverage factor for **95% confidence is typically k=2**.
*   The formula for expanded uncertainty (U) is:
    **Expanded Uncertainty (U) = k * u_c**.

*Example Calculation:*
*   $U = 2 \times 0.0818 \text{ °C} = \mathbf{0.1636 \text{ °C}}$.

### Step 8: Write down the measurement result and the uncertainty, and state how you got both of these

*   The final measurement result should be expressed clearly and concisely, including the best estimate, the expanded uncertainty, and the confidence level.
*   **Example Wording**:
    "The measured temperature for the Mars rover mechanical parts is **-149.98 ± 0.16 °C**. The reported uncertainty is based on a standard uncertainty multiplied by a coverage factor k = 2, providing a level of confidence of approximately 95%, assuming normality."

### Uncertainty Budget Table:

A comprehensive table summarizing each source of uncertainty is essential.

| Source of Uncertainty | Value (if applicable) | Units | Probability Distribution | Divisor (for $u_i$) | Sensitivity Coefficient ($c_i$) | Standard Uncertainty ($u_i(T_{rover})$) (°C) |
| :-------------------- | :-------------------- | :---- | :----------------------- | :------------------ | :------------------------------ | :---------------------------------- |
| **Type A**            |                       |       |                          |                     |                                 |                                     |
| Repeatability         | (from std dev mean)   | °C    | Normal                   | 1                   | 1                               | 0.010                               |
| **Type B**            |                       |       |                          |                     |                                 |                                     |
| Reference Cal. Error  | $\pm 0.05$            | °C    | Normal                   | 2                   | 1                               | 0.025                               |
| ADC Resolution Error  | $\pm 0.0005$          | mV    | Rectangular              | $\sqrt{3}$          | (mV to °C conversion)           | 0.0005                              |
| Cold Junction Comp.   | $\pm 0.1$             | °C    | Rectangular              | $\sqrt{3}$          | 1                               | 0.0577                              |
| Electrical Noise      | $\pm 0.005$           | mV    | Rectangular              | $\sqrt{3}$          | (mV to °C conversion)           | 0.002                               |
| Material Inhomog.     | $\pm 0.02$            | °C    | Rectangular              | $\sqrt{3}$          | 1                               | 0.0115                              |
| Dynamic Response      | $\pm 0.05$            | °C    | (Assumed from test)      | 1                   | 1                               | 0.050                               |
| **Combined Standard Uncertainty ($u_c$)** |                       |       |                          |                     |                                 | **0.0818**                          |
| **Expanded Uncertainty (U) (k=2, 95% Confidence)** |                       |       |                          |                     |                                 | **0.16**                            |

*(Note: Sensitivity coefficients for mV to °C conversion would be applied where applicable in the 'Standard Uncertainty' column, assuming the example values listed are already in °C for simplicity. For a real budget, you would list the original units and then apply the sensitivity factor before calculating the final standard uncertainty for that row.)*

## 6. Data Measurement and Analysis Plan Summary

### Data Measurement Plan:

*   **Pre-Measurement Checks**: Verify calibration status of all equipment, ensure cleanliness, check for damage.
*   **Environmental Control**: Maintain stable and known conditions in the test chamber. Monitor ambient lab conditions if they could influence sensor performance (e.g., through wire resistance).
*   **Number of Repetitions**: A sufficient number of repetitions (e.g., **20-30 readings** for Type A analysis) should be taken at each test point to reliably estimate the mean and standard deviation.
*   **Randomization**: If multiple factors are being varied or multiple thermocouples are being tested, randomize the test order to minimize the effect of unrecognized systematic errors or drifts.
*   **Documentation**: Detailed notes in a **lab notebook** covering set-up, environmental conditions, raw data, and any observations or anomalies.

### Data Analysis Plan:

*   **Raw Data Processing**:
    *   Convert thermocouple voltage readings to temperature using the static calibration curve or lookup table.
    *   Identify and statistically treat outliers (e.g., using Thompson's $\tau$ method).
    *   Calculate the mean temperature and standard deviation for repeatability (Type A uncertainty).
*   **Uncertainty Budget Calculation**:
    *   List all identified uncertainty sources (Type A and Type B).
    *   Determine the appropriate probability distribution for each source (e.g., normal, rectangular).
    *   Apply divisors and sensitivity coefficients to convert all contributions to standard uncertainties in the same units (e.g., °C).
    *   Combine all standard uncertainties using the **RSS method** to get the combined standard uncertainty.
    *   Calculate the expanded uncertainty using a coverage factor (k=2 for 95% confidence).
*   **Software Tools**: Use statistical software (e.g., Python with `scipy.stats`, or spreadsheets like Excel) for calculations, curve fitting for calibration, and uncertainty budget compilation.
*   **Reporting**: Present the final temperature estimate with its expanded uncertainty and confidence level, along with the detailed uncertainty budget table.

By following this structured approach, the Mars rover engineering team can obtain reliable temperature measurements with a quantified level of confidence, ensuring the mechanical parts function properly in the harsh Martian environment.

## References and Further Reading

This notebook draws heavily on the following sources, which are also excellent resources for further study:

*   "Calculating an Uncertainty Budget for a Measurement - Dr Jody Muelaner"
*   "Mars Rover Temperature: Measurement and Uncertainty Analysis"
*   "Mechanical Engineering Metrology and Measurements (MEMM) — Introduction to Measurements for Mechanical Engineers" (The course material context for this notebook)
*   "gpg131_mechanical.pdf" (NPL's Beginner's Guide to Measurement in Mechanical Engineering)
*   "Lecture1.pdf" (Introductory lecture for MEMM)
*   "uncertainty101.pdf" (Uncertainty 101 lecture for MEMM)
*   "lecture5_statistics.pdf" (Statistics for Uncertainty Analysis)
*   "week2.pdf" (Lectures on 8 steps, generalized systems, sensitivity coefficients)
*   "week3.pdf" (Lectures on experimental design, sensor classification, static calibration)
*   "week4.pdf" (Lectures on dynamic measurements, A/D, Fourier analysis)
*   "week5.pdf" (Lectures on statistics, PDF, t-distribution, chi-squared, regression, outliers)
