# sets are unordered collection of data items.sets is immutable and store unique element in it
#initialising set
my_set=set()
type(my_set)

s={1,2,3,4,5,6}
print(type(s))
print(s)

# set method
set1={1,2,3,4,5}
set2={5,7,9,10,11,34}
print(set1.union(set2))  
set1.update(set2)
print(set1)
# the union and update method print all items present in two sets.the union method return the new set whereas update method add items into the existing set

a=set1.symmetric_difference(set2)
print(a)
b=set1.intersection(set2)
print(b)
c=set1.isdisjoint(set2)
print(c)
d=set1.issubset(set2)
print(d)
e=set1.issuperset(set2)
print(e)
set1.remove(1)
set2.discard(3)
# the main difference between remove and discard is, if we try to remove element which is not present in set so remove raise an error whereas discard does not raise any error.
set1.pop()
# pop remove any random element and return it because set is unordered.
del set1
# del deletes whole set1
set2.clear
# clear removes all the items from set2



