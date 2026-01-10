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
text=f.write("\n hello everyone!!!")
f.close()  

with open("my_file.txt","a") as f:
    f.write("\n hey i am inside") 



f=open("my_file.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)
    