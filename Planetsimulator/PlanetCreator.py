from Planet import Planet
class PlanetCreator(object):
    """Creates and manages Planets and their interference"""
    
    #basic constructor to initialize the PlanetCreator
    def __init__(self):
        return super().__init_subclass__()

    #holds all planets in a list
    planets = [] 

    #Creates a planet and append it to the planet list
    #TODO: interferences with other planets should be handled here
    def CreatePlanet(self, description: str, xPosition:float, yPosition:float, speed: float, mass: float) -> Planet:
        if self.ValidatePosition(xPosition, yPosition) == False:
            raise ValueError("There is already a planet in this position!")
        newPlanet = Planet(description, xPosition, yPosition, speed, mass)
        self.planets.append(newPlanet)
        return newPlanet

    #validates if the position of the planet can be used
    def ValidatePosition(self, xPosition:float, yPosition:float):
        for planet in self.planets:
            if ((xPosition == planet.xPosition) and (yPosition == planet.yPosition)):
                return False
        return True