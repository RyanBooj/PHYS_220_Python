from gaussxw import gaussxwab
import numpy as np


def f(z):
    return np.exp(-z**2/(1-z)**2)/(1-z)**2


N = 50          # Number of slices
a = 0.0         # new integration limits
b = 1.0

# Calculate the positions and the weights of the slices (?) (x and w respectively)
x, w = gaussxwab(N, a, b)
s = 0.0


# sum each slice and print result (area under curve)
for k in range(N):
    s += w[k]*f(x[k])
print(s)