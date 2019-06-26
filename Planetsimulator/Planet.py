import math
class Planet():
    """Represents a planet"""
    
    def __init__(self, description:str, x_position:float, y_position:float, x_speed:float, y_speed:float, mass:float):
        """basic constructor to initialize a new planet with its attributes"""
        self.description = description
        self.x_position = x_position
        self.y_position = y_position
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.mass = mass

    gravity_constant = 6.67430 * 10 ** (-11)

    def move_next(self, planets:list, timesteps:int):
        """move to the next timestep"""
        self.calculate_speed(planets, timesteps)
        self.calculate_position(timesteps)

    def calculate_speed(self, planets:list, timesteps:int):
        """the calculation of the speed for the new timestep"""
        for planet in planets:
            if planet != self:
                self.x_speed += timesteps * (self.gravity_constant * planet.mass / (math.fabs(planet.x_position - self.x_position)) ** 3 * (planet.x_position - self.x_position))
                self.y_speed += timesteps * (self.gravity_constant * planet.mass / (math.fabs(planet.y_position - self.y_position)) ** 3 * (planet.y_position - self.y_position))                

    def calculate_position(self, timesteps:int):
        """calculates the current position with the current speed"""
        self.x_position += timesteps * self.x_speed
        self.y_position += timesteps * self.y_speed