import numpy as np




GRAV_CONST = 6.67*(10**-11)
EARTH_MASS = 5.97*(10**24)
EARTH_RAD = 6371 # km

def main():
    # Calculate height for geosynchronous orbit
    partC()

    # Get user input (Time for satellite to orbit once)
    T = input("Please enter orbit time (T in seconds)(q to quit): ")
    if T == "q":
        print("Have a good day!")
    else:
        h = calcH(int(T))
        print("The altitude that satellite must orbit at is: " + str(h))
    return 0

def partC():
    daySec = 24*60*60
    hDay = calcH(daySec)
    print("The height for a satellite that orbits once a day is: " + str(hDay))

    mins1 = 90*60
    mins2 = mins1 / 2

    h1 = calcH(mins1)
    h2 = calcH(mins2)

    print("For a satellite that orbits every 90 mins: " + str(h1))
    print("For a satellite that orbits every 45 mins: " + str(h2))



def calcH(time):
    h = ((GRAV_CONST * EARTH_MASS * (time**2)) / (4*(np.pi**2)))**(1/3) - (EARTH_RAD * 1000)
    return h

main()