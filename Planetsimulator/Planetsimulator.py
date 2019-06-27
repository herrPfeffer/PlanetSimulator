from PlanetManager import PlanetManager
from AnimatedScatter import AnimatedScatter

#create Manager instance
manager = PlanetManager(5)

#initialize variable number of planets
manager.create_planet(description='planet1', xPosition=0, yPosition=1, mass=100000, x_speed=0.01, y_speed=0.01)
manager.create_planet(description='planet2', xPosition=4, yPosition=2, mass=10, x_speed=0.01, y_speed=0.01)
manager.create_planet(description='planet3', xPosition=2, yPosition=3, mass=10, x_speed=0.01, y_speed=0.01)
manager.create_planet(description='planet4', xPosition=1, yPosition=4, mass=10, x_speed=0.01, y_speed=0.01)

#initialize stars
manager.create_star(description="star1", xPosition=5, yPosition=5, mass=1000)

#Show Planets in Plotter
scatter = AnimatedScatter(title="Planetsimulator", x_label="x-Axis", y_label="y-Axis", legend=2, manager=manager)