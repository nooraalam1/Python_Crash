'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.

List items are ordered, changeable, and allow duplicate values.

'''

my_list = [1,2,3,"mango","apple"]
print(my_list)
print(len(my_list))
print(type(my_list)) #<class 'list'>


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi'] --from index 2 to before index 5


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

