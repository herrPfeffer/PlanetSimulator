from PlanetManager import PlanetManager
from AnimatedScatter import AnimatedScatter

#creation of a Manager instance
manager = PlanetManager(5)

#initialising a variable number of planets
#distance in m, masses in kg, speed in m/s
manager.create_planet(description='mercury', xPosition=7.376*10**12, yPosition=7.376*10**12-5.791*10**10, mass=3.285*10**23, x_speed=33490, y_speed=33490)
manager.create_planet(description='venus', xPosition=7.376*10**12, yPosition=7.376*10**12-1.082*10**11, mass=4.867*10**24, x_speed=24763, y_speed=24763)
manager.create_planet(description='earth', xPosition=7.376*10**12, yPosition=7.376*10**12-1.096*10**11, mass=5.972*10**24, x_speed=21058, y_speed=21058)
manager.create_planet(description='mars', xPosition=7.376*10**12, yPosition=7.376*10**12-2.279*10**11, mass=6.390*10**23, x_speed=17062, y_speed=17062)
manager.create_planet(description='jupiter', xPosition=7.376*10**12, yPosition=7.376*10**12-7.786*10**11, mass=1.898*10**27, x_speed=9242, y_speed=9242)
manager.create_planet(description='saturn', xPosition=7.376*10**12, yPosition=7.376*10**12-1.434*10**12, mass=5.683*10**26, x_speed=6852, y_speed=6852)
manager.create_planet(description='uranus', xPosition=7.376*10**12, yPosition=7.376*10**12-2.875*10**12, mass=8.681*10**25, x_speed=4815, y_speed=4815)
manager.create_planet(description='neptun', xPosition=7.376*10**12, yPosition=7.376*10**12-4.50*10**12, mass=1.024*10**26, x_speed=3840, y_speed=3840)
manager.create_planet(description='pluto', xPosition=7.376*10**12, yPosition=7.376*10**12-5.906*10**12, mass=1.303*10**22, x_speed=3302, y_speed=3302)

#initialising stars
manager.create_star(description="sun", xPosition=7.376*10**12, yPosition=7.376*10**12, mass=1.989*10**30)

#showing Planets in Plotter
scatter = AnimatedScatter(title="Planetsimulator", x_label="x-Axis", y_label="y-Axis", legend=2, manager=manager)