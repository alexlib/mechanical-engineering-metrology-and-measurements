---
title: Interactive FFT-based Filter Explorer
---

## Interactive FFT-based Filter Explorer

This is an interactive version of the **FFT-based filtering** notebook. Adjust the
cutoff frequency and filter order with the sliders below — the plots update
automatically.

```{marimo-config}
:echo: true
```

```{marimo} python
import marimo as mo
import numpy as np
from numpy.fft import fft, ifft
from matplotlib import pyplot as plt
```

Load the data file. The data contains a periodic time signal with noise:

```{marimo} python
data = np.loadtxt('book/data/data_for_FFT_filter.txt')
t = data[:, 0]
f = data[:, 1]
N = len(t)
f_s = 1.0 / (t[1] - t[0])              # sampling frequency
T = N / f_s                             # total sample time
del_f = 1.0 / T                         # frequency resolution
f_fold = f_s / 2.0                      # folding frequency
N_disc = int(N / 2.0)

# frequency axis
f_incr = np.arange(0, f_fold + del_f, del_f)
f_dcr = np.arange(f_fold - del_f, 0, -del_f)
frequency = np.r_[f_incr, f_dcr]

# FFT
FFT1 = fft(f)
magnitude1 = np.abs(FFT1) / N_disc
magnitude1[0] /= 2.0
```

Use the sliders to adjust the Butterworth filter parameters:

```{marimo} python
f_cut_slider = mo.ui.slider(
    start=50, stop=2000, step=10, value=500,
    label="Cutoff frequency (Hz)"
)
order_slider = mo.ui.slider(
    start=2, stop=20, step=1, value=10,
    label="Filter order"
)
mo.md("**Filter parameters**\n\n{f_cut_slider}\n\n{order_slider}").batch(
    f_cut_slider=f_cut_slider,
    order_slider=order_slider,
)
```

Apply the filter and plot the results:

```{marimo} python
f_cut = f_cut_slider.value
order_n = order_slider.value

# Butterworth gain
G = 1.0 / np.sqrt(1 + ((frequency / f_cut) ** (2 * order_n)))

# Filter
FFT_filtered = FFT1 * G
FFT_inv = ifft(FFT_filtered)
FFT2 = fft(np.real(FFT_inv))
magnitude2 = np.abs(FFT2) / N_disc
magnitude2[0] /= 2.0

fig, axes = plt.subplots(3, 1, figsize=(10, 10), tight_layout=True)

# Original time signal
axes[0].plot(t, f, marker='o', markerfacecolor='b',
             linestyle=':', color='lightgrey')
axes[0].set_title(f'Periodic time signal (f_s = {f_s:.0f} Hz, N = {N})')
axes[0].set_xlabel('$t$ (s)')
axes[0].set_ylabel('$g_i$ (V)')

# FFT comparison
axes[1].plot(frequency, magnitude1, '-b', label='Unfiltered FFT')
axes[1].plot(frequency, magnitude2, '--r', label='Filtered FFT')
axes[1].set_title(
    f'Filtered and Unfiltered FFT (f_cut = {f_cut} Hz, order = {order_n})')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude (V)')
axes[1].legend()
axes[1].set_xlim([0, f_fold])

# Filtered vs unfiltered time trace
axes[2].plot(t, f, '-b', label='Unfiltered')
axes[2].plot(t, np.real(FFT_inv), '-r', label='Filtered')
axes[2].set_title('Filtered and Unfiltered Time Trace')
axes[2].set_xlabel('Time (s)')
axes[2].set_ylabel('Amplitude')
axes[2].legend()
axes[2].set_xlim([0, 0.051])

plt.close()
fig
```
