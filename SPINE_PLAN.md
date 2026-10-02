# Proposed book spine — mapped onto MEGN 300

**Status: proposal, not yet applied.** This document maps all 98 existing pages
onto the chapter sequence of
[MEGN 300: Instrumentation & Automation](https://github.com/professor-duran/MEGN300)
(Adam W. Duran, Colorado School of Mines, CC BY 4.0), so you can review the
ordering before any of it is written into `book.yml`.

## What MEGN 300 covers, and what it does not

MEGN 300 has 23 chapters in six parts. Parts III–VI (circuit fundamentals,
amplifiers, high-power devices, debugging, open/closed-loop control, PID,
LabVIEW, heat transfer, fluid power) have **no corresponding content in this
book**. So the spine here follows Parts I and II only — chapters 1 to 13.

| MEGN part | Chapters | In this book? |
|---|---|---|
| I — Measurement Fundamentals | 1–5 | Yes, all five map onto existing pages |
| II — Signals and Signal Processing | 6–13 | Mostly; ch. 12 (analog filters) has nothing to map to, ch. 13 (digital filters) only one page |
| III — Electronics | 14–17 | No content |
| IV — Control Systems | 18–20 | No content |
| V — Software Tools | 23 | No content |
| VI — Engineering Science | 21–22 | No content |

## The three structural changes this implies

1. **Calibration moves early.** MEGN puts the measurement-systems model,
   traceability and standards in ch. 1 and static calibration in ch. 2 —
   *before* error analysis and statistics. This book currently teaches
   calibration third, after statistics.
2. **Dynamic measurement moves to ch. 3**, ahead of error analysis, on the
   argument that you should know how a system responds before you try to
   characterise its uncertainty.
3. **Statistics becomes ch. 5**, after error analysis. MEGN resolves the
   chicken-and-egg by giving ch. 4 a "Statistical Foundations" section (mean,
   standard error, confidence intervals) and only going deeper in ch. 5.

Net effect on your page counts — the lopsidedness largely disappears:

| Chapter | Pages now | Pages proposed |
|---|---|---|
| Theory | 27 | 7 |
| Calibration | 21 | 12 |
| Statistics | 16 | 14 |
| Dynamic Signals | 10 | 7 |
| A/D | 6 | 5 |
| Signal Processing | 9 | 14 |
| Unsorted (exercises) | 8 | 0 — distributed |

## Proposed mapping

### Part I — Measurement Fundamentals

**1. Fundamentals of Measurement Theory** — the measurement-systems model,
traceability, standards, and how to record work. (7)

`theory-intro` · `theory-laboratory_notebook` · `theory-significant_digits` ·
`theory-standartization` · `theory-general_measurement_system_analysis` ·
`theory-best_practice_summary` · `theory-checklist`

**2. Static Measurements** — calibration, sensitivity, linearity, hysteresis,
resolution. (12)

*New intro page needed.* `calibration-intro` · `calibration-linear_regression` ·
`theory-uncertainty_of_a_slope` · `calibration-sensitivity_analysis` ·
`theory-Sensitivity_Coefficients_Uncertainty` · `calibration-Lineariy_error_example` ·
`calibration-hysteresis_error_analysis` · `calibration-calibration_error_analysis_2` ·
`calibration-calibration_error_analysis_pressure` ·
`calibration-calibration_non_linear_relations` ·
`calibration-calibration_curve_log_log` · `calibration-calibration_simulation`

> `theory-uncertainty_of_a_slope` sits here rather than in error analysis: it
> *is* a static-calibration method, and its interactive version is now a
> reference-quality page.

**3. Dynamic Measurements** — first and second order systems, step response,
bandwidth. (7)

`dynamic_signals-intro` · `dynamic_signals-first_order_time_response` ·
`dynamic_signals-step_response` ·
`dynamic_signals-2nd_order_system_step_function_log_decrement` ·
`dynamic_signals-design_choice_2nd_order_pressure_transducer` ·
`dynamic_signals-mass_measurement_using_vibrations` ·
`unsorted-input_output_sin_1st_order`

**4. Error Analysis and Uncertainty** — error types, propagation, confidence
intervals, budgets. (24 — the largest chapter, as befits the book's theme)

`theory-01_uncertainty101` · `theory-02_basic_error_analysis` ·
`theory-simple_example` · `theory-uncertainty_example` ·
`theory-volume_cylinder_undertainty_example` ·
`theory-uncertainty_propagation_monte_carlo_gum` ·
`theory-uncertainty_sources_notebook` · `theory-surface_roughness_budget` ·
`theory-hot-wire_uncertainty_budget` · `theory-comparing_two_methods_cylinder_volume` ·
`theory-simulations_for_uncertainty` · `theory-example_uncertainty_analysis` ·
`theory-uncertainty_analysis_NASA` · `theory-exam_example` ·
`theory-iaea_uncertainty_presentation` · `theory-example_from_best_practice` ·
`theory-teaching_measurement_uncertainty` ·
`theory-teaching_measurement_introductory_physics_lab` ·
`calibration-several_calibration_examples` ·
`calibration-orifice_calibration_example` ·
`calibration-full_calibration_analysis_example` ·
`calibration-pressure_calibration_example` · `unsorted-homework_1` ·
`unsorted-homework_example_1` · `unsorted-q2_ex3`

**5. Statistics and Experimental Data Analysis** (14)

`statistics-intro` · `statistics-basic_statistics` ·
`statistics-getting_started` · `statistics-distributions` ·
`statistics-Central_limit_theorem_illustration` · `statistics-histogram_to_distribution` ·
`statistics-Exploring+different+distribution` ·
`statistics-estimate_mean_variance_median_using_pdf` ·
`statistics-t-distribution` · `statistics-t-test` ·
`statistics-Lecture_5` · `statistics-chi_square_test_example` ·
`statistics-outliers_example` · `statistics-outliers_example_pairs`

### Part II — Signals and Signal Processing

**6. Sensors and Actuators** — the real-instrument calibrations. (7)

*New intro page needed.* `calibration-lvdt_calibration_example` ·
`calibration-lvdt_calibration_2` · `calibration-micrometer_calibration` ·
`calibration-weight_scale_example_Wheeler` ·
`calibration-calibration_sensor_examples` ·
`calibration-regression_analysis` ·
`calibration-calibration_simulation_interactive`

**7. Analog vs Digital Systems** — sampling, aliasing, quantization, ADC/DAC.
(5)

`a2d-intro` · `a2d-mimic_analog_to_digital_conversion` ·
`a2d-sampling_aliasing_examples` · `a2d-reconstruct_with_sinc` ·
`a2d-Reconstruction_periodic_signal_Cardinal_series`

**8. Signal-to-Noise Ratio** — *no dedicated content.* Either omit, or add a
short new page on noise sources and averaging. Flagging this as a genuine gap.

**9. Fourier Series and Complex Signal Construction** (5)

*New intro page needed.* `signal_processing-Frequency_content_of_a_periodic_signal` ·
`signal_processing-Fourier_coefficients_analytical_evaluation_periodic_ramp_function` ·
`dynamic_signals-symbolic_evaluation_Fourier_coefficients` ·
`signal_processing-proving_periods` · `a2d-create_plot_signal`

**10. FFT and Spectral Analysis** — DFT, windowing, leakage. (7)

*New intro page needed.* `signal_processing-Fourier_transforms_pure_sine` ·
`signal_processing-Fourier_transform_with_windowing` ·
`signal_processing-fft_of_multi_frequency_signal_window` ·
`signal_processing-FFT_based_filtering` ·
`signal_processing-fft_filter_interactive` ·
`dynamic_signals-simple_fft_two_sine` · `dynamic_signals-spectrum_example` ·
`dynamic_signals-load_plot_spectrum_turbulent_data_jet`

**11–13. Digital Signal Processing / Filters** — (0 beyond ch. 10)
`signal_processing-intro` is retired; its content folds into ch. 10.

## Pages that need merging or a decision

| Pages | Issue | Proposed resolution |
|---|---|---|
| `statistics-outliers_example`, `statistics-outliers_example-2`, `statistics-outliers_example_two` | Three near-identical modified-Thompson demonstrations | Merge into one page with three subsections; keep `..._pairs` (regression residuals) separate since it is a genuinely different test |
| `calibration-full_calibration_analysis_example`, `calibration-pressure_calibration_example` | Same pressure up/down calibration analysis; one is the abridged copy | Merge into the single page already mapped to ch. 4 |
| `statistics-Lecture_5`, `statistics-chi_square_test_example` | Two chi-square demonstrations | Merge |
| `statistics-distributions`, `statistics-Exploring+different+distribution`, `statistics-histogram_to_distribution` | Three distribution explorations | Merge into one; the chapter intro already says one comprehensive reference is enough |
| `dynamic_signals-simple_fft_two_sine`, `dynamic_signals-spectrum_example`, `signal_processing-Frequency_content_of_a_periodic_signal` | FFT/spectrum content split across two chapters | All land in ch. 10, which resolves the split |
| `calibration-calibration_simulation`, `calibration-calibration_simulation_interactive` | Static and interactive versions of the same demo | Keep both; the interactive one is a genuine asset |
| `unsorted-intro` | The "Unsorted — Guide" page | Retire; its guidance moves into the distributed exercise pages |

**Total after merging: 98 → ~90 pages.**

## Exercises

Per your instruction these are distributed rather than kept in a back section:

- `unsorted-homework_1`, `unsorted-homework_example_1` → **ch. 2** (static
  calibration homework)
- `unsorted-q2_ex3`, `unsorted-normal_vs_lognormal` → **ch. 5** (statistics)
- `unsorted-random_data_for_hw_1` → **ch. 4** (uncertainty budget)
- `unsorted-input_output_sin_1st_order` → **ch. 3** (dynamic systems)
- `unsorted-doppler` → **ch. 9** (Fourier / signal construction)

Each would get a short brief: what to extract, what to submit.

## New pages this spine requires

1. **Static Measurements** intro — the largest gap; today calibration has no
   proper opener.
2. **Sensors and Actuators** intro.
3. **Fourier Series** intro.
4. **FFT and Spectral Analysis** intro.
5. Possibly an **SNR** page (ch. 8 is otherwise empty).

## Two things worth deciding before I proceed

- **Is 24 pages too heavy for chapter 4?** It is thematically the core of the
  book, but a single chapter that long has its own navigation problem. Splitting
  it into "Error analysis and propagation" and "Uncertainty budgets in practice"
  would match how it is actually taught.
- **Should ch. 8 (SNR) be written or omitted?** Writing it would add real value —
  noise reduction is what students most often need and the book currently only
  touches it inside the FFT pages.