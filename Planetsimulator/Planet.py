import math
class Planet():
    """Represents a planet"""
    
    def __init__(self, description:str, xPosition:float, yPosition:float, x_speed:float, y_speed:float, mass:float):
        """basic constructor to initialize a new planet with its attributes"""
        self.description = description
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.mass = mass

    gravity_constant = 6.67430*10**(-11)

    def calculate_speed(self, planets:list, timesteps:int):
        for planet in planets:
            if planet==self:
                next()
            else:
                self.x_speed += timesteps*(
                    gravity_constant*planet.mass/(math.abs(planet.xPosition-self.xPosition))**3*(
                        planet.xPosition-self.xPosition))
                self.y_speed += timesteps*(
                    gravity_constant*planet.mass/(math.abs(planet.yPosition-self.yPosition))**3*(
                        planet.yPosition-self.yPosition))
