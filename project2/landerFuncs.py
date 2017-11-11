# Project 2 - Moonlander
# Author: Rutu Samai
# Version:

def showWelcome():
    print("\nWelcome aboard the Lunar Module Flight Simulator\n")
    print("   To begin you must specify the LM's initial altitude")
    print("   and fuel level.  To simulate the actual LM use")
    print("   values of 1300 meters and 500 liters, respectively.\n")
    print("   Good luck and may the force be with you!\n")


def getFuel():
    fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while (fuel <= 0):
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    return fuel


def getAltitude():
    alt = float(input("Enter the initial altitude of the LM (in meters): "))
    while (alt < 1 or alt > 9999):
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
        alt = float(input("Enter the initial altitude of the LM (in meters): "))
    return alt


def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    # print("LM state at retrorocket cutoff") #print in main
    print("Elapsed Time:%5d s" % elapsedTime)
    print("        Fuel:%5d l" % fuelAmount)
    print("        Rate:%5d l/s" % fuelRate)
    print("    Altitude:%8.2f m" % altitude)
    print("    Velocity:%8.2f m/s" % velocity)


def getFuelRate(currentFuel):  # fix!!!?
    fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    while (fuelRate < 0 or fuelRate > 9):
        print("ERROR: Fuel rate must be between 0 and 9, inclusive")
        print()
        fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    if (fuelRate < currentFuel):
        return int(fuelRate)
    else:
        return currentFuel


def updateAcceleration(gravity, fuelRate):  # check
    return gravity * ((float(fuelRate) / 5) - 1)


def updateAltitude(altitude, velocity, acceleration):  # check
    alt = (altitude) + (velocity) + ((acceleration) / 2)
    if(alt >= 0):
        return alt
    else:
        return 0
    # non negative numbers


def updateVelocity(velocity, acceleration):
    return velocity + acceleration


def updateFuel(fuel, fuelRate):
    return fuel - fuelRate


def displayLMLandingStatus(velocity):
    if (-1 <= velocity <= 0):
        print("Status at landing - The eagle has landed!")
    elif (-10 < velocity < -1):
        print("Status at landing - Enjoy your oxygen while it lasts!")
    else:
        print("Status at landing - Ouch - that hurt!")
