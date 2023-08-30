import numpy as np
class Planet:
    def __init__(self, masse = 1, size = 1, x = 100, y = 0):
        self.masse = masse
        self.size = size
        self.x = x
        self.y = y
print (Planet().x)