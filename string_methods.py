a="!!! Annu !!!!! Annu !!!!"
print(a.upper())        #convert all char into upper letters
print(a.lower())        #into lower char
print(a.rstrip("!"))   #remove all occurance of ! on right side
print(a.replace("Annu","anjali"))  #replace all Annu to anjali
print(a.split(" "))    #convert into list
blog="introduction to python"
print(blog.capitalize())     #it will capitalize first letter of tje given string
print(blog.center(50))      #centre method aligns the string to the centre
print(a.count("Annu"))      #it count the accourance of chars in the string
print(a.endswith("!"))      #return True if it endswith !
print(a.startswith("!"))          #return True if it startswith !
b="hello my name is ...!!"
print(b.find("is"))           #it returns the index of first occorance of words ,if word is not present it will return -1
print(b.index("is"))        #it also return the index of char ,but if char is not there than raisean error
d="hello 23434"  
print(d.isalnum())     #return True only if the entire string consists of A-Z,a-z,0-9
print(a.isalpha())   #return True only if the entire string consists of A-Z,a-z
print(a.isalnum())     #return True only it the entire string consists of 1-9
print(blog.islower())  #return True if all char are of lower case letters a-z
print(blog.isupper())  #return True if all char are of upper case letters A-Z
e="hello \n world"
print(e.isprintable())   #return True if it does not contain any non printable char ,but here it is False because of \n
print(a.isspace())    #return True if string contain white spaces in it
print(blog.istitle())  #return True if the first word of each word is capital
print(a.swapcase())  #it swap the char case upper to lower vice versa
print(d.title())  #convert capital to each letter of the word
# etc
