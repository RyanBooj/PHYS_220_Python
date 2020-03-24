import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data5 = np.loadtxt('Class_5_Data.txt')
x = data5[:, 0]
y = data5[:, 1]
err = data5[:, 2]
plt.figure(1)
plt.errorbar(x, y, err, fmt='o')

coef = np.polyfit(x, y, 1)
fun = np.poly1d(coef)
plt.plot(x, fun(x), 4)
plt.show()

data4 = np.loadtxt('Class_4_Data.txt')
y = norm.pdf(data4)

plt.figure(2)
n, bins, patches = plt.hist(data4, 20, density=True, color='b', alpha=.6, edgecolor='k')

data4_mean = data4.mean()
data4_std = data4.std()

h = norm.pdf(bins, data4_mean, data4_std)

plt.plot(bins, h, 'r--', linewidth=2)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')

plt.show()