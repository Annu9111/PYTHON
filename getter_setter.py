# A getter in python is a method used to retrieve the value of a class attribute.getters are the key part of incapsulation, typically defined under @property decorators 

class myclass:
    def __init__(self,value):
        self.__value=value
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,new_val):
        self.__value=new_val
    
    def show(self):
        print(f"the value is {self.__value}")
        
a=myclass(23)
a.show()          

# getter do not take any parameter and we cannot set the value through getter method.for that we need setter, typically defined under @property_name.setter

a.value=45
a.show()    
    
    
    
        