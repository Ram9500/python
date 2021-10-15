# Type casting - works on valid convertion
"""
a = float(100)
print(a, type(a))

b = int(55.99)
print(b, type(b))

c = str(100)    # c = "100"
print(c, type(c))

d = float("100.78")    # 
print(d, type(d))
"""


# input()
"""
print("Enter a number")
a = input()
x = int(a)
print("the user value =",x,type(x))

print("Enter a number")
b = int(input())
print("the user value =",b,type(b))

c = x + b
print("sum =", c,type(c))
"""

# operators
"""
print(10+3)    # 13
print(10-3)    # 7
print(10*3)    # 30
print(10**3)   # 10 power of 3 = 1000
print(10/3)    # 3.3333
print(10//2)   # Quoient = 3
print(10%2)    # Remainder = 1
"""
# assignment operator (while loop)
"""
a = 10 
print(a) # 10

a += 5   # a = 10 + 5
print(a) # a = 15

a *= 2   # a = 15 * 2
print(a) # a = 30
"""

# comparision ope (while, if else)
# return T/F
"""
print(10 == 10) # T
print(10 != 10) # F
print(10 >= 10) # T
print(10 > 10)  # F
print(10 <= 10) # T
print(10 < 10)  # F
"""

# 
"""
print(10==10 and 4<6) # T and T = T
print(10==10 and 4>6) # T and F = F
print(10==10 or 4>6)  # T or F = T
print(not 10==10)     # not T = F
"""

# pep 8 - coding rules
"""
print("Enter a number")
a = input()
x = int(a)
print("the user value =", x, type(x))

print("Enter a number")
b = int(input())
print("the user value =", b, type(b))

c = x + b
print("sum =", c, type(c))
"""

# Collection

# array - collection of similar data type
# List  - collection of data type
"""
#    0   1     2      3    4  - indexes
a = [1,2.55,'hello',False,6j,1,1,1,1,1,1]   # duplicate members
print(a, type(a))

print(a[2])  # ordered
a[2] = 99    # modifyable
print(a)
"""

# tuple 
"""
#    0   1     2      3    4  - indexes
a = (1,2.55,'hello',False,6j,1,1,1,1,1,1)   # duplicate members
print(a, type(a))
print(a[4])  # ordered

a[2] = 99    # unmodifyable
"""

# set
"""
a = {'a','b','c','d','a','a','b','c'}   # no duplicate members
print(a, type(a))
"""

# if else - decision statement
# syntax 
"""
if <condition T/F>:
elif <condition T/F>:
else:
"""

# if example
"""
a = 500
if a>10:
    print("a is bigger than 10")
"""

# if + Indentation
"""
a = 50
if a>10:
    print("a is bigger than 10")
    print("code inside if")
    print("hello world")
print("end of if")
"""

# if else + Indentation
"""
a = 5
if a>10:
    print("a is bigger than 10")
    print("code inside if")
    print("hello world")
else:
    print("a is smaller than 10")
    print("code inside else")
print("end of if")
"""

"""
a = 10
if a>10:
    print("a is bigger than 10")
    print("code inside if")
    print("hello world")
elif a==10:
    print("a is 10")
else:
    print("a is smaller than 10")
    print("code inside else")
print("end of if")
"""

# syntax 
"""
if <condition T/F>:     (compulsary) (only once)
elif <condition T/F>:   (optional)   (as many as you want)
else:                   (optional)   (only once)
"""
# example
"""
a = 10
if a>10:
    print("a is bigger than 10")
elif a==10:
    print("a is 10")
elif a==50:
    print()
elif a==90:
    print()
else:
    print("a is smaller than 10")
print("end of if")
"""

# example
"""
a = 100
if a==10:
    print(10)
elif a==20:
    print(20)
"""

# loop
# while loop - numbers
# for loop   - string/list/tuple/set

# while loop - syntax
# while <condition T/F>:
"""
a = 1
while a<=5:
    print(a)
    a = a + 1
print("loop over")
"""

# example
"""
a = 70          # initilization/ start
while a<=100:     # condition/ stop
    print(a)
    a = a + 5   # incremenation/ add or jump
print("loop over")
"""

# Ctrl + C : KeyboardInterrupt
"""
a = 1          # initilization/ start
while a>0:     # condition/ stop
    print(a)
    a = a + 1   # incremenation/ add or jump
print("loop over")
"""

# for loop syntax
# for <variable> in <string/list/tuple>:

# string - fetches letter by letter
"""
for abc in "hello world":
    print(abc)
"""

# list - fetches item by item
"""
mylist = [1,2.33,"hello world",100]
for i in mylist:
    print(i)
"""

# python standard functions 
"""
input()
type()
id()
print()
int()
"""

# user defined functions syntax
# def <func name>():

# step 1: func + calling
"""
def Ram():  # func creation
    print("hello world")
    print("code inside Ram func")

def myfun():
    print("hello myfun")

myfun()
Ram()
myfun()
"""
# step2: func + arguments
"""
def myfun(a,b):
    print("sum = ", a,b)


myfun(20,50)        # argument
myfun(4.5,6.7)
myfun('hello','moon')
"""
# step3: func + default argument
"""
def myfun(a=0,b=0):
    print("values are", a,b)

myfun()
myfun(88)
myfun(b=88)
myfun(10,20)
"""
# step4: func + arbitrary argument
"""
def myfun(*a):          # *a = arbitrary argument, it will store inside a tuple
    print("values are", a, type(a))
    b = list(a)
    print(b)

myfun()
myfun(1,2)
myfun(1,2,3,5,56,6,8,5,78,9,6,6,6,6,6)
"""
# step 5: func + return
"""
def myfun():
    print("hello world")
    return 100

def anotherfun():
    print("hello moon")
    return 500

x = myfun() + anotherfun() + myfun()
print(x)
"""
# hello world
# hello moon
# hello world
# 700


# library
"""
import math
x = math.sqrt(24)
print(x)
"""


# library
"""
import myown123
print(myown123.x)
print(myown123.y)
myown123.myfun()
"""

# boto3

# pip install boto3
# pip install awscli
# aws configure

#import boto3

# programming language - c,c++,java,python,perl,php
# scripting - python,perl,php
"""
import os
import time

os.mkdir("D:/filke")

time.sleep(7)

os.rmdir("D:/filke")
"""

"""
import boto3
x = boto3.resource('ec2')
x.create_key_pair(KeyName='awskey1402')
"""

"""
import boto3
x = boto3.resource('ec2')
x.create_instances(ImageId='ami-08e0ca9924195beba',InstanceType='t2.micro',KeyName='awskey1402',MaxCount=5,MinCount=1)
"""


   



