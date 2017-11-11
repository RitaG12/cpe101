from quakeFuncs import *

def main():
	earthquakeList = read_quakes_from_file('quakes.txt')
	displayData(earthquakeList)
	choice = ""
	
	while choice != 'q':
		choice  = input("Choice: ")
		choice = choice.lower()
            
		if choice == "s":
			
			sortBy = input("Sort by (m)agnitude), (t)ime, (l)ongitude, l(a)titude? ")
			print()
			if sortBy == 'm':
				displayData(sortByMagnitude(earthquakeList)) #ends whole thing here.
			elif sortBy == 't':
				displayData(sortByTime(earthquakeList))
            elif sortBy == 'l':
                displayData(sortByLong(earthquakeList))
            else:
                displayData(sortByLat(earthquakeList))

    #elif nextFunction == "f" :
        #filterBy = input("Filter by (m)agnitude or (p)lace? ")
        #if filterBy == 'p':
            #searchString = input("Search for what string? ")
#else m
        #else:
            #lower = int("Lower bound: ")
            #upper = int("Upper bound ")
    #elif nextFunction == "n":
#else next is q
    #else:
#quit



if __name__ == "__main__":
		main()


