import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = (x ** 2 + y ** 2) / 2

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_wireframe(x, y, z, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('MSE surface')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_wireframe(x, y, np.log10(z))
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_title('MSE log scale surface')

plt.tight_layout()
plt.show()
