a="my name is 'annu' "       #type str
print(a)
# In Python, a string is an immutable sequence of Unicode characters used to store and manipulate text data. They are a foundational data type and can be created using single ('...'), double ("..."), or triple quotes ("""...""" or '''...''')

#string slicing
a="my name is"
print(a[0:3])         #0 is included, 3 is excluded
print(a[:3])         #0 to 3   output=my
print(a[:])       #output=my name is
print(a[::2])      #output=m aei
print(a[-4:-1])    #e i
print(a[::-1])     #si rman ym