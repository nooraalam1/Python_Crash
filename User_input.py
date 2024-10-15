x = input("Name:")
print("Your name is "+x)
print(type(x)) #<class 'str'>

y = input("Age:")
print(type(y)) #<class 'str'>

'''

input takes everything as a string. So we have to do type casting

'''

y = int(input("Age:"))
print(type(y)) #<class 'int'>
print(f"Your Age is {y}") #format string