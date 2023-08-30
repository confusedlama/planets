import numpy as np



class Planet:
    def __init__(self, masse,dT , size = 1, x = 100, y = 0,vx = 10, vy = 0, ax = 0, ay = 0):
        self.masse = masse
        self.size = size
        self.x = x
        self.y = y
        self.dT = dT
        self.Vx = vx
        self.Vy = vy
        self.Ax = ax
        self.Ay = Ay


Sonne = Planet()