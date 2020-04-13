import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def read_data():
    # initialize lists for data
    distance = []  # distance from object in centimeters
    ADC1 = np.array([])  # analog to digital converter values that corresponded to the distance measured in 'distance'
    ADC2 = np.array([])  # Each ADC list contains data from one of the four sensors, which were all used to calculate
    ADC3 = np.array([])  # the distance in distance
    ADC4 = np.array([])

    # opening the file
    file_object = open("MM_sensors_data.txt", "r")

    # there are 73 lines in the file
    k = 0
    while k < 73:
        # read in a line and store the data in the appropriate list
        current_line = file_object.readline()
        data_vals = current_line.split()
        for i in range(len(data_vals)):
            if i == 0:
                distance = np.append(distance, float(data_vals[i]))
            elif i == 1:
                ADC1 = np.append(ADC1, int(data_vals[i]))
            elif i == 2:
                ADC2 = np.append(ADC2, int(data_vals[i]))
            elif i == 3:
                ADC3 = np.append(ADC3, int(data_vals[i]))
            else:
                ADC4 = np.append(ADC4, int(data_vals[i]))
        k += 1
    file_object.close()
    return distance, ADC1, ADC2, ADC3, ADC4


# residuals function
# of the form: (c1*x + c2) / (x^2 + c3*x + c4)
def residuals_fun(x, t, y):
    return ((x[0] * t) + x[1]) / (t ** 2 + (x[2] * t) + x[3]) - y


def generate_data(t, x1, x2, x3, x4):
    return ((x1 * t) + x2) / (t ** 2 + (x3 * t) + x4)


def main():
    # read in sensor data from file
    distance, ADC1, ADC2, ADC3, ADC4 = read_data()

    # Estimations happening here
    # initial estimate is 4 1's (4 coefficients in residuals_fun)
    init = np.ones(4)

    # Robust least squares optimization
    residuals_lsq = least_squares(residuals_fun, init, loss='soft_l1', f_scale=0.5, args=(ADC1, distance))

    # plot result
    plt.figure('Sensor 1')
    ADC1_max = int(np.amax(ADC1))
    ADC1_min = int(np.amin(ADC1))
    plt_sens1_x = np.linspace(ADC1_min, ADC1_max, 10000)
    plt_sens1_y = generate_data(plt_sens1_x, *residuals_lsq.x)
    plt.plot(plt_sens1_x, plt_sens1_y, label='ADC Robust Least Squares Estimation')
    plt.plot(ADC1, distance, 'o', label='Measured Data')
    plt.xlabel('ADC Voltage Values')
    plt.ylabel('Distance From Sensor to Object (CM)')
    plt.legend(loc='upper right')

    plt.show()


main()

