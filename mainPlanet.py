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
    def gravitation(self, G, P1 , P2):
        dx = self.P1.x - self.P2.x
        dy = self.P1.y - self.P2.y
        self.r = np.sqrt((dx) ** 2 + (dy) ** 2)
        fr = -self.G * self.P1.masse * self.P2.masse /(self.r**2)
        alpha = np.arctan(dx / dy)
        if dx < 0:
            if dy > 0:
                alpha += np.pi
            else:
                alpha -= np.pi

        self.Fx1 = fr * np.cos(alpha)
        self.Fy1 = fr * np.sin(alpha)
        return self.Fx1,self.Fy1

    def __init__(self,P1,P2,t,dT):
        self.duration = t
        self.dT = dT
        self.P1 = P1
        self.P2 = P2
        self.G = 10
        self.Fx1 = 0
        self.Fy1 = 0
        self.Fx2 = 0
        self.Fy2 = 0
        self.Fr1 = 0
        self.step()
        self.planets = [self.P1, self.P2]

    def step(self):

            self.Fx1,self.Fy1 = self.gravitation(self.G,self.P1, self.P2)

            self.Fx2 = -self.Fx1
            self.Fy2 = -self.Fy1
            #print(self.r, self.P2.Ay)
            self.P1.Ax = self.Fx1 / self.P1.masse
            self.P1.Ay = self.Fy1 / self.P1.masse
            self.P2.Ax = self.Fx2 / self.P2.masse
            self.P2.Ay = self.Fy2 / self.P2.masse

            self.P1.Vx += self.P1.Ax * dT
            self.P1.Vy += self.P1.Ay * dT
            self.P2.Vx += self.P2.Ax * dT
            self.P2.Vy += self.P2.Ay * dT

            self.P1.x += self.P1.Vx * dT
            self.P1.y += self.P1.Vy * dT
            self.P2.x += self.P2.Vx * dT
            self.P2.y += self.P2.Vy * dT




y = 100

planet1 = Planet(10000,10,y,1, 0)
satelit = Planet(10,100,y+10,-1, 0)
duration = 100
dT = 0.05
Dynamic(planet1,satelit,duration, dT)





t = 2
a = 2
v = a * t
s = v * t
