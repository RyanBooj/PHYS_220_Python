import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# function to be integrated in Bessel function approximation
def fnct(m, x, theta):
    return np.cos((m * theta) - (x * np.sin(theta)))


# Fit three points with a polynomial curve to approximate the area under that curve
# Need three points for each "slice"
# Each point, x, gets these three points by: [a, a+h, a+2h], [a+2h, a+3h, a+4h], ...
# Area under these three points given by: (1/3)h[f(a)+4f(a+h)+f(a+2h) + f(a+2h)+4f(a+3h)+f(a+4h)...]
#                                       = (1/3)h[f(a+(n-2)h + 4f(a+(n-1)h+f(b)]
# Finally:                      I(a, b) = (1/3)h[f(a) + f(b) + 4sum[k=1->(n/2)](f(a+(2k-1)h) + 2sum[k=1->n-1](f(a+2kh))
def J(m, x):
    # number of slices for simpson's rule
    N = 1000

    # defining bounds for integral
    a = 0
    b = np.pi

    # define area
    area = 0

    # calculate the parts with no coefficients
    h = (b - a) / N
    area += fnct(m, x, a) + fnct(m, x, b)

    # calculate the parts with coefficients of 4
    sum = 0
    for k in range(1, (N // 2) + 1):
        sum += fnct(m, x, a + ((2 * k) - 1) * h)
    area += 4 * sum

    # calculate the parts with coefficients of 2
    sum = 0
    for k in range(1, (N // 2)):
        sum += fnct(m, x, a + (2 * k * h))
    area += 2 * sum

    # multiply result by (h/3) and return
    area *= (1 / 3) * h
    return area


def plot_bessel():
    # define variables for each graph
    y_vals0 = []
    y_vals1 = []
    y_vals2 = []

    # calculate the approximations of each function
    for i in range(21):
        y_vals0.append(J(0, i))
        y_vals1.append(J(1, i))
        y_vals2.append(J(2, i))

    # plot results
    plt.figure(1)
    plt.plot(y_vals0, label='J0')
    plt.plot(y_vals1, label='J1')
    plt.plot(y_vals2, label='J2')
    plt.legend()
    plt.savefig('bessel_functions.png')

# Defining the intensity function
def intensity(r):
    # wavelength of light source
    lmda = 500  # in unit nm
    lmda /= 1000  # convert to micrometers
    k = (2*np.pi) / lmda
    m = 1

    # function
    return (J(1, k*r) / (k*r))**2

# n is number of samples from 0 to 1 um
def plot_intensity(n):
    # making a picture of intensity of light source from 0 to 1um (distance from source)
    # need 2D array to store intensity values at each point
    image = np.zeros([n, n], np.float)

    # separation of pixels - made so that edges are 1um from center
    resolution = (n/2) * (10**-6)
    x = 0
    y = 0
    # loop through all values and set 'pixel' to intensity(distance_from_center) brightness
    for i in range(n):
        x = (i - (n / 2)) * resolution
        for j in range(n):
            # need to make the center of the image in the middle - default would be upper left corner
            y = (j - (n/2)) * resolution
            distance = np.sqrt(x**2 + y**2)
            if distance == 0:
                image[i, j] = intensity(0.1 * (10**-10))
            else:
                image[i, j] = intensity(distance)

    plt.figure(2)
    plt.imshow(image, cmap='hot')
    plt.gray()
    # plt.show()
    plt.savefig('diffraction.png')




def main():
    plot_bessel()
    plot_intensity(100)


main()
