import numpy as np



class Planet:
    def __init__(self, masse, x, y ,vx , vy , ax = 0, ay = 0, size = 1):
        self.masse = masse
        self.size = size
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy = vy
        self.Ax = ax
        self.Ay = ay
    def newValues(self,x,y,vx,vy,ax,ay):
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy= vy
        self.Ax = ax
        self.Ay = ay



y = 0
planet1 = Planet(10,100,y,100, 0)
satelit = Planet(10,-100,y,-100, 0)

##Describes the Dynamic of Two Bodies, using a Numerical approach
def dynamic(P1,P2,dT):
    print(2)


dynamic(planet1,satelit)


