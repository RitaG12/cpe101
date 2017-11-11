from landerFuncs import *

def main():
   elapsedTime=0
   velocity=0.00
   fuelRate=0
   gravity= 1.62

   showWelcome()
   altitude = getAltitude()
   currentFuel = getFuel()

   print("\nLM state at retrorocket cutoff")
  
#fuel rate-20, wrong altitude values, etc, use up amount of fuel exactly. 10 
   while altitude > 0:
       if currentFuel > 0: #changed from 0 to 1
          displayLMState(elapsedTime, altitude, velocity, currentFuel, fuelRate)
          print()
          fuelRate = getFuelRate(currentFuel)
          acceleration = updateAcceleration(gravity, fuelRate)
          altitude = updateAltitude(altitude, velocity, acceleration)
          velocity = updateVelocity(velocity, acceleration)
          currentFuel = updateFuel(currentFuel, fuelRate)
       else:
          print("OUT OF FUEL - Elapsed Time: %3d Altitude: %7.2f Velocity: %7.2f" %(elapsedTime, altitude, velocity))
          fuelRate = 0
          acceleration = updateAcceleration(gravity, fuelRate)
          altitude = updateAltitude(altitude, velocity, acceleration)
          velocity = updateVelocity(velocity, acceleration)
          currentFuel = updateFuel(currentFuel, fuelRate)
       elapsedTime += 1

   print("\nLM state at landing/impact")
   displayLMState(elapsedTime, altitude, velocity, currentFuel, fuelRate)
   print()
   displayLMLandingStatus(velocity)

if __name__ == "__main__":
   main()
