# variable can be define at the class level or at the instance level
# class variable:class variable are define at the class level and are share among all the instance of the class . They are define outside of any method and are usually used to store information that is common to all the instances of the class.

#instance variable:define under init method and are define at the instance level
class Employee:
    company_name="ABC Tech"        #class variable
    def __init__(self,name):
        self.name=name     #instance variable
        self.salary=10000    #instance default variable
        
    def show(self):
        print(f"The name of employee is {self.name} and his/her salary is {self.salary} working in {self.company_name}")
        
emp1=Employee("Mr.Beast")
emp1.show()
emp1.company_name="abc tech"
emp1.salary=200000000
Employee.show(emp1)

emp2=Employee("tom brusely")
Employee.company_name="google"      #here class variable will change
emp2.show()




        
        
        