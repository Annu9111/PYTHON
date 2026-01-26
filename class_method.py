# class method = to define a class method "@classmethod" decorator is used, the first argument of the method should alwalys be "cls" which represent the class itself

class Person:
    company="abc"
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(f"the name of employee is {self.name} working in {self.company}")
        
    @classmethod
    def company_change(cls,new_company):
        cls.company=new_company
        
e1=Person("rahul")
e1.show() 
e2=Person("siya")
e2.company_change("google")
e2.show()               