class Planet():
    """Represents a planet"""
    
    def __init__(self, description:str, xPosition:float, yPosition:float, speed:float, mass:float):
        """basic constructor to initialize a new planet with its attributes"""
        self.description = description
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.speed = speed
        self.mass = mass

    #attributes of a planet
    description = ""
    xPosition = 0
    yPosition = 0
    speed = 0
    mass = 0

