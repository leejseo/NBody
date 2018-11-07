
from graphicslib import *
from vector import *
from nbody_simulate import *

GRAPHICS = True

R = [(-5e10, 0), (5e10, 0)]
V = [(0, 2.5e3), (0, -2.5e3)]
M = [3e28, 3e28]
data = simulate(R, V, M, GRAPHICS=True)
f = open("./write.txt", 'w')
for row in data:
    f.write(repr(row)+'\n')
f.close()
