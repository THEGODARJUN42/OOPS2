class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(10, 12)
print("Diminesion of rectangles - Lenght : %d widht : %d" % (newRectangle.length, newRectangle.width)) 
print("Area of Rectangle :", newRectangle.rectangle_area())  
      
     
     
