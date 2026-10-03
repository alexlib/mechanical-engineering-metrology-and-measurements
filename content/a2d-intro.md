# Analog vs Digital — Introduction and Learning Goals

Short summary
Sampling, aliasing, reconstruction, and practical A/D conversion examples. This chapter explains how continuous analog signals become discrete digital data, and how to avoid losing information in the process.

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

1. [Sampling, clipping and aliasing](a2d-sampling_aliasing_examples.md) — Nyquist theorem and aliasing demonstration: what happens when you sample too slowly.
2. [Mimic A/D conversion](a2d-mimic_analog_to_digital_conversion.md) — quantization: how continuous analog values map to discrete digital levels and the uncertainty that introduces.
3. [Digital to Analog conversion using sinc](a2d-reconstruct_with_sinc.md) — Shannon reconstruction using sinc interpolation: perfectly recovering a band-limited signal from samples.
4. [Analog to digital (A/D) and Digital to Analog (d/A) conversion example](a2d-Reconstruction_periodic_signal_Cardinal_series.md) — theoretical foundation for reconstruction; Cardinal series and why sinc interpolation works.
5. [Signal construction and helper functions for the frequency content class](a2d-create_plot_signal.md) — helper functions and signal generation utilities for experimenting with sampling and reconstruction.

Rationale: Students first see the consequences of undersampling (aliasing), then understand quantization error, then learn *how* signals are perfectly reconstructed, before diving into the mathematics. This progression connects practice (what goes wrong?) to theory (why?) to mathematics (how to fix it?).

---

## You've Completed the Toolkit

You now have a complete understanding of measurement uncertainty:
- **Uncertainty**: What uncertainty is and where it comes from
- **Statistics**: How to quantify uncertainty from data
- **Calibration**: How to reduce and control instrument uncertainty
- **Dynamic Signals & Signal Processing**: How systems and signal analysis affect measurements
- **Analog vs Digital**: How to acquire analog signals digitally without losing fidelity

These tools combine in real experiments: you design a measurement → calibrate your instrument → choose sampling parameters → collect data → analyze statistically → propagate uncertainty → report results with confidence.

See the main book introduction for a "Measurement Workflow" guide that ties all these concepts together in a practical measurement scenario.
