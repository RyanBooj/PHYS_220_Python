import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Plot in 3D
delta = 0.1
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-3.0, 3.0, delta)

X, Y = np.meshgrid(x, y)  # set X and Y to all the numbers in the 2D plane in the rang of x and y
Z = np.sin(X)*np.cos(Y)

fig = plt.figure(1)
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z)
ax.plot_wireframe(X, Y, Z, color='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()