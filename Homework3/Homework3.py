import numpy as np
import matplotlib.pyplot as plt

# Semi-Empirical mass formula constants
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2
# a5 needs to be calculated


def calcA5(A, Z):
    if A % 2 == 1:
        return 0
    elif Z % 2 == 0:
        return 12.0
    else:
        return -12.0

# Part A - total binding energy
def calcBindEnergyA(A, Z):
    # Call function to calculate a5
    a5 = calcA5(A, Z)

    # calculate binding energy from given formula
    B = a1*A - a2*(A**(2/3)) - a3*(Z**2 / A**(1/3)) - a4*((A-2*Z)**2 / A) + a5/A**(1/2)
    return B

    # This code correctly calculates the binding energy of an atom. The expected answer was approximately
    # 490 MeV, and the code gave the answer of ~493.94 MeV.

# Part B - energy per nucleon
def calcBindEnergyB(A, Z):
    # Call function to calculate a5
    a5 = calcA5(A, Z)

    # calculate binding energy from given formula
    B = a1 * A - a2 * (A ** (2 / 3)) - a3 * (Z ** 2 / A ** (1 / 3)) - a4 * ((A - 2 * Z) ** 2 / A) + a5 / A ** (1 / 2)
    return B / A

    # This code correctly calculates the binding energy for an atomic nucleus with atomic number Z and mass Number B.

def calcBindEnergyC(Z, showGraph=True):
    # declare array to store all binding energy values
    energyVals = []
    atomicNums = []
    energyPerNuc = []
    for A in range(Z, 3*Z):
        # Call function to calculate a5
        a5 = calcA5(A, Z)

        # calculate binding energy from given formula
        B = a1 * A - a2 * (A ** (2/3)) - a3 * (Z ** 2 / A ** (1/3)) - a4 * ((A - 2 * Z) ** 2 / A) + a5 / A ** (1/2)
        energyVals.append(B)
        atomicNums.append(A)
        energyPerNuc.append([B/A, A])
    if showGraph:
        plt.figure(1)
        plt.plot(atomicNums, energyVals, 'ro')
        plt.show()

    # return the most stable nucleus
    return np.amax(energyPerNuc, axis=0)

    # This code creates a graph that plots the values of A, the atomic mass number, and B, the nuclear binding energy.
    # The graph shows that as A increases, the binding energy initially increases, but levels out quickly.
    # This function also finds the most stable nucleus for a given atomic mass value.

def calcBindEnergyD():
    # call calcBindEnergyC with Z from 1-100
    maxBindingAtomicNum = 0
    largestBindEnergy = 0
    for Z in range(1, 101):
        mostStableBinds = calcBindEnergyC(Z, False)
        print("The most stable nucleus is mass number: " + str(mostStableBinds[1]), end="")
        print(" for the atomic number " + str(Z))

        # Find the largest binding energy and store the value of Z that it occurs at
        if Z==1:
            largestBindEnergy = mostStableBinds[0]
        else:
            if largestBindEnergy < mostStableBinds[0]:
                largestBindEnergy = mostStableBinds[0]
                maxBindingAtomicNum = Z

    print("The maximum binding energy occurs at atomic number: " + str(maxBindingAtomicNum))


def main():
    print("-----------------------------------------------------------------------------------------")
    print("The binding energy for an atom with mass number 58 and atomic number 28")
    print(calcBindEnergyA(58, 28))

    print("-----------------------------------------------------------------------------------------")
    print("The binding energy per nucleon for an atom with mass number 58 and atomic number 28")
    print(calcBindEnergyB(58, 28))

    print("-----------------------------------------------------------------------------------------")
    stable = calcBindEnergyC(28)
    print("The most stable nucleus is atomic number: " + str(stable[1]))
    print("This nucleus has a binding energy per nucleon of: " + str(stable[0]))

    print("-----------------------------------------------------------------------------------------")
    calcBindEnergyD()


main()
