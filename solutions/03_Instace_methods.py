class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width 
    def area(self):
        print(f"Area: {self.height *self.width}")
rect=Rectangle(10,5)
rect.area()