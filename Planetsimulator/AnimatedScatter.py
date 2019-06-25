from PlanetCreator import PlanetCreator
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, title:str, xLabel:str, yLabel:str, legend:int, creator:PlanetCreator):
        """Basic Constructor"""
        self.creator = creator
        self.fig, self.ax = plt.subplots()      
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=100, init_func=self.setupValues)
        self.initPlotter(title, xLabel, yLabel, legend)
        return super().__init_subclass__()

    def initPlotter(self, title:str, xLabel:str, yLabel:str, legend:int):
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc=legend)
        plt.show()

    def setupValues(self):
        """Setup the values"""
        self.ax.scatter(self.creator.getXPositions(), self.creator.getYPositions(), label=self.creator.getDescriptions())

    def update(self, *args):
        """Update the scatter plot."""