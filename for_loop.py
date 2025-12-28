# for loop can iterate over a sequence of iterable object[strings,list,tuple,sets,dictionary] in python.
name="Annu"
for i in name:
    print(i,end=",")
    
colors=["red","yellow","orange","purple","green"]
for i in colors:
    print(i)  
    for j in i:
        print(j)
        
# for loop : for specific number of time we can use:range 
for i in range(4):     #end=3
    print(i)          
    
for i in range(1,9):     #starts= 1 , ends= 8 
    print("hello world")
    
for i in range(1,8,2):    #starts= 1 , end= 7 ,step=2
    print(i)
    
for i in range(5,-1,-1):   #starts=5 ,end=0,step=-1 
    print(i)            
    
    
    

