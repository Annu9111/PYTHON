# break:the break statement enable a program to skip over a part of the code.it teminate the very loop it lies within. 

i=1
while i<15:
    print("5 X",i,"=",5*i)
    if i==10:
        break
    i+=1
print("its comes out from the loop")

#continue:it skip the rest of the loop statement and causes the next iteration to occur
for i in range(5):
    if i==2:
        continue
    print(i,"continue skip the iteration")


    
