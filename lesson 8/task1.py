import matplotlib.pyplot as plt
import numpy as np
import scipy.special as ss


x = np.linspace(-1, 1, 200)
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

[plt.plot(x, ss.legendre(i + 1)(x), color=colors[i - 1], label=f'{i} pow of legendre`s polynome') for i in range(1, 8)]

plt.title("Legendre`s polynom")
plt.legend()
plt.grid(True)
plt.show()
