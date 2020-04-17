import numpy as np
import matplotlib.pyplot as plt
import random as rand

MOVE_DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# returns an array that adds or subtracts to the x and y values
def rand_move():
    # get random number from 0-3
    choice = (rand.randrange(4))
    shift_val = MOVE_DIR[choice]
    return shift_val

def main():
    # define grid size with L
    L = 101
    # define position variables - start at the middle of the grid
    i = L // 2
    j = L // 2
    current_coords = [i, j]
    # Define number of moves to make
    N = 10000

    # define lists to store the coordinates of the moves - move 1000 times
    x = np.zeros(N)
    y = np.zeros(N)

    # define a color for each of three particles and define plot
    colors = ['g', 'r', 'y']
    plt.figure(1)
    plt.xlim(0, L)
    plt.ylim(0, L)

    # repeat for three particles with a different color
    for k in range(3):
        for i in range(N):
            shift = rand_move()
            current_coords = np.add(current_coords, shift)
            # make sure random move doesnt take the coordinates larger than 101 or less than 0
            # if the move attempted to go out of bounds, nothing happens
            if current_coords[0] > L:
                current_coords[0] -= 1
            elif current_coords[0] < 0:
                current_coords[0] += 1
            elif current_coords[1] > L:
                current_coords[1] -= 1
            elif current_coords[1] < 0:
                current_coords[1] += 1

            x[i] = current_coords[0]
            y[i] = current_coords[1]

        plt.plot(x, y, colors[k])

    # plt.show()
    plt.savefig("random_3walks.png")

main()

