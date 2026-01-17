class person:           #class is a blueprint or a template for creating objects
    name="Anjali"
    occupation="software developer"
    networth=10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()               #object
print(a.name)   
a.info()

b=person()
b.name="nikita"
b.occupation="HR"
b.info()