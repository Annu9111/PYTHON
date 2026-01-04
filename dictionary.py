# dictionaries are ordered(python 3.7 onwards) pairs of keys values, with unique kyes 
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
    






