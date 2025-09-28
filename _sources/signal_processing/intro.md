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

Recommended notebooks to run
- simple_fft_two_sine.ipynb
- spectrum_example.ipynb
- FFT_based_filtering.ipynb
- Fourier_transform_with_windowing.ipynb
- Frequency_content_of_a_periodic_signal.ipynb

Suggested exercises
- Demonstrate aliasing by downsampling and explain observed artifacts.
- Compare window functions on a mixed-frequency signal and discuss leakage.

Prerequisites
Discrete signals, sampling basics, and NumPy FFT usage.

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
