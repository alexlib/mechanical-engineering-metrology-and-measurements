# Dynamic Signals — Introduction and Learning Goals

**Short summary**
Time-domain and dynamical-system behavior: step responses, first/second order systems, and vibration-based measurements.

**Learning objectives**
- Interpret first- and second-order system responses and key parameters (time constant, damping, natural frequency).
- Extract physical quantities (e.g., mass from vibrations) from measured signals.
- Link time-domain responses to frequency content.

**Key concepts (brief)**
- Step response, log-decrement, and damping ratio estimation.
- Modal interpretation for simple systems and measurement-driven parameter estimation.
- Practical considerations: sensor dynamics and filtering.

**Prerequisites**
Ordinary differential equations basics and elementary signal processing.

---

## Ordered reading (suggested)

Follow this sequence to understand how measurement systems actually respond to inputs. The order moves from basic first-order dynamics, through second-order systems and damping, to practical applications where you extract physical information from vibrations.

1. [first_order_time_response.ipynb](first_order_time_response.ipynb) — first-order systems: time constant and exponential response (e.g., RC circuits, temperature sensors with lag)
2. [step_response.ipynb](step_response.ipynb) — interpreting step and impulse responses; the fundamental tool for characterizing system behavior
3. [2nd_order_system_step_function_log_decrement.ipynb](2nd_order_system_step_function_log_decrement.ipynb) — damped oscillation, natural frequency, damping ratio, and log-decrement estimation from noisy data
4. [mass_measurement_using_vibrations.ipynb](mass_measurement_using_vibrations.ipynb) — extract unknown mass from measured vibration frequency using the system model
5. [design_choice_2nd_order_pressure_transducer.ipynb](design_choice_2nd_order_pressure_transducer.ipynb) — apply system dynamics to instrument design: trade-offs between sensitivity, bandwidth, and natural frequency

Rationale: Students first understand how simple systems lag behind inputs (first-order), then recognize oscillatory behavior and damping (second-order). The final two notebooks show why this matters: real sensors and transducers have dynamics that affect what you actually measure, and you can *exploit* those dynamics to extract information (vibration → mass).

---

## What comes next?

Time-domain analysis reveals *when* signals occur and *how fast* they change. But to understand *what frequencies* are present in your signal, you need frequency-domain analysis. The **Signal Processing** chapter teaches Fourier transforms and FFT — the frequency-domain complement to the time-domain tools you've just learned.

