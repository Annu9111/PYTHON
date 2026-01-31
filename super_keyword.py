# the super() keyword in python is used to refer to the parent class .It is espacially usefull when a class inherits from a multiple parent classes and you want to call the method from one of the parent classes.
class Parent:
    def parent_method(self):
        print(f"this is a parent class")
        
class child(Parent):
    def child_method(self):
        print(f"this is a child method")
    
    def parent_method(self):
        return super().parent_method()      
    
c1=child()
c1.parent_method()   

# ---------------------------------------------------------------------
class Employee:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        
    def show(self):
        print(f"{self.name} is {self.age} years old .His/Her id number is {self.id} ")  
        
class Person(Employee):
    def __init__(self,name,age,job,id):
        super().__init__(name,age,id)
        self.job=job
        
    def details(self):
        print(f"{self.name} is {self.age} years old.His/Her profession is {self.job} and His/Her Id is {self.id}")
        
e1=Employee("Radha",34,1010)
e1.show()

p1=Person("beast",23,"youtuber",78)
p1.details()

            
    
        
                      
         
                  