

class Rectangle:

    def __init__(self, width,height):
        self._width = width
        self._height = height
@propoerty  
def width(self):
    pass


@property
def height(self):
    pass

rectangle = Rectangle(3,4)

print(rectangle.height)
print(rectangle.width)        