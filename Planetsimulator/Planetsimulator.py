from PlanetCreator import PlanetCreator
from AnimatedScatter import AnimatedScatter
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np

#create Creator instance
creator = PlanetCreator()

#initialize variable number of planets
creator.CreatePlanet(description='planet1', xPosition=0, yPosition=0, mass=150, speed=1)
creator.CreatePlanet(description='planet2', xPosition=1, yPosition=1, mass=300, speed=1)

#Show Planets in plotter
scatter = AnimatedScatter("Planetsimulator", "x-Axis", "y-Axis", 2, creator.planets)

#for planet in creator.planets:
#    plt.scatter(x=planet.xPosition, y=planet.yPosition, alpha=0.5, label=planet.description)
#plt.title('Planetsimulator')
#plt.xlabel('x-Axis')
#plt.ylabel('y-Axis')
#plt.legend(loc=2)
#plt.show()