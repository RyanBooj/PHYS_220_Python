import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

def randRange(n, vmin, vmax):
    return (vmin-vmax)*np.random.rand(n) + vmin

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

n = 100
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randRange(n, 23, 32)
    ys = randRange(n, 0, 100)
    zs = randRange(n, zl, zh)
    ax.scatter(xs, ys, zs, s=m, c=c)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()