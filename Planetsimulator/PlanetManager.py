from Planet import Planet

class PlanetManager(object):
    """Creates and manages Planets and their interference"""
    
    def __init__(self, timesteps:int = 100):
        """Basic Constructor"""
        self.timesteps = timesteps

    #holds all planets in a list
    planets = []
    #timesteps = delta t
    timesteps = 100

    def CreatePlanet(self, description: str, xPosition:float, yPosition:float, x_speed:float, y_speed:float, mass: float):
        """Creates a planet and append it to the planet list"""
        if self.ValidatePosition(xPosition, yPosition) == False:
            raise ValueError("There is already a planet in this position!")
        newPlanet = Planet(description, xPosition, yPosition, x_speed, y_speed, mass)
        self.planets.append(newPlanet)
        return newPlanet

    def ValidatePosition(self, xPosition:float, yPosition:float):
        """validates if the position of the planet can be used"""
        for planet in self.planets:
            if ((xPosition == planet.xPosition) and (yPosition == planet.yPosition)):
                return False
        return True

    def getPositions(self):
        positionMap = {}
        xPositions = []
        yPositions = []
        for planet in self.planets:
            planet.move_next(self.planets, self.timesteps)
            xPositions.append(planet.xPosition)
            yPositions.append(planet.yPosition)
        positionMap["xCoordinate"] = xPositions
        positionMap["yCoordinate"] = yPositions
        return positionMap

    def determineMaxXPosition(self):
        """determines the max x-Value"""
        #TODO
        return 10

    def determineMaxYPosition(self):
        """determines the max y-Value"""
        #TODO
        return 10

    
