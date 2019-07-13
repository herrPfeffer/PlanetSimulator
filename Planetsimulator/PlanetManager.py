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
    timesteps = 10**10

    def create_planet(self, description: str, x_position:float, y_position:float, x_speed:float, y_speed:float, mass: float):
        """Creates a planet and appends it to the list planetary_objects."""
        if self.validate_position(x_position, y_position) == False:
            raise ValueError("There is already a planet in this position!")
        new_planet = Planet(description, x_position, y_position, x_speed, y_speed, mass)
        self.planetary_objects.append(new_planet)
        return new_planet

    def create_star(self, description:str, x_position:float, y_position:float, mass:float):
        """Creates a star and appends it to the list planetary_objects."""
        if self.validate_position(x_position, y_position) == False:
            raise ValueError("There is already a planetary object in this position.")
        new_star = Star(description, x_position, y_position, mass)
        self.planetary_objects.append(new_star)
        return new_star


    def validate_position(self, x_position:float, y_position:float):
        """Validates if the position of the planet can be used."""
        for planet in self.planetary_objects:
            if ((x_position == planet.x_position) and (y_position == planet.y_position)):
                return False
        return True

    def get_positions(self):
        """Returns a map with the x and y coordinates of all planets."""
        position_map = {}
        x_positions = []
        y_positions = []
        for planet in self.planetary_objects:
            planet.move_next(self.planetary_objects, self.timesteps)
            x_positions.append(planet.x_position)
            y_positions.append(planet.y_position)
        position_map["x_coordinate"] = x_positions
        position_map["y_coordinate"] = y_positions
        return position_map

    def determine_max_x_position(self):
        """determines the max x-Value"""
        return 2*7.377*10**12
        
    def determine_max_y_position(self):
        """determines the max y-Value"""
        return 2*7.377*10**12
        