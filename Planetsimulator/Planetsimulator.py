from PlanetManager import PlanetManager
from AnimatedScatter import AnimatedScatter

#create Creator instance
creator = PlanetManager()

#initialize variable number of planets
creator.CreatePlanet(description='planet1', xPosition=0, yPosition=1, mass=150, speed=1)
creator.CreatePlanet(description='planet2', xPosition=1, yPosition=2, mass=300, speed=1)
creator.CreatePlanet(description='planet3', xPosition=2, yPosition=3, mass=300, speed=1)
creator.CreatePlanet(description='planet4', xPosition=3, yPosition=4, mass=300, speed=1)

#Show Planets in plotter
scatter = AnimatedScatter("Planetsimulator", "x-Axis", "y-Axis", 2, creator)