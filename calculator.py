# calculator 
print("""welcome to python calculator
+ for add
- for sub
* for mul
/ for divide
** for power
// for floor division""")
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=input("Enter operator: ")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    if b!=0:
        print(a/b)
    else:
        print("wrong divisor")    
elif c=="//":
    if b!=0:
        print(a//b)
    else:
        print("wrong divisor")    
elif c=="**":
    print(a**b)   
else:
    print("invalid operator")                     