'''
A set is a collection which is unordered, unchangeable*, and unindexed.

Duplicates Not Allowed

'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'apple', 'cherry', 'banana'}
print(len(thisset))
print(type(thisset)) #<class 'set'>


'''
Sets are unordered collections, so they don’t support indexing or slicing like lists or tuples do.
'''

#Convert the set to a list or tuple (which allows indexing)

thisset = {"apple", "banana", "cherry", "apple"}
x = list(thisset)
print(x[0]) #apple
x[0] = "Jack Fruit"
thisset = set(x)
print(type(thisset)) #<class 'set'>

#---Loop----

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#---Set Join---

'''
The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
