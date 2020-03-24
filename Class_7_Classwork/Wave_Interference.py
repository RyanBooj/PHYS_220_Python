import numpy as np
import matplotlib.pyplot as plt

# variables or something
wavelength = 5.0  # cm
k = 2*np.pi/wavelength
ei0 = 1.0  # initial amplitude
separation = 20.0  # cm
side = 100.0  # cm
points = 500
spacing = side/points

x1 = side/2 + separation/2
y1 = side/2

x2 = side/2 - separation/2
y2 = side/2

ei = np.empty([points, points], float)  # empty 500x500 vector for floats
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j

        r1 = np.sqrt((x-x1)**2 + (y-y1)**2)
        r2 = np.sqrt((x-x2)**2 + (y-y2)**2)

        ei[i, j] = ei0*np.sin(r1*k) + ei0*np.sin(r2*k)

plt.imshow(ei, origin="lower", extent=[0, side, 0, side])
plt.show()