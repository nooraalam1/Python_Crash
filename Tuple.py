'''
Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

'''

my_tuple = ("mango",10,"apple",50)
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple)) #<class 'tuple'>

my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[2:5]) #('cherry', 'orange', 'kiwi')

my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[-4:-1]) #('orange', 'kiwi', 'melon')

'''
----Change Tuple Values----
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

 You can convert the tuple into a list, change the list, and convert the list back into a tuple

'''

my_tuple = ("mango","apple","banana")
x = list(my_tuple)
print(type(x)) #<class 'list'>

x.insert(1,"Jackfruit")
x = tuple(my_tuple)
print(my_tuple) #('mango', 'apple', 'banana')
print(type(my_tuple)) #<class 'tuple'>

'''

----Methods---

append()
extend()
clear()
insert()
remove()
pop()
copy()
index()
count()
sort()
reverse()


'''

 
