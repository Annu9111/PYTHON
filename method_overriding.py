class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        return self.x*self.y
    
a1=shape(34,56)
print(a1.area())        
