import matplotlib.pyplot as plt
import numpy as np


def Lisange(a, b, i):
    plt.subplot(2, 2, i)
    t = np.linspace(0, 2 * np.pi, 628)
    x = np.sin(a * t)
    y = np.sin(b * t)
    plt.plot(x, y)


if __name__ == '__main__':
    wavering_x = [3, 3, 5, 5]
    wavering_y = [2, 4, 4, 6]

    for i in range(4):
        Lisange(wavering_x[i], wavering_y[i], i + 1)
    plt.show()
