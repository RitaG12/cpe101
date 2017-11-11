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

	print("Earthquakes:")
	print("------------")
	for Earthquake in quakes:
		print("({:.2}) {:>40} at {:} ({3:.3}, {3:.3})".format(Earthquake.mag, Earthquake.place, Earthquake.time, Earthquake.place))
	print()
	print("Options:")
	print("  (s)ort")
	print("  (f)ilter")
	print("  (n)ew quakes")
	print("  (q)uit")

	


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
def filter_by_mag(quakes, low, high):
   pass       
     
# Required function - implement me!
def filter_by_place(quakes, word):   
   pass

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   pass
     


   
