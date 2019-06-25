from Planet import Planet

class PlanetCreator(object):
    """Creates and manages Planets and their interference"""
    
    def __init__(self):
        """Basic Constructor"""
        return super().__init_subclass__()

    #holds all planets in a list
    planets = [] 

    #TODO: interferences with other planets should be handled here
    def CreatePlanet(self, description: str, xPosition:float, yPosition:float, speed: float, mass: float) -> Planet:
        """Creates a planet and append it to the planet list"""
        if self.ValidatePosition(xPosition, yPosition) == False:
            raise ValueError("There is already a planet in this position!")
        newPlanet = Planet(description, xPosition, yPosition, speed, mass)
        self.planets.append(newPlanet)
        return newPlanet

    def ValidatePosition(self, xPosition:float, yPosition:float):
        """validates if the position of the planet can be used"""
        for planet in self.planets:
            if ((xPosition == planet.xPosition) and (yPosition == planet.yPosition)):
                return False
        return True

    def getXPositions(self) -> list:
        returnList = []
        for planet in self.planets:
            returnList.append(planet.xPosition)
        return returnList

    def getYPositions(self) -> list:
        returnList = []
        for planet in self.planets:
            returnList.append(planet.yPosition)
        return returnList

    def getDescriptions(self) -> list:
        returnList = []
        for planet in self.planets:
            returnList.append(planet.description)
        return returnList