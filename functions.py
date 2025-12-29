# Function: a function is a part of code that perform a specific tasks whenever it is called.
# there are two types of function:
#1. builtin function(min,max,len,type,range,dict,list,tuple,set,print,etc)   2.user definefunction

def calculate_gmean(a,b):
    mean=(a*b)//(a+b)
    return mean

print(calculate_gmean(4,5))
print(calculate_gmean(8,2))
# ---------------------------------------
def is_greater(a,b):
    if a>b:
        print('greater number is',a)
    else:
        print('greater number is',b)

is_greater(3,6)
is_greater(8945,234)
# -------------------------------------------
# there are four types of arguments that we can provide a function 
# 1. default argument
def sum_of(a=1,b=3):
    print(a+b)

sum_of()
sum_of(3,6)
sum_of(4)
# ----------------
# 2.keyword argument
def name(fname,mname,lname):
    print("hello",fname,mname,lname)

name(mname="bruce",lname="lee",fname="tom")  #order does not matter 
# -----------------
# 3.Required argument
def is_sum(a,b=3):
    print(a+b)
is_sum(3)
is_sum(3,5)    
# -------------------
# 4.varible length argument
def average(*numbers):  #the function accessing the argument in the form of tuple
    sum=0                 #type of number is tuple
    for i in numbers:
        sum=sum+i
    print("average is" ,sum//len(numbers))  

average(1,2,3,4,5,6,7,8,9)

def name(**name): #the function accessing the argument in the form of dictionary
    print(type(name))  #dict
    print("Hello",name["name1"],name["name2"],name["name3"],name["name4"])

name(name1="riya,",name2="priya,",name3="jiya,",name4="miya")    
    

    

    
    
 
    
    
