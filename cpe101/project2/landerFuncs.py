# Project 2 - Moonlander
#
# Name: Henry Berman
# Instructor: Hatalsky

def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator\n")
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.\n")
   print("   Good luck and may the force be with you!\n")

def getFuel():
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))

   while fuel < 1 or fuel > 9999:
      print("ERROR: Amount of fuel must be positive, please try again")
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))

   return fuel

def getAltitude():
   alt = int(input("Enter the initial altitude of the LM (in meters): "))

   while alt < 1 or alt > 9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      alt = int(input("Enter the initial altitude of the LM (in meters): "))

   return alt
   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print("Elapsed Time:", "{:>4} s".format(elapsedTime))
   print("        Fuel:", "{:>4} l".format(fuelAmount))
   print("        Rate:", "{:>4} l/s".format(fuelRate))
   print("    Altitude:", "{:>7.2f} m".format(altitude))
   print("    Velocity:", "{:>7.2f} m/s".format(velocity))

def getFuelRate(currentFuel):
   fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))

   while fuelRate < 0 or fuelRate > 9:
      print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
      fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))

   if currentFuel > fuelRate:
      return fuelRate
   else:
      return currentFuel

 
def updateAcceleration(gravity, fuelRate):
   return gravity * ((fuelRate/5) - 1)

def updateAltitude(altitude, velocity, acceleration):
   alt = altitude + velocity + (acceleration/2)

   if alt > 0:
      return alt
   else:
      return 0

def updateVelocity(velocity, acceleration):
   return velocity + acceleration

def updateFuel(fuel, fuelRate):
   return fuel - fuelRate

def displayLMLandingStatus(velocity):
   if (velocity <= 0 and velocity >= -1):
      print("Status at landing - The eagle has landed!")
   elif (velocity < -1 and velocity > -10):
      print("Status at landing - Enjoy your oxygen while it lasts!")
   else:
      print("Status at landing - Ouch - that hurt!")
