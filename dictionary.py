# dictionaries are ordered(python 3.7 onwards) pairs of keys values, with unique keys 
# initialising dictionary  
a={}
print(type(a))

dic={"name":"annu"}
print(dic["name"])

info={"name":"priya","age":32,"is_eligible":True}
# if key does not exists so info["name"] will raise an error whereas get returns None 
print(info["name"])
print(info.get("name"))

print(info.keys())   #returns all the keys
print(info.values())  #return all the values
print(info.items())  #return all the keys values pairs

for key,value in info.items():   #it will unpack the tuple
    print(f"her {key} is {value}")
    
#dictionary method
d1={1:23,2:45,3:56,4:67,5:89,6:76}
d2={'a':"A","b":"B","c":"C"}
d1.update(d2)  #it will add d2 in d1
print((d1))
d2.clear() #it will clear all the items from d1
d1.pop(1)  #it will remove key value pair of 1
d1.popitem(6)   #it will remove last element
del d1[1]   #it will remove key value pair of 1
       






