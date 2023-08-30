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


##Describes the Dynamic of Two Bodies, using a Numerical approach
class Dynamic:
    def coulomb(self,G,P1,P2):
        self.r = np.sqrt((P1.x) ** 2 + (P2.x) ** 2)
        Fr1 = G * P1.masse * P2.masse * 1/ (self.r**2)
        Fr2 = -Fr1
        return Fr1,Fr2
    def FxFy(self,P1,P2,Fr):
        dx = P1.x - P2.x
        print(dy = P1.y - P2.y)
        alpha = np.arctan(dx/dy)
        self.Fx = Fr * np.sin(alpha)
        self.Fy = Fr * np.cos(alpha)
        return self.Fx, self.Fy

    def __init__(self,P1,P2,t,dT):

        self.duration = t
        self.dT = dT
        self.P1 = P1
        self.P2 = P2
        self.G = 1
        i = 0
        self.Fx1 = 0
        self.Fy1 = 0
        self.Fx2 = 0
        self.Fy2 = 0
        self.Fr1 = 0
        while i < duration:


            self.Fr2 = -self.Fr1
            self.Fr1,self.Fr2 = self.coulomb(self.G,self.P1, self.P2)
            self.Fx1,self.Fy1 = self.FxFy(self.P1,self.P2,self.Fr1)
            self.Fx2,self.Fy2 = self.FxFy(self.P2,self.P1,self.Fr2)
            print(self.P1.x, self.P1.x, self.P2.x, self.P2.y,self.Fx1,self.Fx2)
            i += dT


y = 0

planet1 = Planet(10,100,y,100, 10)
satelit = Planet(10,-100,y,-100, -10)
duration = 100
dT = 0.1
Dynamic(planet1,satelit,duration, dT)







