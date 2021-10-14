class Point: # __new__ __init__ __str__ __eq__
    def __init__(self, valx, valy): # a method
        
        self.x=valx # definition and initialization of the attribute x
        self.y=valy # definition and initialization of the attribute x
    def __str__(self):
        return f"<{self.x},{self.y}>"
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def __add__(self, val):
        return Point(self.x+val, self.y+val)
    def clear(self):
        self.x=self.y=0
    def __eq__(self, other):
        return self.x==other.x and self.y ==other.y


class PointColor(Point):
    def __init__(self, valx, valy, col):
        super().__init__(valx, valy)
        self.color=col
    def clear(self):
        super().clear()
        self.color="black"
        
p=PointColor(4,5,"green")
print(p)