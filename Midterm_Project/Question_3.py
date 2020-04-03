import numpy as np
from gaussxw import gaussxwab

# defining constants
P = 6.626070 * (10**-34)  # Planck's Constant
hbar = P / (np.pi * 2)  # Planck's Constant / 2Pi
c = 299792485  # Speed of light
kb = 1.38064852 * (10**-23)

# defining a function to represent the expression in the integral
def f(z):
    # undefined at zero and one, but value approaches zero from graph
    if z == 0 or z == 1:
        return 0
    else:
        return (((z/(1 - z))**3) / ((np.exp(z/(1 - z))) - 1)) * (1/(1-z)**2)


# using trapezoidal rule to approximate the integral from 0-1 with n slices
def trap_approx(n):
    # hardcoded values because this function just approximates one function
    a = 0
    b = 1

    h = (b - a) / n
    area = 0

    # Because we start at 1, to get the loop to run for all values,
    # the upper limit must be +1
    for k in range(1, n):
        area += f(a + (k * h))

    area += (1 / 2) * (f(a) + f(b))
    area *= h
    return area


def main():
    est = trap_approx(100)
    print("The approximated area with n=100 is: " + str(est))

    stefboltz = est*((kb**4) / (4*(np.pi**2)*(c**2)*(hbar**3)))
    print("Estimated Stefan-Boltzmann Constant: " + str(stefboltz))


main()
