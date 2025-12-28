# while loop: as the name suggests,while loop executes statements while the condition is True as soon as the condition become False the interpreter comes out of the while loop.
i=1
while i<=10:
    print(i)
    i+=1
print("it's all done")

i=10
while i>0:
    print(i)
    i-=1
print("reverse iteration is done")

#we can also use else statement with while loop as soon as while loop condition become False else statement starts executing

i=5
while i>3:
    print("hello")
    i-=1
else:
    print("world")
            
        
    