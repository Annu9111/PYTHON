#global and local variable

#local variable is a variable which is accessible within the function only
#global variable is a variable which is define outside the function and accessible in whole code
 

x=4    #global variable

def num():
    x=2        #local variable
    print("local x is",x)

num()
print("global x is",x)   
# ----------------------------------------------------------------------------
#global keyword = it change the global variable within the function
y=89
def fam():
    global y
    y=4
    print("global variable",y)
    
fam()
print(y)     

