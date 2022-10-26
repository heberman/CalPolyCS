from landerFuncs import *

def main():
    showWelcome()
    altitude = getAltitude()
    fuel = getFuel()
    time = 0
    acceleration = 0
    velocity = 0
    fuelRate = 0
    print("\nLM state at retrorocket cutoff")
    displayLMState(time, altitude, velocity, fuel, fuelRate)

    while altitude > 0:
        if fuel > 0:
            fuelRate = getFuelRate(fuel)
        time += 1
        acceleration = updateAcceleration(1.62, fuelRate)
        altitude = updateAltitude(altitude, velocity, acceleration)
        velocity = updateVelocity(velocity, acceleration)
        if fuel == fuelRate:
            fuel = 0
            fuelRate = 0
            if altitude > 0:
                print("OUT OF FUEL - Elasped Time:{:>4}".format(time), "Altitude:{:>8.2f}".format(altitude), "Velocity:{:>8.2f}".format(velocity))
        else:
            fuel = updateFuel(fuel, fuelRate)
            if altitude > 0:
                displayLMState(time, altitude, velocity, fuel, fuelRate)

    print("\nLM state at landing/impact")
    displayLMState(time, altitude, velocity, fuel, fuelRate)
    displayLMLandingStatus(velocity)

if __name__ == '__main__':
   main()