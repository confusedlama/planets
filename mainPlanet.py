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

    def __init__(self,P1,P2,t,dT):

        self.duration = t
        self.dT = dT
        i = 0

        while i < duration:
            self.r = np.sqrt((P1.x) ** 2 + (P2.x) ** 2)
            self.P1 = P1
            self.P2 = P2
            self.Fx1
            self.Fy1
            self.Fx2
            self.Fy2

    def Force(self):
        return 0



            print(self.P1.x,self.P1.x,self.P2.x,self.P2.y)

            i += dT


        print (self.r)



y = 0

planet1 = Planet(10,100,y,100, 0)
satelit = Planet(10,-100,y,-100, 0)
duration = 100
dT = 0.1
Dynamic(planet1,satelit,duration, dT)







