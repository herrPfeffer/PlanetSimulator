from PlanetManager import PlanetManager
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    scats = []
    def __init__(self, title:str, xLabel:str, yLabel:str, legend:int, creator:PlanetManager):
        """Basic Constructor"""
        self.legend = legend
        self.creator = creator
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=100, init_func=self.setupValues)
        self.initPlotter(title, xLabel, yLabel)
        return super().__init_subclass__()

    def initPlotter(self, title:str, xLabel:str, yLabel:str):
        """Intit the basic plotter and show it"""
        plt.title(title)
        self.fig.canvas.set_window_title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()

    def setupValues(self):
        """Setup the scatter"""
        self.ax.set_xlim(xmax=self.creator.determineMaxXPosition())
        self.ax.set_ylim(ymax=self.creator.determineMaxYPosition())
        for planet in self.creator.planets:
            self.scats.append(self.ax.scatter(x=[], y=[], label=planet.description, alpha=0.5))
        self.ax.legend(loc=self.legend)
        return self.scats,

    def update(self, *args):
        """Update scatter values with the creator xPositions, yPositions methods"""
        counter = 0
        xPositions = self.creator.getXPositions()
        yPositions = self.creator.getYPositions()
        for scat in self.scats:
            scat.set_offsets(list(zip([xPositions[counter]], [yPositions[counter]])))
            counter += 1
        return self.scats,