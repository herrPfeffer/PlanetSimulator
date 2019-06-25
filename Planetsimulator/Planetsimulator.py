from PlanetCreator import PlanetCreator
from AnimatedScatter import AnimatedScatter

#create Creator instance
creator = PlanetCreator()

#initialize variable number of planets
creator.CreatePlanet(description='planet1', xPosition=0, yPosition=0, mass=150, speed=1)
creator.CreatePlanet(description='planet2', xPosition=1, yPosition=1, mass=300, speed=1)

#Show Planets in plotter
scatter = AnimatedScatter("Planetsimulator", "x-Axis", "y-Axis", 2, creator)