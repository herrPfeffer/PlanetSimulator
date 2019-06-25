from PlanetCreator import PlanetCreator
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, title:str, xLabel:str, yLabel:str, legend:int, creator:PlanetCreator):
        """Basic Constructor"""
        self.legend = legend
        self.creator = creator
        self.fig, self.ax = plt.subplots()      
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=100, init_func=self.setupValues, interval=1000)
        self.initPlotter(title, xLabel, yLabel)
        return super().__init_subclass__()

    def initPlotter(self, title:str, xLabel:str, yLabel:str):
        """Intit the basic plotter and show it"""
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()

    def setupValues(self):
        """Setup the values"""
        for planet in self.creator.planets:
            self.scat = self.ax.scatter(x=planet.xPosition, y=planet.yPosition, label=planet.description, alpha=0.5)
        self.ax.legend(loc=self.legend)
        return self.scat,

    def update(self, *args):
        """Update the scatter plot."""
        self.scat.set_offsets(list(zip(self.creator.getXPositions(), self.creator.getYPositions())))
        self.ax.legend(loc=self.legend)
        return self.scat,