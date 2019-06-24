import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""

    def __init__(self, title:str, xLabel:str, yLabel:str, legend:int, planets:list):
        """Basic Constructor"""        
        self.fig, self.ax = plt.subplots()
        self.planets = planets
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5, init_func=self.setupValues, blit=True)
        self.initPlotter(title, xLabel, yLabel, legend)
        plt.show()
        return super().__init_subclass__()

    def initPlotter(self, title:str, xLabel:str, yLabel:str, legend:int):        
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc=legend)

    def setupValues(self):
        """Setup the values"""
        for planet in self.planets:
            self.scat = self.ax.scatter(x=planet.xPosition, y=planet.yPosition, alpha=0.5, label=planet.description)
        return self.scat

    def update(self):
        """Update the scatter plot."""
        self.scat.set_offsets(x=planet.xPosition, y=planet.yPosition)
        return self.scat