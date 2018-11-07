##############################
########## CONSTANT ##########
##############################

import math
from vector import *   
from graphicslib import *
G = 6.673E-11

##############################

class Graphics:
    def __init__(self, xmin, xmax, ymin, ymax, bodies):
        '''
        Make a canvas that visualize
        motion of N bodies
        '''
        
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.height = 500
        self.width = self.height * (xmax-xmin)/(ymax-ymin)
        
        #make canvas and set parameter
        self.canvas = Canvas()
        self.canvas.setWidth(self.width)
        self.canvas.setHeight(self.height)
        self.canvas.setTitle("N Body Simulator")
        
        self.bodies = {}
        
        self.__setPosition(bodies)
    
    def __addBody(self, body):
        assert type(body) == Body
        shape = Circle(self.height/100)
        shape.setFillColor("black")
        shape.setBorderWidth(0)
        self.bodies[body] = shape
        self.canvas.add(shape)
    
    def __setPosition(self, bodies):
        for body in bodies:
            self.__addBody(body)
        self.__updatePosition()
    
    def __updatePosition(self):
        for body, shape in self.bodies.items():
            x, y = body.r.x, body.r.y
            xcoor = (x-self.xmin)*self.width/(self.xmax-self.xmin)
            ycoor = (self.ymax-y)*self.height/(self.ymax-self.ymin)
            shape.moveTo(xcoor, ycoor)
    
    def update(self): 
        self.__updatePosition()


##############################

class Body(object):
    def __init__(self, r, v, m):
        assert type(r) == type(v) == Vector
        self.r = r
        self.v = v
        self.m = m 
        
    def move(self, force, dt):
        assert type(force) == Vector
        a = 1/self.m * force #acceleration
        dr = 0.5*a*dt**2 + self.v*dt #r = 1/2at^2 + v0t
        dv = a * dt
        self.r += dr
        self.v += dv
        
    def force(self, b):
        assert type(b) == Body
        r = b.r - self.r
        return (G * self.m * b.m / r.norm()**3) * r

def simulate(R, V, M, dt=86400, numiter=5000, gconst=(-1e11, 1e11, -1e11, 1e11), GRAPHICS = False):
    assert len(R) == len(V) == len(M)
    assert type(R) == type(V) == type(M) == list
    N = len(R)
    bodies = [None]*N
    for i in range(N):
        rx, ry = R[i]
        vx, vy = V[i]
        m = M[i]
        bodies[i] = Body(Vector(rx, ry), Vector(vx, vy), m)
    if GRAPHICS:
        xmin, xmax, ymin, ymax = gconst
        graphics = Graphics(xmin, xmax, ymin, ymax, bodies)
    t = 0
    ret = []
    for num in range(numiter+1):
        t = dt*num
        data = []
        for body in bodies:
            rx, ry = body.r.x, body.r.y
            vx, vy = body.v.x, body.v.y
            m = body.m
            data.append([(rx, ry), (vx, vy)])
        f = [Vector(0, 0) for i in range(N)]
        for i in range(N):
            for j in range(i):
                f[i] += bodies[i].force(bodies[j])
                f[j] -= bodies[i].force(bodies[j])
        for i in range(N):
            bodies[i].move(f[i], dt)
        if GRAPHICS:
            graphics.update()
        ret.append(data)
    if GRAPHICS:
        graphics.canvas.close()
    return ret
