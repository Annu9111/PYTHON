#hybrid inheritance
class baseclass:
    pass

class derived1(baseclass):
    pass

class derived2(baseclass):
    pass

class derived3(derived1,derived2):
    pass

#hierarical inheritance
class base:
    pass

class b1(base):
    pass

class b2(base):
    pass

class b3(b1):
    pass

class b4(b2):
    pass
