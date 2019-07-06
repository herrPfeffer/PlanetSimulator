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

#    def calculate_speed(self, planets:list, timesteps:int):
#        """the calculation of the speed for the new timestep"""
#        x_sum=0
#        y_sum=0
#        for planet in planets:
#            if planet != self:
#                 if planet.y_position != self.y_position:
#                    y_sum+=((self.gravity_constant * planet.mass / 
#                                                 ((math.fabs(planet.y_position - self.y_position)) ** 3)) * (planet.y_position - self.y_position))

#                 if planet.x_position != self.x_position:
#                    x_sum+=((self.gravity_constant * planet.mass / 
#                                                 ((math.fabs(planet.x_position - self.x_position)) ** 3)) * (planet.x_position - self.x_position))
#                               
#            self.x_speed+=(1/timesteps)*x_sum
#            self.y_speed+=(1/timesteps)*y_sum


#something wrong with y_speed or y_position: they only move in x_direction
#maybe the values are too high or too low because they move very slowly
    def calculate_speed(self, planetary_objects:list, timesteps:int):
        x_sum=0
        y_sum=0
        for planet in planetary_objects:
            if planet != self:
                x_sum+=((self.gravity_constant*planet.mass)/(math.sqrt((planet.x_position-self.x_position)**2+(planet.y_position-self.y_position)**2)**3))*(planet.x_position-self.x_position)
                y_sum+=((self.gravity_constant*planet.mass)/(math.sqrt((planet.x_position-self.x_position)**2+(planet.y_position-self.y_position)**2)**3))*(planet.y_position-self.y_position)
        self.x_speed+=1/(timesteps)*x_sum           
        self.y_speed+=1/(timesteps)*y_sum

    def calculate_position(self, timesteps:int):
        """calculates the current position with the current speed"""
        self.x_position += 1/timesteps * self.x_speed
        self.y_position += 1/timesteps * self.y_speed