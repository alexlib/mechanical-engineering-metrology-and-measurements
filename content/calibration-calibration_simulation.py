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
    ## Simulation of calibration errors
    """)
    return


@app.cell
def _():
    # Cell 1: Imports and Setup

    import numpy as np
    import matplotlib.pyplot as plt
    import ipywidgets as widgets
    from scipy.stats import linregress
    from ipywidgets import interact, fixed, Layout, HBox, VBox
    from IPython.display import display

    # Set up the plotting style
    plt.style.use('seaborn-v0_8-whitegrid')
    # For Jupyter Lab/VS Code, consider using: %matplotlib widget
    return HBox, VBox, interact, linregress, np, plt, widgets


@app.cell
def _(linregress, np, plt):
    # Cell 2: Data Generation and Error Model Functions

    def apply_calibration_errors(X_ideal, ideal_slope, ideal_intercept, 
                                 n_cycles, n_points_per_half_cycle, 
                                 zero_offset, sensitivity_error, linearity_error, 
                                 hysteresis_error, dead_band, resolution):
        """
        Generates the cyclical data and applies the user-defined static errors.
    
        Returns: X_sim, Y_sim, ideal_fit_Y, is_increasing
        """
    
        # ----------------------------------------------------------------------
        # 1. Base X Data Generation (Cyclical for Hysteresis)
        # ----------------------------------------------------------------------
        X_min = X_ideal.min()
        X_max = X_ideal.max()
    
        # Create one cycle: ascending and then descending
        x_asc = np.linspace(X_min, X_max, n_points_per_half_cycle)
        x_desc = np.linspace(X_max, X_min, n_points_per_half_cycle)
    
        # Concatenate the ascending and descending parts for one full cycle
        x_cycle = np.concatenate([x_asc, x_desc[1:-1]]) # exclude endpoints to avoid duplication
    
        # Repeat the cycle N times
        X_sim = np.tile(x_cycle, n_cycles)
    
        # Identify the direction of travel for each point (needed for Hysteresis)
        # 1. Create a boolean array: True for ascending (first half of each tile), False for descending
        is_ascending_half = np.tile(np.concatenate([np.ones(len(x_asc), dtype=bool), 
                                                    np.zeros(len(x_desc)-2, dtype=bool)]), n_cycles)
        # The X value itself (for error calculation)
        X_err_input = X_sim
    
        # ----------------------------------------------------------------------
        # 2. Apply Errors (in a sequence, as they stack)
        # ----------------------------------------------------------------------
    
        # Start with the True Ideal Output
        Y_ideal = ideal_slope * X_err_input + ideal_intercept
        Y_erroneous = Y_ideal.copy()

        # a) Zero Offset Error (Bias)
        Y_erroneous += zero_offset

        # b) Sensitivity Error (Gain Error):
        # Sensitivity is the slope. A 10% error means a gain of 1.1 or 0.9.
        Y_erroneous *= (1 + sensitivity_error / 100.0)

        # c) Linearity Error: Simple quadratic term (parabola offset)
        X_mid = (X_max + X_min) / 2
        Y_erroneous += linearity_error * (X_err_input - X_mid)**2 
    
        # d) Hysteresis Error: Offset only applied during one direction (e.g., ascending)
        # Note: This is a simplified model of static hysteresis
        Y_erroneous[is_ascending_half] += hysteresis_error / 2
        Y_erroneous[~is_ascending_half] -= hysteresis_error / 2

        # e) Dead Band Error: No change in output for input changes within the dead band around X=0
        # For a static simulation, the simplest model is that the output is zero for a range of input
        Y_erroneous[np.abs(X_err_input) <= dead_band] = Y_erroneous[np.abs(X_err_input) <= dead_band].min() 
        # A more rigorous dead-band is state-dependent, but this shows the flat-spot effect well.
        # We'll clamp the output to the output at the deadband edge
    
        Y_at_deadband_edge = Y_erroneous[X_err_input == X_max].min() 
        # Re-evaluating dead band for a clearer visual effect near zero
        dead_band_mask = (X_err_input > -dead_band) & (X_err_input < dead_band)
        Y_erroneous[dead_band_mask] = ideal_intercept + zero_offset # Clamp to the biased zero value
    
    
        # f) Resolution/Quantization Error: output is forced to discrete steps
        if resolution > 0:
            Y_erroneous = np.round(Y_erroneous / resolution) * resolution
        
        # Add small random noise for a more realistic sensor reading
        Y_sim = Y_erroneous + np.random.normal(0, 0.1, len(Y_erroneous))
    
        return X_sim, Y_sim, Y_ideal, is_ascending_half


    # Define the main plotting function that will be called by ipywidgets.interact
    def plot_calibration_simulation(cycles, points_per_half_cycle, 
                                    zero_offset, sensitivity_error, linearity_error, 
                                    hysteresis_error, dead_band, resolution):
    
        # --- Data Definition ---
        X_ideal_range = np.array([-10, 10]) # Ideal range for X input
        ideal_slope = 1.0  # Ideal: Y = 1*X + 0
        ideal_intercept = 0.0

        # --- Data Generation ---
        X_sim, Y_sim, Y_ideal, is_ascending = apply_calibration_errors(
            X_ideal_range, ideal_slope, ideal_intercept, cycles, points_per_half_cycle, 
            zero_offset, sensitivity_error, linearity_error, hysteresis_error, dead_band, resolution
        )

        # --- Linear Regression on SIMULATED DATA ---
        # Perform linear fit: Y_fit = m*X_sim + c
        slope, intercept, r_value, p_value, std_err = linregress(X_sim, Y_sim)
        Y_fit = slope * X_sim + intercept

        # --- Error Calculation ---
        # Calibration Error (Residual): The difference between the measured data (Y_sim) 
        # and the best-fit line (Y_fit)
        calibration_error = Y_sim - Y_fit

        # --- Plotting ---
        fig, ax = plt.subplots(figsize=(10, 6))

        # 1. Plot the Simulated Sensor Data (as symbols)
        ax.plot(X_sim[is_ascending], Y_sim[is_ascending], 'o', color='blue', markersize=3, alpha=0.5, label='Simulated Data (Increasing X)')
        ax.plot(X_sim[~is_ascending], Y_sim[~is_ascending], 'o', color='red', markersize=3, alpha=0.5, label='Simulated Data (Decreasing X)')
    
        # 2. Plot the Best-Fit Linear Regression Line
        ax.plot(X_sim, Y_fit, '-', color='black', linewidth=2, label=f'Best-Fit Line: Y = {slope:.2f}X + {intercept:.2f}')
    
        # 3. Plot the Ideal Response Line
        ax.plot(X_sim, Y_ideal, '--', color='gray', linewidth=1, label='Ideal Response: Y = 1.00X + 0.00')

        # 4. Plot Error Arrows (every Nth point to avoid clutter)
        arrow_skip = len(X_sim) // 20 # Plot about 20 arrows total
        if arrow_skip == 0: arrow_skip = 1
        
        for i in range(0, len(X_sim), arrow_skip):
            ax.annotate('', xy=(X_sim[i], Y_fit[i]), xytext=(X_sim[i], Y_sim[i]),
                        arrowprops=dict(arrowstyle="->", color='darkorange', linewidth=1.5))
    
        # --- Annotations and Labels ---
        ax.set_title(f'Static Calibration Error Simulation (R²={r_value**2:.4f})')
        ax.set_xlabel('Input (X)')
        ax.set_ylabel('Output (Y)')
        ax.legend(loc='upper left')
    
        # Set fixed axis limits for a better interactive experience
        ax.set_xlim(X_ideal_range[0] - 1, X_ideal_range[1] + 1)
        ax.set_ylim(X_ideal_range[0] - 3, X_ideal_range[1] + 3)
    
        plt.show()

        # --- Display Error Metrics ---
        # The max absolute residual is often a key metric for static calibration error.
        max_abs_error = np.max(np.abs(calibration_error))
    
        # Calculate Non-Linearity (Max deviation from best-fit line)
        # In this context, the max_abs_error is a good proxy for the combined error.
    
        print(f"--- Key Metrics ---")
        print(f"Max Absolute Calibration Error (Residual): {max_abs_error:.2f}")
        print(f"Calibration Span (Max Y - Min Y): {Y_sim.max() - Y_sim.min():.2f}")

    return (plot_calibration_simulation,)


@app.cell
def _(HBox, VBox, interact, plot_calibration_simulation, widgets):
    # Cell 3: Create Widgets and Interactive Display

    # --- Widget Definitions ---

    # Data Generation Sliders
    cycles_slider = widgets.IntSlider(min=1, max=5, step=1, value=2, description='Cycles (N):')
    points_slider = widgets.IntSlider(min=10, max=100, step=10, value=30, description='Points/Half-Cycle (N2):')

    # Error Sliders
    zero_offset_slider = widgets.FloatSlider(min=-2.0, max=2.0, step=0.1, value=0.0, description='Zero Offset (Bias):')
    sensitivity_slider = widgets.FloatSlider(min=-10.0, max=10.0, step=1.0, value=0.0, description='Sensitivity Error (%):')
    linearity_slider = widgets.FloatSlider(min=-0.05, max=0.05, step=0.005, value=0.0, description='Linearity Error (x^2 Coeff):')
    hysteresis_slider = widgets.FloatSlider(min=0.0, max=1.0, step=0.1, value=0.0, description='Hysteresis Error (Mag):')
    dead_band_slider = widgets.FloatSlider(min=0.0, max=1.0, step=0.1, value=0.0, description='Dead Band (Input Width):')
    resolution_slider = widgets.FloatSlider(min=0.0, max=0.5, step=0.05, value=0.0, description='Resolution (Quantization):')

    # Organize Widgets in a clear layout
    data_control = VBox([
        HBox([cycles_slider, points_slider]),
        HBox([zero_offset_slider, sensitivity_slider, linearity_slider]),
        HBox([hysteresis_slider, dead_band_slider, resolution_slider])
    ])

    # Create the interactive plot
    print("Adjust the sliders below to simulate different static calibration errors.")
    print("The orange arrows show the residual (Calibration Error) between the data points and the best-fit line.")

    interactive_plot = interact(
        plot_calibration_simulation, 
        cycles=cycles_slider,
        points_per_half_cycle=points_slider,
        zero_offset=zero_offset_slider,
        sensitivity_error=sensitivity_slider,
        linearity_error=linearity_slider,
        hysteresis_error=hysteresis_slider,
        dead_band=dead_band_slider,
        resolution=resolution_slider
    )
    return


if __name__ == "__main__":
    app.run()
