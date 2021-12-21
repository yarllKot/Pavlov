import math
import numpy as np
from matplotlib import pyplot as pp
#coding: utf8


MODEL_G = 9.81
MODEL_DT = 0.001
class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        

    def advance(self):
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT
class Rocket(Body):
    A=True
    def __init__(self, x, y, m1, m2, vm, dm):
        super().__init__(x, y, 10, 10)
        self.m1=m1 #rocket mass
        self.m2=m2 #rocket and oil mass
        self.vm=vm #oil velocity
        self.dm=dm #dm

    def advance(self): 
        if self.m1<self.m2:
            self.vx+=(self.dm*self.vm/self.m2)
            self.vy+=(self.dm*self.vm/self.m2)
            self.m2-=self.dm
        else:       #Rocket starts falling
            if(self.A):
                self.A=False
        super().advance()
        

b = Body(0, 0, 9, 9)
r = Rocket(0, 0, 10, 14, 11, 0.01)

bodies = [b, r]


for t in np.arange(0, 2, MODEL_DT): 
    for b in bodies:
        b.advance() 


for b in bodies:
    pp.plot(b.trajectory_x, b.trajectory_y) 
pp.show()