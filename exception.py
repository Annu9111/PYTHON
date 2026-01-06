# exception handling is a processof respondingto un wanted or unexcepted event when a computer program runsexception handling deal with these events to avoid the program or system crashing
nums=input("enter number you want: ")
try:
    for i in range(1,11):
        print(int(nums),"x",i,"=",int(nums)*i)
except Exception as e:
    print("sorry, you typed wrong datatype!!")

print("Here your table is done")            


try:
    a=int(input("enter any number for index"))
    b=[1,2,3,4,5,6,7]
    print(b[a])
except ValueError:
    print("number entered is not an integer")
except IndexError:
    print("index is invalid")        
