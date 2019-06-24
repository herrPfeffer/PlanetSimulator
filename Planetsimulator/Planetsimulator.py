from PlanetCreator import PlanetCreator
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np

#create Creator instance
creator = PlanetCreator()

#initialize variable number of planets
creator.CreatePlanet(description='planet1', xPosition=0, yPosition=0, mass=150, speed=1)
creator.CreatePlanet(description='planet2', xPosition=1, yPosition=3, mass=100, speed=1)
creator.CreatePlanet(description='planet3', xPosition=4, yPosition=5, mass=300, speed=1)

#Show Planets in plotter
for planet in creator.planets:
    plt.scatter(planet.xPosition, planet.yPosition, planet.mass, alpha=0.5, 
                label=planet.description)
plt.title('Planetsimulator')
plt.xlabel('x-Axis')
plt.ylabel('y-Axis')
plt.legend(loc=2)
plt.show()