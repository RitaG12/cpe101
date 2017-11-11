from urllib.request import *
from json import *
from datetime import *
from operator import *

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
   
# Add Earthquake class definition here   
   



# Required function - implement me!   
def read_quakes_from_file(filename):
   pass      

# Required function - implement me!
def filter_by_mag(quakes, low, high):
   pass       
     
# Required function - implement me!
def filter_by_place(quakes, word):   
   pass

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   pass
     


   