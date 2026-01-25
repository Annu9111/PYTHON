#static method = these are the methods that belong to a class rather than an instance of the class.They are define under @staticmethod decorator and do not have access to the instance of the class.

class Maths:
    def __init__(self,num):
        self.num=num
        
    def addtonum(self,n):
        self.num=self.num+n
        
    @staticmethod
    def add(a,b):
        return a+b
    
    
res=Maths.add(2,5)
print(res)
            
