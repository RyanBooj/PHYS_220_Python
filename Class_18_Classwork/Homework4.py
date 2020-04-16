import numpy as np
import random as rand
import matplotlib.pyplot as plt

# Question 1: Using the Monte Carlo Method to compute Pi
# and plotting results against actual value of np.pi


# Estimate Pi by finding the area of a semi-circle with a known area
# inside of a rectangle of known area
# Defining Function to plot unit circle
# Rectangle will be -radius <= x <= radius, 0 <= y <= radius (Area = (radius*2)*radius)
def f_semi(x, radius=1):
    return np.sqrt(radius**2 - x**2)


# Function to estimate the area using monte carlo with N random points
# pass a value of radius to change the size of the area to be estimated
# (larger areas may give better approximations, default=1)
# returns the ratio of number of points below to total number of points
def monte_carlo(N, radius=1):
    # count variable tracks number of points below function
    count = 0

    # Loop to generate random points
    for i in range(N):
        # x between -1 and 1, y between 0 and 1
        x = rand.randrange(-radius, radius)
        y = rand.randrange(radius)

        # Check if random point is inside function
        if y < f_semi(x, radius):
            count += 1

    return count/N


# Function to plot the estimation of the value of pi using N from 10-1000
# and a semicircle with a radius of 4
def plot_estimation(N=1000, radius=4):
    # define radius of semicircle and bounding area

    bound_area = (radius*2)*radius
    x = np.arange(10, N+10, 10)
    x = x.astype(int)
    y = np.array([])
    for i in range(np.size(x)):
        y = np.append(y, monte_carlo(x[i], radius))

    # area_semicircle = (pi*r**2) / 2
    # Make the y values the value of pi by multiplying by (2 * bound_area) / (radius**2)
    y = np.multiply(y, (2 * bound_area) / (radius**2))

    # Plot the value of Pi estimated with each number of points
    plt.figure('Number of Random Points vs Estimation Value')
    plt.plot(x, y)
    plt.xlabel('Amount of Random Guesses')
    plt.ylabel('Value of Estimation')

    plt.savefig('estimation.png')
    # Plot the difference between np.pi and the estimated value per
    # number of points
    plt.figure('Difference Between Pi and Estimation')
    difference = np.subtract(y, np.pi)
    difference = np.absolute(difference)

    plt.plot(x, difference)
    plt.xlabel('Amount of Random Guesses')
    plt.ylabel('Discrepancies between Actual and Estimation')
    plt.ylim(bottom=0)
    plt.savefig('difference.png')
    plt.show()

def main():
    # Estimate with 10000 points
    # Area of Shape = (count*Bound_Area)/(N)
    # ratio = monte_carlo(10000)
    # area = ratio*8
    #
    # # area_semi = (pi*(r**2)) / 2
    # # radius of this semicircle is 2
    # pi_est = (area / 2)

    plot_estimation(10000)
    # By increasing the area of the shape that I measured, the accuracy of the
    # estimation increased significantly
    # plot_estimation(10000, 100)


main()

# Question 1 Response:
# Based on the results of my second plot, the difference between the numpy library's
# value for pi and the value that my monte carlo function estimated decreases significantly
# when increasing the number of points from 10 to around 1000. After this initial increase
# in accuracy, the estimations do not continue to become more accurate however. The difference
# between the estimated value and the actual value stays almost constant between 0.1 and 0.2.
# This could be because the monte carlo method relies on random numbers, and the accuracy of the
# estimation is not only a function of the amount of data points used, but is also based on the
# values of the random numbers that are generated. If the random numbers that are generated tend
# more towards values that are below the function curve, then the value of pi will be estimated
# too large and visa versa. One way that I found to reduce the difference between the  estimated
# value and the actual value was to increase the radius of the semi-circle that I was estimating.
# Increasing the area from 4 to 100 significantly reduced the difference between my estimation and
# the actual value. This could be due to the random number generator favoring either large numbers
# or small numbers, and by increasing the radius, all the numbers became large, increasing the accuracy.
