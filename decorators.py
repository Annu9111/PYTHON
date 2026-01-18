# A decorator is a function that take another function a an argument and return a new function that modifies the behaviour of the original function.

def greet(fx):
    def mfx():
        print("good morning!!")
        fx()
        print("thank you ")
    return mfx

@greet
def hello():
    print( "hello everyone")
 
hello()


#function with some arguments
def dec(fx):
    def mfx(*args,**kwargs):
        print("welcome to this function")
        fx(*args,**kwargs)
        print("thankyou for using")
    return mfx

@dec
def sum(a,b,c):
    print(a+b+c)

sum(1,2,3)

        
         