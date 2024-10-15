x = [1,2,3,4,5]
y = ["mango","banana","apple"]

print(len(x)) #5
print(len(y)) #3

x.append(10)
print(x) #[1,2,3,4,5,10]

z = x.copy()
print(z) #[1,2,3,4,5,10]

z = z.clear()
print(z) #None

x.extend(y)
print(x) #[1, 2, 3, 4, 5, 10, 'mango', 'banana', 'apple']

z = [3,6,5,2,4,1]
z.sort()
print(z) #[1, 2, 3, 4, 5, 6]

z.reverse()
print(z) #[6, 5, 4, 3, 2, 1]

z.pop()
print(z) #[6, 5, 4, 3, 2]

z.pop(3)
print(z) #[6, 5, 4, 2]

'''
--Array Methods--

append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()

Visit for example:
https://github.com/nooraalam1/Python_Crash/blob/main/Array%20Methods.pdf

'''
