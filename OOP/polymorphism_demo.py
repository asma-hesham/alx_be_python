import math
class Shape:
    def area(self):
        raise NotImplementedError("Derived class must implement this method")
    
class Rectengle(Shape):
    def __init__(self, Length:float , width:float):
        self.Length = Length
        self.width = width
        

    def area(self): 
        return self.Length * self.width   

class Circle(Shape):    
    def __init__(self, redius):
        self.redius = redius
    
    def area(self):
        return math.pi * (self.redius**2)
    