from funcs import *

def main():
  weightSkater= float(input("How much do you weigh (pounds)? "))
  distance= float(input("How far away is your professor (meters)? ")) 
  object= input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock,\
	 (l)ight saber, or lawn (g)nome? ")
  mass= getMassObject(object)
  velSkater= getVelocitySkater(poundsToKG(weightSkater), mass, getVelocityObject(distance))
  comment=""
 
  if mass <= 0.1:
    comment="You're going to get an F!"
  elif mass > 0.1 and mass <= 1.0:
    comment="Make sure your professor is OK."
  else: 
    if distance < 20: 
       comment= "How far away is the hospital?"
    else: 
       comment= "RIP professor." 

  print("\nNice throw! ",comment) 
  print("Velocity of skater: %.3f m/s " % (velSkater))

  if velSkater < .2:
     print("My grandmother skates faster than you!")
  elif velSkater >= 0.2 and velSkater < 1.0: 
     print("") 
  else:
     print("Look out for that railing!!!")

if __name__ == '__main__':
   main()
