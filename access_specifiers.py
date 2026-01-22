# Access Specifiers==>these are used to limit the access of class variables and class methods outside of class.

# 1.Public Access Specifiers = all the variables and method in python are public by default,any instance variable in a class followed by the self keyword are public accessed
class Employee:
    def __init__(self,name):
        self.name=name

a=Employee("python")
print(a.name)     
#_________________________________________________________________________________________
# 2.Private Access Specifiers = private members of a class are those members which are only accessible inside the class.A variable or method should be considered private by prefixing its name with a double underscore(__).
class private:
    def __init__(self,name):
        self.__name=name

obj=private("python")
# print(obj.__name)  #not eccessible directly
print(obj._private__name)       #can be accessible indirectly

print(obj.__dir__())  #print all the methods present in class.
# ____________________________________________________________________________________________
# 3.Protected Access Specifiers = a member of a class that is intended to be accessed only by the class itself and its subclasses
class protect :
    def __init__(self,name):
        self._name=name

a=protect("python")
print(a._name)  


   