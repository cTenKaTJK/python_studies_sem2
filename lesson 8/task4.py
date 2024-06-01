import numpy as np
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt


def update(val):
    amp1, amp2 = amp1_slider.val, amp2_slider.val
    freq1, freq2 = freq1_slider.val, freq2_slider.val

    y1, y2 = amp1 * np.sin(freq1 * x), amp2 * np.sin(freq2 * x)
    y_sum = y1 + y2

    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line_sum.set_ydata(y_sum)

    fig.canvas.draw_idle()


if __name__ == '__main__':
    fig, (ax1, ax2, ax_sum) = plt.subplots(3, 1, figsize=(10, 8))

    x = np.linspace(0, 2 * np.pi, 1000)
    y1 = y2 = np.sin(x)
    y_sum = y1 + y2

    [line1], [line2], [line_sum] = ax1.plot(x, y1, label='1st wave'), ax2.plot(x, y2, label='2nd wave'), ax_sum.plot(x, y_sum, label='Sum of waves')

    ax1.set_ylim(-10, 10)
    ax2.set_ylim(-10, 10)
    ax_sum.set_ylim(-20, 20)

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.4)

    amp1 = plt.axes((0.15, 0.30, 0.65, 0.03))
    amp2 = plt.axes((0.15, 0.25, 0.65, 0.03))
    freq1 = plt.axes((0.15, 0.20, 0.65, 0.03))
    freq2 = plt.axes((0.15, 0.15, 0.65, 0.03))

    amp1_slider = Slider(amp1, '1st Amplitude', 0.1, 10.0, valinit=1)
    amp2_slider = Slider(amp2, '2nd Amplitude', 0.1, 10.0, valinit=1)
    freq1_slider = Slider(freq1, '1st Frequency', 0.1, 10.0, valinit=1)
    freq2_slider = Slider(freq2, '2nd Frequency', 0.1, 10.0, valinit=1)

    amp1_slider.on_changed(update)
    amp2_slider.on_changed(update)
    freq1_slider.on_changed(update)
    freq2_slider.on_changed(update)

    plt.show()
