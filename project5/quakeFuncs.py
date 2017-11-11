from urllib.request import *
from json import *
from datetime import *
from operator import *
from utility import *
# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
def displayData(quakes): #passing in quakes, from readQuakesfromFile
	print()
	print("Earthquakes:")
	print("------------")
	
	for Earthquake in quakes:
		print("({:.2f})".format(Earthquake.mag), "{:>40s}".format(Earthquake.place), " at ", time_to_str(Earthquake.time), "({:.3f}".format(Earthquake.longitude)+","+ " {:.3f}".format(Earthquake.latitude)+")")
	print()
	print("Options:")
	print("  (s)ort")
	print("  (f)ilter")
	print("  (n)ew quakes")
	print("  (q)uit")
	print()	

# Add Earthquake class definition here   
class Earthquake:
	def __init__(self, place, mag, longitude, latitude, time):
		#place - string, mag- float, long- float, lat-float, time-int
		self.place = place
		self.mag = mag
		self.longitude = longitude
		self.latitude = latitude
		self.time = time
	
	def __eq__(self, other):
		if (self.place == other.place and
			epsilon_equal(self.mag, other.mag) and
			epsilon_equal(self.longitude, other.longitude) and
			epsilon_equal(self.latitude, other.latitude) and
			self.time == other.time):
				return True
		else:
				return False
	
# Required function - implement me!   
def read_quakes_from_file(filename):
	earthList = [ ] #list of Earthquake objects
	inFile = open(filename, "r")

	for line in inFile:
		listSplit = line.split() #[2.19, -121.5801697, 36.......] list of strings
		mag = float(listSplit[0])
		longitude = float(listSplit[1])
		latitude = float(listSplit[2])
		time = int(listSplit[3])
		place = ' '.join(listSplit[4:]) 
		earthList.append(Earthquake(place, mag, longitude, latitude, time))

	inFile.close()

	return earthList    

# Required function - implement me!
def sortByMagnitude(quakes): #descending order, SORT 
    sortedList =  sorted(quakes, key=lambda earthquake: earthquake.mag, reverse=True)
    return sortedList
    #sortedList = quakes.sort(key= lambda x: x.mag, reverse = True) #sorts by magnitude

def sortByTime(quakes): #descending order, SORT
    sortedList =  sorted(quakes, key=lambda earthquake: earthquake.time, reverse=True)
    return sortedList

def sortByLong(quakes): #asceding order, SORT
    sortedList =  sorted(quakes, key=lambda earthquake: earthquake.longitude)
    return sortedList

def sortByLat(quakes): #ascendingg order, SORT
    sortedList =  sorted(quakes, key=lambda earthquake: earthquake.latitude)
    return sortedList
                                 
# Required function - implement me!
def filter_by_place(quakes, word):  #check 
    sortedList = []
    word = word.lower()
    for e in quakes:
       place = e.place.lower()
       if word in place:
          sortedList.append(e)
    return sortedList


def filter_by_mag(quakes, low, high):
	sortedList = []
	low = float(low)
	high = float(high)
	for e in quakes:
		 if e.mag >= low and e.mag <=  high:
			 sortedList.append(e)
	return sortedList

# Required function for final part - implement me too!   
def quake_from_feature(feature):
	
	place = feature["properties"]["place"]
	longitude = feature["geometry"]["coordinates"][0]
	latitude = feature["geometry"]["coordinates"][1]
	mag = feature["properties"]["mag"]
	time = feature["properties"]["time"]
	time = time//1000 #to seconds
	#print("place")
	#print(place)
	quake = Earthquake(place, mag, longitude, latitude, time)
	return quake

def stringForm(eq):
	list = [ ]
	list.append(str(eq.mag))
	list.append(str(eq.longitude))
	list.append(str(eq.latitude))
	list.append(str(eq.time))
	list.append(eq.place)

	string =' '.join(list)

	return string




   
