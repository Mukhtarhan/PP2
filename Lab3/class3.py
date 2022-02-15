class Shape:
    
    def __init__(self,length,width):
        
         self.length=length
         self.width=width
    def area(self):  
         print(self.length*self.width)

class Rectangle(Shape):
    def __init__(self,length,width):
        Shape.__init__(self,length,width)

x=Rectangle(4,5)
x.area()
