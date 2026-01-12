# lambda fun: a lambda fun is a small anonymous fun without name.it is define using the lambda keyword.  
# lambda argument : expression 

square=lambda x:x**2
print(square(4))

cube=lambda x:x**3
print(cube(4))

avg=lambda x,y,z:(x+y+z)/3
print(avg(3,5,5))

# To pass fun into fun eg. 

def function(fx,val):
    return 6 + fx(val)

print(function(lambda x:x**3,2))





