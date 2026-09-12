# Analog-to-Digital (A2D) — Introduction and Learning Goals

Short summary
Sampling, aliasing, reconstruction, and practical A/D conversion examples.

Learning objectives
- Explain sampling theorem and conditions for perfect reconstruction.
- Demonstrate aliasing and anti-aliasing requirements.
- Implement simple reconstructions (sinc/interpolation) and study errors.

Key concepts (brief)
- Nyquist frequency and aliasing examples.
- Reconstruction using sinc (Cardinal series) and practical limits.
- Quantization and its effect on measurement uncertainty (intro-level).

Prerequisites
Basic Fourier theory and sampling concepts.

---

## Ordered reading (suggested)

Follow this sequence to understand how analog signals are safely digitized. The order moves from the fundamental sampling theorem, through aliasing pitfalls, to practical reconstruction and signal regeneration.

1. [sampling_aliasing_examples.ipynb](sampling_aliasing_examples.ipynb) — Nyquist theorem and aliasing demonstration: what happens when you sample too slowly
2. [mimic_analog_to_digital_conversion.ipynb](mimic_analog_to_digital_conversion.ipynb) — quantization: how continuous analog values map to discrete digital levels and the uncertainty that introduces
3. [reconstruct_with_sinc.ipynb](reconstruct_with_sinc.ipynb) — Shannon reconstruction using sinc interpolation: perfectly recovering a band-limited signal from samples
4. [Reconstruction_periodic_signal_Cardinal_series.ipynb](Reconstruction_periodic_signal_Cardinal_series.ipynb) — theoretical foundation for reconstruction; Cardinal series and why sinc interpolation works
5. [create_plot_signal.ipynb](create_plot_signal.ipynb) — helper functions and signal generation utilities for experimenting with sampling and reconstruction

Rationale: Students first see the consequences of undersampling (aliasing), then understand quantization error, then learn *how* signals are perfectly reconstructed, before diving into the mathematics. This progression connects practice (what goes wrong?) to theory (why?) to mathematics (how to fix it?).

---

## You've Completed the Toolkit

You now have a complete understanding of measurement uncertainty:
- **Theory**: What uncertainty is and where it comes from
- **Statistics**: How to quantify uncertainty from data
- **Calibration**: How to reduce and control instrument uncertainty  
- **Dynamic Signals & Signal Processing**: How systems and signal analysis affect measurements
- **A/D Conversion**: How to acquire analog signals digitally without losing fidelity

These tools combine in real experiments: you design a measurement → calibrate your instrument → choose sampling parameters → collect data → analyze statistically → propagate uncertainty → report results with confidence. 

See the main book introduction for a "Measurement Workflow" guide that ties all these concepts together in a practical measurement scenario.

<!-- AUTOGEN_START -->
## Pages in this chapter

- [Analog to digital (A/D) and Digital to Analog (d/A) conversion example](Reconstruction_periodic_signal_Cardinal_series.ipynb)
- [Signal construction and helper functions for the frequency content class](create_plot_signal.ipynb)
- [Mimic A/D conversion](mimic_analog_to_digital_conversion.ipynb)
- [Digital to Analog conversion using sinc](reconstruct_with_sinc.ipynb)
- [Sampling, clipping and aliasing](sampling_aliasing_examples.ipynb)
<!-- AUTOGEN_END -->
