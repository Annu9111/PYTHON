class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        return f"name is {self.name}"    

class Developer:
    def __init__(self,language):
        self.language=language
        
    def show(self):
        return f"language is {self.language}"    

class Person(Employee,Developer):
    def __init__(self, name,language):
        self.name=name
        self.language=language
        
p=Person("lily","python")
print(p.show())
print(Person.mro())    #method resolution order        