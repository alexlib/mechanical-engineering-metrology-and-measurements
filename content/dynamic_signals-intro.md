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

Follow this sequence to understand how measurement systems actually respond to inputs. The order moves from basic first-order dynamics, through second-order systems and damping, to practical applications and frequency-domain connections.

1. [1st order dynamic system](dynamic_signals-first_order_time_response.md) — first-order systems: time constant and exponential response (e.g., RC circuits, temperature sensors with lag).
2. [Step responses of dynamical systems](dynamic_signals-step_response.md) — interpreting step and impulse responses; the fundamental tool for characterizing system behavior.
3. [Log decrement method](dynamic_signals-2nd_order_system_step_function_log_decrement.md) — damped oscillation, natural frequency, damping ratio, and log-decrement estimation from noisy data.
4. [Lab Worksheet: Measurement of Unknown Mass using Vibrating Beam](dynamic_signals-mass_measurement_using_vibrations.md) — extract unknown mass from measured vibration frequency using the system model.
5. [Example of pre-measurement design](dynamic_signals-design_choice_2nd_order_pressure_transducer.md) — apply system dynamics to instrument design: trade-offs between sensitivity, bandwidth, and natural frequency.
6. [Fast Fourier Transform (FFT) of a sum of two sine signals](dynamic_signals-simple_fft_two_sine.md) — bridge from time domain to frequency domain with two sines.
7. [Symbolic evaluation of Fourier series coefficients](dynamic_signals-symbolic_evaluation_Fourier_coefficients.md) — analytical Fourier background for dynamic signals.
8. [Plot power spectrum of experimental data](dynamic_signals-load_plot_spectrum_turbulent_data_jet.md) — spectrum of real turbulent-jet data.
9. [Spectrum example](dynamic_signals-spectrum_example.md) — additional spectrum interpretation example.

Rationale: Students first understand how simple systems lag behind inputs (first-order), then recognize oscillatory behavior and damping (second-order). The final notebooks show why this matters for real sensors, and how time-domain behavior links to frequency content.

---

## What comes next?

Time-domain analysis reveals *when* signals occur and *how fast* they change. But to understand *what frequencies* are present in your signal, you need frequency-domain analysis. The **Signal Processing** chapter teaches Fourier transforms and FFT — the frequency-domain complement to the time-domain tools you've just learned.
