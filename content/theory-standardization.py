import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Standardization and Traceability

    Measurements are useful only when they can be compared. Traceability is the property of a measurement result that provides an unbroken chain of calibrations to a reference standard, with a stated uncertainty at each step. Good traceability makes results from different labs, instruments, or times comparable and defensible.

    Key points
    - Traceability links your instrument to a reference standard (ideally an SI realization) through documented calibration steps.
    - Every calibration step should include an uncertainty estimate — this is how comparability is quantified.
    - Accreditation and standards bodies provide the infrastructure and rules that make traceability reliable.

    Essential organizations (one-line roles)
    1. [BIPM — Bureau International des Poids et Mesures](https://www.bipm.org/) — coordinates the international system of units (SI) and key comparisons between national metrology institutes.
    2. National Metrology Institutes (NMIs), e.g. [NIST (US)](https://www.nist.gov/) and [NPL (UK)](https://www.npl.co.uk/) — realize national standards and provide high-quality calibrations.
    3. [ILAC — International Laboratory Accreditation Cooperation](https://ilac.org/) — promotes international acceptance of accredited laboratory results.
    4. [ISO — International Organization for Standardization](https://www.iso.org/) — publishes standards that govern measurement and quality systems.
    5. National standards bodies (example: [Standards Institute of Israel (SII)](https://www.sii.org.il/en/)) — implement accreditation and national policies.

    Short student tasks
    - Trace one common lab measurement (e.g., length, mass, voltage) back to the reference standard: list each calibration step and its uncertainty.
    - Visit one organization above and write a 4–6 sentence summary of how it supports measurement comparability.
    - For a chosen calibrated sensor, sketch a minimal uncertainty budget for one calibration step (identify main uncertainty contributors).

    Further reading
    - GUM: "Guide to the Expression of Uncertainty in Measurement" (BIPM/JCGM) — core guidance on uncertainty and traceability.
    - BIPM and NMI websites — practical examples of how standards are realized and disseminated.
    """)
    return


if __name__ == "__main__":
    app.run()
