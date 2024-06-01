import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


A, B = 1, 2


def init():
    line.set_data([], [])
    return line,


def anim(frame):
    delta = frame % 100
    t = np.linspace(0, 2 * np.pi, 628)
    x = np.sin(A * t)
    y = np.sin(B * t + delta)
    line.set_data(x, y)
    return line,


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    line, = ax.plot([], [], lw=2)
    animation = FuncAnimation(fig, anim, frames=np.arange(0, 101), init_func=init, interval=100, blit=True, repeat=True)
    plt.show()
