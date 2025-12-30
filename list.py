# lists are ordered collection of datatype.
# they store multiple items in a single variable.
# lists are changeable(mutable) meaning we can alter them after creation.
lst=[23,4,5,6,"annu",True]
print(lst)
print(type(lst))    #list
print(lst[4])
print(lst[1:4])

if "annu" in lst:
    print("yes")
else:
    print("no")
    
my_list=[i*i for i in range(20)]
print(my_list)

lsts=[i for i in range(10) if i%2==0]
print(lsts)

#list methods 
l=[3,6,2,3,8,5,3,4,8,4]
l.append(45)   #it will append element at the end
print(l)
l.sort()  #arrange the elements default(ascending order)
print(l)
l.sort(reverse=True) #decending order
print(l)
l.reverse()  #reverse the order of list
print(l)
print(l.index(45)) #return the index of first occurance of the list item
print(l.count(8))  #count the number of items in list
m=l.copy()  #return copy of the list
print(m)
l.insert(2,56) #insert element at a given index
print(l)
n=[23,45,78,89,678]
l.extend(m) #add list at the end
print(l)
 

   
        
