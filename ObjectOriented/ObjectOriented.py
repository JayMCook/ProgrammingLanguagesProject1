import json
import math
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

json_file_path = os.path.join(current_dir, 'SolarSystem.json')

with open(json_file_path, 'r') as f:
    sun = json.load(f)

class sun_class:
   def __init__(self, name, diameter=None, circumference=None):
      self.name = name
      self.planets = []
      if circumference == None: self.circumference = math.pi * diameter
      else: self.circumference = circumference
      if diameter == None: self.diameter = circumference / math.pi
      else: self.diameter = diameter
      self.volume = ((self.diameter/2)**3)*math.pi*(4/3)
      self.planetsvolume = 0
   def printvalues(self):
      print("Sun Name:", self.name, "\nSun Diameter:", self.diameter,  "\nSun Circumference:", self.circumference)
   def printvolume(self):
      if self.volume >= self.planetsvolume:
         print("Sun Volume is greater than sum of Planet Volumes")
      else:
         print("Planet Volumes are greater than Sun Volume")
 
class planet_class(sun_class):
   def __init__(self, name, diameter=None, circumference=None, orbitalPeriod=None, distance=None):
      self.name = name
      self.moons = []
      if circumference == None: self.circumference = math.pi * diameter
      else: self.circumference = circumference
      if diameter == None: self.diameter = circumference / math.pi
      else: self.diameter = diameter
      if orbitalPeriod == None: 
         self.distance = distance
         self.orbitalPeriod = (distance**3)**(.5)
      else: self.orbitalPeriod = orbitalPeriod
      if distance == None:
         self.orbitalPeriod = orbitalPeriod
         self.distance = (orbitalPeriod**2)**(1./3.)
      else: self.distance = distance
   def printvalues(self):
      print("Planet Name:", self.name, "\n Planet Diameter:", self.diameter, "\n Planet Circumference:", self.circumference, "\n Planet Orbital Period:", self.orbitalPeriod, "\n Planet Distance from Sun:", self.distance)

class moon_class:
   def __init__(self, name, diameter=None, circumference=None):
      self.name = name
      if circumference == None: self.circumference = math.pi * diameter
      else: self.circumference = circumference
      if diameter == None: self.diameter = circumference / math.pi
      else: self.diameter = diameter
   def printvalues(self):
      print("Moon Name:", self.name, "\n Moon Diameter:", self.diameter,  "\n Moon Circumference:", self.circumference)

if "Diameter" in sun:
  sun_object = sun_class(sun["Name"], diameter=sun["Diameter"])
elif "Circumference" in sun:
  sun_object = sun_class(sun["Name"], circumference=sun["Circumference"])
else:
  print("missing data")



for planet in sun["Planets"]:
   if "Diameter" in planet:
      if "OrbitalPeriod" in planet:
         planet_object = planet_class(planet["Name"], diameter=planet["Diameter"], orbitalPeriod=planet["OrbitalPeriod"])
      elif "DistanceFromSun" in planet:
         planet_object = planet_class(planet["Name"], diameter=planet["Diameter"], distance=planet["DistanceFromSun"])
      else: 
         print("missing data")
   elif "Circumference" in planet:
      if "OrbitalPeriod" in planet:
         planet_object = planet_class(planet["Name"], circumference=planet["Circumference"], orbitalPeriod=planet["OrbitalPeriod"])
      elif "DistanceFromSun" in planet:
         planet_object = planet_class(planet["Name"], circumference=planet["Circumference"], distance=planet["DistanceFromSun"])
      else:
         print("missing data")
   else:
      print("missing data")
   
   if 'Moons' in planet:
    for moon in planet["Moons"]:
        if "Diameter" in moon:
          moon_object = moon_class(moon["Name"], diameter=moon["Diameter"])
        elif "Circumference" in moon:
          moon_object = moon_class(moon["Name"], circumference=moon["Circumference"])
        else:
          print("missing data")
        planet_object.moons.append(moon_object)

   sun_object.planetsvolume += (((planet_object.diameter)/2)**3)*math.pi*(4/3)
   
   sun_object.planets.append(planet_object)

sun_object.printvalues()
   
for planet in sun_object.planets:
   planet.printvalues()
   if planet.moons:
      for moon in planet.moons:
         moon.printvalues()

sun_object.printvolume()



      

