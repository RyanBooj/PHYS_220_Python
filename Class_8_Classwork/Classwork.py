import numpy as np
import matplotlib.pyplot as plt

# calculating a derivative using the definition of a derivative

# define a function
def f(x):
    return x*(x-1)

def derivative(x, delta):
    dfdx = (f(x+delta) - f(x)) / delta
    return dfdx

def derivTest():
    vals = []
    actual = 1
    delta = 10 ** -2

    for i in range(0, 6):
        deriv = derivative(1, delta)
        print(deriv)
        vals.append(((deriv - actual) / actual) * 100)
        delta = delta * (10 ** -2)

    # plot percent error
    plt.figure(1)
    plt.plot(vals)
    # plt.show()

def yk(x):
    return np.sqrt(1-x**2)

def integral(N):
    h = 2/N
    area = 0
    for k in range(1, N+1):
        xk = -1 + h*k
        y = yk(xk)
        area = area + y*h
    return area

def main():
    # derivTest()

    print("Expected (pi/2): " + str(np.pi/2))
    for i in [100, 1000, 10000, 100000, 1000000]:
        print(integral(i))

main()