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
    residuals_lsq1 = least_squares(residuals_fun, init, loss='soft_l1', f_scale=0.5, args=(ADC1, distance))

    # plot results
    plt.figure('Sensor 1')
    ADC1_max = int(np.amax(ADC1))
    ADC1_min = int(np.amin(ADC1))
    plt_sens1_x = np.linspace(ADC1_min, ADC1_max, 10000)
    plt_sens1_y = generate_data(plt_sens1_x, *residuals_lsq1.x)
    plt.plot(plt_sens1_x, plt_sens1_y, label='ADC Robust Least Squares Estimation')
    plt.plot(ADC1, distance, 'o', label='Measured Data')
    plt.xlabel('ADC Voltage Values')
    plt.ylabel('Distance From Sensor to Object (CM)')
    plt.legend(loc='upper right')
    plt.savefig("Sensor1.png")

    # Repeat for other sensors

    residuals_lsq2 = least_squares(residuals_fun, init, loss='soft_l1', f_scale=0.5, args=(ADC2, distance))

    plt.figure('Sensor 2')
    ADC2_max = int(np.amax(ADC2))
    ADC2_min = int(np.amin(ADC2))
    plt_sens2_x = np.linspace(ADC2_min, ADC2_max, 10000)
    plt_sens2_y = generate_data(plt_sens2_x, *residuals_lsq2.x)
    plt.plot(plt_sens2_x, plt_sens2_y, label='ADC Robust Least Squares Estimation')
    plt.plot(ADC2, distance, 'o', label='Measured Data')
    plt.xlabel('ADC Voltage Values')
    plt.ylabel('Distance From Sensor to Object (CM)')
    plt.legend(loc='upper right')
    plt.savefig("Sensor2.png")

    # For second graphs where the length of the ADC data is shorter, only use the corresponding
    # values from distance (first 22 values)
    residuals_lsq3 = least_squares(residuals_fun, init, loss='soft_l1', f_scale=0.5, args=(ADC3, distance[:21]))

    plt.figure('Sensor 3')
    ADC3_max = int(np.amax(ADC3))
    ADC3_min = int(np.amin(ADC3))
    plt_sens3_x = np.linspace(ADC3_min, ADC3_max, 10000)
    plt_sens3_y = generate_data(plt_sens3_x, *residuals_lsq3.x)
    plt.plot(plt_sens3_x, plt_sens3_y, label='ADC Robust Least Squares Estimation')
    plt.plot(ADC3, distance[:21], 'o', label='Measured Data')
    plt.xlabel('ADC Voltage Values')
    plt.ylabel('Distance From Sensor to Object (CM)')
    plt.legend(loc='upper right')
    plt.savefig("Sensor3.png")

    residuals_lsq4 = least_squares(residuals_fun, init, loss='soft_l1', f_scale=0.5, args=(ADC4, distance[:21]))

    plt.figure('Sensor 4')
    ADC4_max = int(np.amax(ADC4))
    ADC4_min = int(np.amin(ADC4))
    plt_sens4_x = np.linspace(ADC4_min, ADC4_max, 10000)
    plt_sens4_y = generate_data(plt_sens4_x, *residuals_lsq4.x)
    plt.plot(plt_sens4_x, plt_sens4_y, label='ADC Robust Least Squares Estimation')
    plt.plot(ADC4, distance[:21], 'o', label='Measured Data')
    plt.xlabel('ADC Voltage Values')
    plt.ylabel('Distance From Sensor to Object (CM)')
    plt.legend(loc='upper right')
    plt.savefig("Sensor4.png")

    # plt.show()

main()

