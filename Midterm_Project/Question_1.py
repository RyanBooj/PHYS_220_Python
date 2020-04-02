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
    return (s_up(N) - s_down(N)) / (abs(s_up(N)) + abs(s_down(N)))

# function to plot n terms
def plot_n_vals(n):
    y_vals = []
    x_vals = []
    for i in range(1, n+1):
        x_vals.append(i)
        y_vals.append(get_y_vals(i))

    plt.figure(1)
    plt.loglog(x_vals, y_vals)
    plt.show()


# main function, calling plot function with different values
def main():
    plot_n_vals(100)
    plot_n_vals(1000)

main()
