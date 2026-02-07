# walrus operator is a new addition in python 3.8 and allows you to assign a value to a variable within in expression it is represeted by :=

a=True
print(a:=False)      #ans=False

num=[1,2,3,4,5]
while(n:=len(num))>0:
    print(num.pop())
    
    
foods=list()
while(food := input("Enter food: ")) !="quit":
    foods.append(food)
        