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
    # Mimic A/D conversion
    """)
    return


@app.cell
def _():
    # from https://dsp.stackexchange.com/questions/33596/analog-to-digital-conversion-using-python
    import numpy as np
    import matplotlib.pyplot as plt
    time_of_view = 1.0
    analog_time = np.linspace(0, time_of_view, num=100)
    sampling_rate = 21.0  # s.
    sampling_period = 1.0 / sampling_rate  # s.
    sample_number = time_of_view / sampling_period
    sampling_time = np.linspace(0, time_of_view, int(sample_number))  # Hz
    carrier_frequency = 9.0  # s
    amplitude = 1
    phase = 0
    quantizing_bits = 4
    quantizing_levels = 2 ** quantizing_bits / 2  # Hz
    quantizing_step = 1.0 / quantizing_levels  # V
      # deg
    def analog_signal(time_point):
        return amplitude * np.cos(2 * np.pi * carrier_frequency * time_point + phase)
    sampling_signal = analog_signal(sampling_time)
    quantizing_signal = np.round(sampling_signal / quantizing_step) * quantizing_step
    _fig = plt.figure()
    plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
    plt.title('Analog to digital signal conversion')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    # plt.plot (analog_time,   analog_signal (analog_time) );
    #plt.stem (sampling_time, sampling_signal);
    plt.show()
    return analog_signal, analog_time, plt, quantizing_signal, sampling_time


@app.cell
def _(analog_signal, analog_time, plt, quantizing_signal, sampling_time):
    _fig = plt.figure()
    plt.plot(analog_time, analog_signal(analog_time))
    #plt.stem (sampling_time, sampling_signal);
    plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
    plt.title('Analog to digital signal conversion')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    return


if __name__ == "__main__":
    app.run()
