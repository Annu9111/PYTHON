class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])    
        
    def show(self):
        print(f"employee name is {self.name} and age is {self.age}")
        
emp1=Employee("tommy",67)
emp1.show()
string="maya-45"
emp2=Employee.fromstr(string)   
emp2.show()         