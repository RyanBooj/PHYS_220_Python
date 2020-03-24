import numpy as np
import matplotlib.pyplot as plt

# density plot
data = np.loadtxt("circular.txt", float)

# change location of origin to the bottom left corner like usual
plt.imshow(data, origin="lower")

# there are many options to change the look of the plot, for example, make it grayscale
# or add a bar that shows high/low density
plt.gray()
plt.colorbar()

# plt.savefig("circular.jpg", dpi=600)
plt.show()