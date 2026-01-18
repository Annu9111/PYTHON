# A constructor is a special method in a class used to create and initialize an object of a class .Contructor invoke automatically when an object of a class is created.
class Person:
    def __init__(self,name,occ):      #constructor
        self.name=name
        self.occ=occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}") 
        
a=Person("Tom","developer")        #object
a.info()

b=Person("John","Teacher")
b.info()
           
