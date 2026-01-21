# Inheritance: when a class derived from another class.the child class will inherit all the public and protected properties and method from parent class,it can also have their own properties and method is called inheritance.

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print(f"{self.name} is {self.age} years old.")
        
        
class child(Parent):
    def lang(self):
        print("the default language is python")
            
        
obj=Parent("tom",34)
obj.show()   

a=child("jiya",45)
a.show()
a.lang()         