from abc import ABC, abstractmethod





class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
    
    

class Triangle(Shape):
    def __init__(self, base, ht):
        self.base = base
        self.ht = ht

    def area(self):
        return self.base *self.ht/2

shapes= [(Circle(4)), Square(5), Triangle(6,7)]

for shape in shapes:
    print(shape.area())