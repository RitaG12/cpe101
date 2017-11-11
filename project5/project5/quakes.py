from quakeFuncs import *

def main():
    earthquakeList = read_quakes_from_file(quakes.txt)
    displayData(earthquakeList)
    
    #e1 = Earthquake('122km SSE of Chignik Lake, Alaska', 4.5, -157.822,55.2888 ,1488211648 )
    
    #quakes = [e1]
#   result = "(4.50)        122km SSE of Chignik Lake, Alaska at 2017-02-27 08:07:28 (-157.822, 55.289)"

if __name__ == "__main__":
		main()


