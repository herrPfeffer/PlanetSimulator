from PlanetManager import PlanetManager
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    scats = []
    def __init__(self, title:str, xLabel:str, yLabel:str, legend:int, manager:PlanetManager):
        """Basic Constructor"""
        self.legend = legend
        self.manager = manager
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.update, 
                                           frames=self.manager.timesteps, 
                                           init_func=self.setupValues)
        self.initPlotter(title, xLabel, yLabel)

    def initPlotter(self, title:str, xLabel:str, yLabel:str):
        """Intit the basic plotter and show it"""
        plt.title(title)
        self.fig.canvas.set_window_title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()

    def setupValues(self):
        """Setup the Scatter"""
        self.ax.set_xlim(xmax=self.manager.determineMaxXPosition())
        self.ax.set_ylim(ymax=self.manager.determineMaxYPosition())
        self.scats.clear()
        for planet in self.manager.planets:
            self.scats.append(self.ax.scatter(x=[], y=[], label=planet.description, alpha=0.5))
        self.ax.legend(loc=self.legend)
        return self.scats,

    def update(self, *args):
        """Update scatter values with the creator xPositions, yPositions methods"""
        counter = 0
        xPositions = self.manager.getXPositions()
        yPositions = self.manager.getYPositions()
        for scat in self.scats:
            scat.set_offsets(list(zip([xPositions[counter]], [yPositions[counter]])))
            counter += 1
        return self.scats,