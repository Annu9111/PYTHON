from functools import reduce
# the map,filter and reduce functions are builtin function, that allow you to apply a function to a sequences of element and return a new sequence .These function are known as higher order function as they take other function as argument. 

# map(function,iterable) 
def cube(x):
    return x**3

ls=[1,2,3,4,5,6,7,8,9,10]

new_list=list(map(cube,ls))
print(new_list)

new=list(map(lambda x:x*x,ls))
print(new)

a=list(map(str,ls))
print(a)
# ---------------------------------------------------------------------------

# filter(predicate,iterable) 
def fun(a):
    return a>4

new_l=list(filter(fun,ls))
print(new_l)

# ---------------------------------------------------------------------------

numbers=[1,2,3,4,5,6]
def my_sum(x,y):
    return x+y
sum=reduce(my_sum,numbers)
print(sum)   
 