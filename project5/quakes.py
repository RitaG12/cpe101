from quakeFuncs import *

def main():
	earthquakeList = read_quakes_from_file('quakes.txt')
	displayData(earthquakeList)
	choice = ""
	
	while choice != 'q':
		choice  = input("Choice: ")
		choice = choice.lower()
            
		if choice == "s":
			sortBy = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
			sortBy = sortBy.lower()
			print()
			if sortBy == 'm':
				earthquakeList = sortByMagnitude(earthquakeList)
				displayData(earthquakeList) #ends whole thing here.
			elif sortBy == 't':
				earthquakeList = sortByTime(earthquakeList)
				displayData(earthquakeList)
			elif sortBy == 'l':
				earthquakeList = sortByLong(earthquakeList)
				displayData(earthquakeList)
			elif sortBy == 'a':
				earthquakeList = sortByLat(earthquakeList)
				displayData(earthquakeList)

		elif choice == "f" :
			filterBy = input("Filter by (m)agnitude or (p)lace? ")
			filterBy = filterBy.lower()
			if filterBy == 'p':
				searchString = input("Search for what string? ")
				print()
				searchString = searchString.lower()
				displayData(filter_by_place(earthquakeList, searchString))
			elif filterBy == 'm':
				lower = input("Lower bound: ")
				upper = input("Upper bound: ")
				displayData(filter_by_mag(earthquakeList, lower, upper))

		elif choice == "n":
			dict = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
			features = dict["features"]
			
			newEqs = False
			for feature in features:
				eq = quake_from_feature(feature)
				if eq not in earthquakeList:
					earthquakeList.append(eq)
					newEqs = True
			if newEqs:
				print("New quakes found!!!")
				displayData(earthquakeList)
	
#rewrite file
	inFile = open('quakes.txt', 'w')
	for e in earthquakeList:
		eqData = stringForm(e) #want to write these into the file & reply 
		inFile.write(eqData+'\n')

	inFile.close()


if __name__ == "__main__":
		main()


