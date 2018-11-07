##############################
########## GRAPHICS ##########
##############################

#For debugging, one may need graphics
from nbody_simulate import Body
from graphicslib import *
from vector import *

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
