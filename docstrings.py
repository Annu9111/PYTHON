# python docstrings are the string literals that appears right after the defination function ,method, class or module.they are used to document the code
def cube(n):
    '''it takes the number n
    return cube of n'''
    return n**3
print(cube(4))
print(cube.__doc__)   #it print docstring

# PEP 8 is the official style guide for Python code, a set of recommendations aimed at improving the readability and consistency of Python code. Adhering to it makes code easier for other developers to read, understand, and maintain

