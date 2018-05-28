# coding:utf8
import numpy
import scipy

print (1+2)
print (3+4)

mysum = 1+2
print(mysum)

a, b = 1, 2
c = d = 1
print(a, b)
print(a); print(b)
print(c, d)

myint = 1
myfloat = 1.0
mystr = "Hello"
mybool = True

print(type(myint))
print(type(myfloat))
print(type(mystr))
print(type(mybool))
print(type(a))

print('This is a "quote"')

print(1+2)
print(1+2==3)

myint = 1
print(myint)
print(float(myint))

print(int(False),bool(0))
print(int(True),bool(1))
print(bool("Hello"))

print(type(None))
print(bool(None))

print("He" + "l" * 2 + "o!") 
print(True + False)
print(True * 2)

savings = 100
print("I have " + str(savings) + " USD in my account.")
print("I have ", savings, " USD in my account.")


mylist1 = ["sam", 1.75, "sara", 1.82] # mylist1 contains strings and numbers.
mylist2 = [["sam", 1.75], ["sara", 1.82]] # mylist2 contains lists, and each list contains a string and a number.
print(mylist1)
print(mylist2)
print(type(mylist1))

list1, list2 = [1,2], [3,4]
print(list1, list2)

slice = mylist1[:7]
print(slice)
print(mylist[5:])

print("sara"[0])
print("sara"[0:2])