'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict)) #<class 'dict'>
print(len(thisdict)) 
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])
print(thisdict.values())
print(thisdict.items())

#----Update----

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#----Loop----

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
for x in thisdict.values():
  print(x)
