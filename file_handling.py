#READING A FILE
f=open("my_file.txt","r")    #file name ,mode name(r=read is default)
text=f.read()       
print(text)
f.close()

#WRITING TO  A FILE
f=open("my_file.txt","w")    #w=write mode
text=f.write("hello everyone welcome back to my channel!!!")
f.close()

#APPINDING TO A FILE
f=open("my_file.txt","a")    #a=add to the existing file
text=f.write("\nhello everyone!!!")
f.close()  

#No need to close-->shortcut to open a file
with open("my_file.txt","a") as f:
    f.write("\nhey i am inside") 

# --------------------------------------------------------------

f=open("my_file.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)
    
    
f=open("file.txt","w")
lines=["line1 \n","line2 \n","line3 \n"]
f.writelines(lines)
f.close()

# ---------------------------------------------------------------------
# seek function:allow you to move the current position position within a file, position is specified in bytes 
with open("my_file.txt","r") as f:
    #move to the 10th byte in the file
    f.seek(10)
    data=f.read()
    print(data)
    
# tell function :it tells the current position of pointer within the file
with open("my_file.txt","r") as f:
    f.seek(10)
    print(f.tell())  #tells current position
    data=f.read()
    print(data)    

# truncate:you can truncate the file to the specific size
with open("file2.txt","w") as f:
    f.write("hello world!!")
    f.truncate(5)
    
    


    
    
    
    