import matplotlib.pyplot as plt


# function being used
def f(n):
    return 1 / n


# calculate s_up
def s_up(N):
    # create a list from 1 to N
    indexes = list(range(1, N + 1))
    result = 0

    # for each number in the list, calculate sum(n=1 -> N)(1/n)
    for i in range(N):
        result += f(indexes[i])

    return result


# calculate s_down
def s_down(N):
    # create a list from 1 to N
    indexes = list(range(1, N + 1))
    result = 0

    # for each number in the list, starting with the largest number, calculate sum(n=N -> 1)(1/n)
    for i in range(N - 1, -1, -1):
        result += f(indexes[i])

    return result


# Function to get the values that need to be graphed on the y-axis
def get_y_vals(N):
    up = s_up(N)
    down = s_down(N)
    return (up - down) / (abs(up) + abs(down))


# function to plot n terms
def plot_n_vals(n):
    y_vals = []
    x_vals = []
    for i in range(1, n + 1):
        x_vals.append(i)
        y_vals.append(get_y_vals(i))

    plt.figure(1)
    plt.loglog(x_vals, y_vals)
    plt.show()


# main function, calling plot function with different values
def main():
    plot_n_vals(100)
    plot_n_vals(1000)

    # may take a couple of seconds to compute
    plot_n_vals(10000)


main()
# Question 1 response:

# The graphs show the difference between the accuracy of the calculations. When
# the program is run with smaller values of N, the difference is small, shown by
# only a single spike in the function. But when larger values of N are given,
# the spike steadily increase in magnitude. This can be explained by the downward
# sum being more precise than the upward sum. This is because of the way that Python
# rounds floating point numbers. More specifically, Python has a limited number
# of significant digits and when the sum reaches a certain point, the floating
# point number representing the sum needs to store one more digit than it is able to.
# This causes Python to round the number so it can be stored. When computing s_down
# this rounding happens at a different operation than when computing s_up. This results
# in s_down being able to store most of the smaller sums (since it starts summing from
# larger values of N first) to a greater degree of precision. Therefore, since s_up loses
# this extra degree of precision quickly since its sum will be larger for most of the
# calculation, s_down has a small advantage in precision when dealing with large values
# of N.
