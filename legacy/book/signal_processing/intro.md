# Signal Processing — Introduction and Learning Goals

Short summary
Frequency-domain tools for measurement signals: FFT, windowing, spectral interpretation, and basic filtering.

Learning objectives
- Compute and interpret discrete Fourier transforms and spectra.
- Understand windowing, spectral leakage, and resolution trade-offs.
- Apply simple spectral filtering and reconstruction concepts.

Key concepts (brief)
- Frequency resolution, Nyquist limit, and window-induced spectral effects.
- Interpreting power spectra vs amplitude spectra.
- Practical filtering: time-domain vs frequency-domain considerations.

Prerequisites
Discrete signals, sampling basics, and NumPy FFT usage.

---

## Ordered reading (suggested)

Follow this sequence to master frequency-domain analysis. The order moves from basic FFT computation, through windowing artifacts and spectral interpretation, to practical noise filtering in the frequency domain.

1. [Fourier_transforms_pure_sine.ipynb](Fourier_transforms_pure_sine.ipynb) — discrete Fourier transform (DFT) of simple sinusoids; understand the FFT output
2. [Frequency_content_of_a_periodic_signal.ipynb](Frequency_content_of_a_periodic_signal.ipynb) — comprehensive FFT methodology: DC removal, proper sampling rate selection, interpreting amplitude and power spectra
3. [Fourier_transform_with_windowing.ipynb](Fourier_transform_with_windowing.ipynb) — spectral leakage, window functions, and how to choose windows for different signal types
4. [fft_of_multi_frequency_signal_window.ipynb](fft_of_multi_frequency_signal_window.ipynb) — FFT of signals with multiple frequency components; windowing in practice
5. [Fourier_coefficients_analytical_evaluation_periodic_ramp_function.ipynb](Fourier_coefficients_analytical_evaluation_periodic_ramp_function.ipynb) — analytical Fourier series for non-sinusoidal periodic signals
6. [FFT_based_filtering.ipynb](FFT_based_filtering.ipynb) — use frequency-domain filtering to remove noise and unwanted harmonics
7. [fft_filter_interactive.md](fft_filter_interactive.md) — interactive visualization of FFT filtering (hands-on exploration)

Rationale: Students first compute FFTs and understand the output, then learn how windowing affects spectral appearance (critical for interpretation), then apply filtering to extract clean signals. Analytical Fourier series connects theory to the numerical FFT results. The interactive tool at the end lets students experiment and develop intuition.

---

## What comes next?

You now understand how to analyze signals in both time domain (Dynamic Signals chapter) and frequency domain (this chapter). But how do you *acquire* signals from the real world without losing information to aliasing or quantization? The **A/D Conversion** chapter completes the picture, showing how sampling rate, quantization, and reconstruction affect the fidelity of your digital measurements.

<!-- AUTOGEN_START -->
## Pages in this chapter

- [Using FFT-based filter to reduce noise](FFT_based_filtering.ipynb)
- [Symbolic evaluation of Fourier coefficients](Fourier_coefficients_analytical_evaluation_periodic_ramp_function.ipynb)
- [Fourier transforms with windowing](Fourier_transform_with_windowing.ipynb)
- [Fourier transforms](Fourier_transforms_pure_sine.ipynb)
- [Using FFT the right way to find the correct spectrum](Frequency_content_of_a_periodic_signal.ipynb)
- [## FFT demo of a real, periodic signal](fft_of_multi_frequency_signal_window.ipynb)
- [Digitizing the signal using pure Python](proving_periods.ipynb)
<!-- AUTOGEN_END -->
