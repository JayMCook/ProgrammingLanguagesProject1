import json
import math
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

json_file_path = os.path.join(current_dir, 'SolarSystem.json')

with open(json_file_path, 'r') as f:
    data = json.load(f)

def DiametertoCircumference(diameter):
    return diameter * math.pi

def CircumferencetoDiameter(circumference):
    return circumference/math.pi

def OrbitalPeriodtoDistance(orbitalPeriod):
    return (orbitalPeriod**2)**(1./3.)

def DistancetoOrbitalPeriod(distance):
    return (distance**3)**(.5)

print("Sun Name: ", data['Name'])
if('Diameter' in data):
    print("Sun Diameter: ", data['Diameter'])
    sunVolume = (((data['Diameter'])/2)**3)*math.pi*(4/3)
elif('Circumference' in data):
    print("Sun Diameter: ", CircumferencetoDiameter(data['Circumference']))
    sunVolume = ((CircumferencetoDiameter(data['Circumference'])/2)**3)*math.pi*(4/3)

if('Circumference' in data):
    print("Sun Circumference: ", data['Circumference'])
elif('Diameter' in data):
    print("Sun Circumference: ", DiametertoCircumference(data['Diameter']))

volumeTotal = 0
planetCounter = 1
for planet in data['Planets']:
    print("Planet", planetCounter, "Name:", planet['Name'])
    if('Diameter' in planet):
        print("Planet", planetCounter, "Diameter:", planet['Diameter'])
        volumeTotal += ((planet['Diameter']/2)**3)*math.pi*(4/3)
    elif('Circumference' in planet):
        print("Planet", planetCounter, "Diameter:", CircumferencetoDiameter(planet['Circumference']))
        volumeTotal += (((CircumferencetoDiameter(planet['Circumference']))/2)**3)*math.pi*(4/3)

    if('Circumference' in planet):
        print("Planet", planetCounter, "Circumference:", planet['Circumference'])
    elif('Diameter' in planet):
        print("Planet", planetCounter, "Circumference:", DiametertoCircumference(planet['Diameter']))

    if('DistanceFromSun' in planet): 
        print("Planet", planetCounter, "Distance from Sun:", planet['DistanceFromSun'])
    elif('OrbitalPeriod' in planet):
        print("Planet", planetCounter, " DistanceFromSun:", OrbitalPeriodtoDistance(planet['OrbitalPeriod']))

    if('OrbitalPeriod' in planet):
        print("Planet", planetCounter, "Orbital Period:", planet['OrbitalPeriod'])
    elif('DistanceFromSun' in planet):
        print("Planet", planetCounter, "Orbital Period:", DistancetoOrbitalPeriod(planet['DistanceFromSun']))

    
    moonCounter = 1
    if 'Moons' in planet:
        for moon in planet['Moons']:
            print("Moon", moonCounter, "Name:", moon['Name'])
            if('Diameter' in moon):
                print("Moon", moonCounter, "Diameter:", moon['Diameter'])
            elif('Circumference' in moon):
                print("Moon", moonCounter, "Diameter:", CircumferencetoDiameter(moon['Circumference']))

            if('Circumference' in moon):
                print("Moon", moonCounter, "Circumference:", moon['Circumference'])
            elif('Diameter' in moon):
                print("Moon", moonCounter, "Circumference:", DiametertoCircumference(moon['Diameter']))

            moonCounter += 1


    planetCounter += 1

if (volumeTotal >= sunVolume):
    print("Sun volume is less than total volume of Planets")
else:
    print("Sun volume is greater than total volume of Planets")
