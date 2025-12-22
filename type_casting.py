# typecasting
# ---------------------------
# the conversion of one datatype to another datatype is called type casting in python
# python supports wide variety of functions and methods like---
# int(),float(),bin(),hex(),oct(),list(),set(),dict(),tuple(),set(),str()
a="1"
b="4"
c=a+b     #output:14
print(type(c))
# there are two types of typecasting in python:- (1)implicit (2)explicit
# --------------------------------------------------------------------
# (1)explicit
#conversion of one datatype into another datatype done by developer or programmer's intervention or mannually to achieve various operation 
a="1"
b="2"
print(int(a)+int(b))     #datatype(int)
# ------------------------------------------------------------------------
#(2)implicit
# Implicit type casting (also known as type coercion) in Python is the automatic conversion of one data type to another by the Python interpreter during an operation, typically to prevent data loss. The core principle of implicit conversion is "type promotion," where Python converts a lower precision or "smaller" data type to a higher precision or "larger" data type. This ensures that operations involving mixed types produce the most accurate result possible. 
a=23
b=34.67
print(a+b)            #datatype(float)
 

