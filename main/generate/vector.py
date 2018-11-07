import math
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        assert type(other) == Vector
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        assert type(other) == Vector
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        assert type(other) == float or type(other) == int
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        assert type(other) == float or type(other) == int        
        return self*other
    
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
