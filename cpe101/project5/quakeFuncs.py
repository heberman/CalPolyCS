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
class Earthquake:
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return self.place == other.place and self.mag == other.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == other.time

def read_quakes_from_file(filename):
    quakes = []
    file = open(filename, "r")
    for line in file:
        vals = line.split()
        mag = float(vals[0])
        long = float(vals[1])
        lat = float(vals[2])
        time = int(vals[3])
        place = ' '.join(vals[4:])
        quakes.append(Earthquake(place, mag, long, lat, time))
    return quakes

def display_quakes(quakes):
    print("\nEarthquakes:")
    print("------------")
    for quake in quakes:
        print("(%.2f)" % quake.mag + "{:>40}".format(quake.place) + " at " + time_to_str(quake.time) + " (%8.3f, %6.3f) " % (quake.longitude, quake.latitude))
    print()

def display_options():
    print("Options:")
    print(" (s)ort")
    print(" (f)ilter")
    print(" (n)ew quakes")
    print(" (q)uit")

# Required function - implement me!
def filter_by_mag(quakes, low, high):
   return [quake for quake in quakes if quake.mag >= low and quake.mag <= high]
     
# Required function - implement me!
def filter_by_place(quakes, word):   
   return [quake for quake in quakes if quake.place.lower().find(word.lower()) != -1]

# Required function for final part - implement me too!   
def quake_from_feature(feature):
    mag = feature["properties"]["mag"]
    place = feature["properties"]["place"]
    time = feature["properties"]["time"] // 1000
    long = feature["geometry"]["coordinates"][0]
    lat = feature["geometry"]["coordinates"][1]
    return Earthquake(place, mag, long, lat, time)

def write_data(quakes):
    file = open("quakes.txt", "w")
    for quake in quakes:
        file.write(str(round(quake.mag, 2)) + " " + str(quake.longitude) + " " + str(quake.latitude) + " " + str(
            quake.time) + " " + quake.place + "\n")
     


   