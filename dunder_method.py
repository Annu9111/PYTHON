class Person:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for i in self.name:
            i+=1
        return i
    
p=Person("lily")
print(p.name)
print(len(p.name))   
     