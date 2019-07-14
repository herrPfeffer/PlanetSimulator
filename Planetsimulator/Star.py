from Planet import Planet

class Star(Planet):
    """Represents a star"""
    
    def __init__(self, description:str, x_position:float, y_position:float, mass:float):
        """basic constructor to initialise a new planet with its attributes"""
        self.description = description
        self.x_position = x_position
        self.y_position = y_position
        self.mass = mass

    def move_next(self, planets:list, timesteps:int):
        return