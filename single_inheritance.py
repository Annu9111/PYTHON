class Animal:
    def __init__(self,name):
        self.name=name
        
    def sound(self):
        return f" makes sound"
    
class rabbit(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name)
        self.breed=breed  
        
a=Animal("dog")
print(a.sound())
b=rabbit("rabbit","himaliyan") 
print(b.sound())              