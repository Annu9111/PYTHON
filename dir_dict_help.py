# dir() = the dir() function return the  list of all the attribute and methods (including dunder method) available for an object.
lst=[1,2,3,4,5]
print(dir(lst))


#__dict__ = the __dict__ attribute return a dictionary representation of an object's attribute. it is useful tool for introspection.

class person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name of employee is {self.name}")
p1=person("radha")
print(p1.__dict__)

#help() = the help function is used to get help documentation for an object ,including the discription of attribute and methods

print(help(person))                