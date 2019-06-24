from Planet import Planet
class PlanetCreator(object):
    """Creates and manages Planets and their interference"""
    
    #basic constructor to initialize the PlanetCreator
    def __init__(self):
        return super().__init_subclass__()

    #holds all planets in a list
    planets = [] 

    #Creates a planet and appends it to the planet list
    def CreatePlanet(self, description: str, xPosition:int, yPosition:int, speed: float, mass: float) -> Planet:
        newPlanet = Planet(description, xPosition, yPosition, speed, mass)
        self.planets.append(newPlanet)
        return newPlanet