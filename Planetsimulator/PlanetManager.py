from Planet import Planet
from Star import Star

class PlanetManager(object):
    """Creates and manages planets and their interference"""
    
    def __init__(self, timesteps:int=10**20):
        """Basic Constructor"""
        self.timesteps = timesteps

    #holds all planets in a list
    planetary_objects = []
    #timesteps = delta t
    timesteps = 10**20

    def create_planet(self, description: str, xPosition:float, yPosition:float, x_speed:float, y_speed:float, mass: float):
        """Creates a planet and appends it to the planet list"""
        if self.validate_position(xPosition, yPosition) == False:
            raise ValueError("There is already a planet in this position!")
        newPlanet = Planet(description, xPosition, yPosition, x_speed, y_speed, mass)
        self.planetary_objects.append(newPlanet)
        return newPlanet

    def create_star(self, description:str, xPosition:float, yPosition:float, mass:float):
        if self.validate_position(xPosition, yPosition) == False:
            raise ValueError("There is already a planetary object in this position.")
        new_star = Star(description, xPosition, yPosition, mass)
        self.planetary_objects.append(new_star)
        return new_star


    def validate_position(self, xPosition:float, yPosition:float):
        """validates if the position of the planet can be used"""
        for planet in self.planetary_objects:
            if ((xPosition == planet.x_position) and (yPosition == planet.y_position)):
                return False
        return True

    def get_positions(self):
        """returns a map with the x and y coordinates of the planets"""
        positionMap = {}
        xPositions = []
        yPositions = []
        for planet in self.planetary_objects:
            planet.move_next(self.planetary_objects, self.timesteps)
            xPositions.append(planet.x_position)
            yPositions.append(planet.y_position)
        positionMap["xCoordinate"] = xPositions
        positionMap["yCoordinate"] = yPositions
        return positionMap

    def determine_max_x_position(self):
        """determines the max x-Value"""
        #TODO
        return 2*7.377*10**12

    def determine_max_y_position(self):
        """determines the max y-Value"""
        #TODO
        return 2*7.377*10**12