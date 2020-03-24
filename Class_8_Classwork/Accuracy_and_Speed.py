import numpy as np

# computer get big error from small error when do lot math

y = 1 + (10**-14)*np.sqrt(2)
x = 1

print(y-x)

print(np.sqrt(2))