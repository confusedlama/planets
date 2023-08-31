import numpy as np
#import matplotlib.pyplot as plt


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


##Describes the Dynamic of Two Bodies, using a Numerical approach
class Dynamic:
    def coulomb(self,G,P1,P2):
        self.r = np.sqrt((P1.x) ** 2 + (P2.x) ** 2)
        Fr1 = G * P1.masse * P2.masse * 1/ (self.r**2)
        Fr2 = -Fr1
        return Fr1,Fr2
    def FxFy(self,P1,P2,Fr):
        dx = P2.x - P1.x
        dy = P2.y - P1.y
        alpha = np.arctan(dx/dy)

        self.Fx = Fr * np.cos(alpha)
        self.Fy = Fr * np.sin(alpha)
        return self.Fx, self.Fy

    def __init__(self,P1,P2,t,dT):
        self.duration = t
        self.dT = dT
        self.P1 = P1
        self.P2 = P2
        self.G = 2000
        self.Fx1 = 0
        self.Fy1 = 0
        self.Fx2 = 0
        self.Fy2 = 0
        self.Fr1 = 0

        self.planets = [self.P1, self.P2]

    def step(self):

            self.Fr1,self.Fr2 = self.coulomb(self.G,self.P1, self.P2)
            self.Fx1,self.Fy1 = self.FxFy(self.P1,self.P2,self.Fr1)
            self.Fx2,self.Fy2 = self.FxFy(self.P2,self.P1,self.Fr2)
            #print(self.P1.x, self.P1.y, self.Fx1, self.Fx2)
            self.P1.Ax = self.Fx1 / self.P1.masse
            self.P1.Ay = self.Fy1 / self.P1.masse
            self.P2.Ax = self.Fx2 / self.P2.masse
            self.P2.Ay = self.Fy2 / self.P2.masse
            self.P1.Vx = self.P1.Vx + self.P1.Ax * dT
            self.P1.Vy = self.P1.Vy + self.P1.Ay * dT
            self.P2.Vx = self.P2.Vx + self.P2.Ax * dT
            self.P2.Vy = self.P2.Vy + self.P2.Ay * dT
            self.P1.x = self.P1.x + self.P1.Vx * dT
            self.P1.y = self.P1.y + self.P1.Vy * dT
            self.P2.x = self.P2.x + self.P2.Vx * dT
            self.P2.y = self.P2.y + self.P2.Vy * dT




y = 100

planet1 = Planet(10,100,y,1, -1)
satelit = Planet(10,-100,-y,-1, 1)
duration = 100
dT = 0.5
Dynamic(planet1,satelit,duration, dT)







