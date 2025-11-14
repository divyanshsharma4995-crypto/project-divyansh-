x=23
y="hello"
print(x)
print(type(x))
print(y)
print(type(y))



z=5.4
print(z)
print(type(z))



# my_var=40
# print(my_var)

x,y,z="30","40","50"
x="30","40","50"
print(x)
fruits=["apple","banana","cherry"]
x,y,z=fruits
x=y=z=fruits
fruits=[2,4,7,8,34]
print(type(fruits))
x="good"
def my_func():
    print("python is " + x)
my_func()

def my_func():
    global x
    x="good"
    my_func()
print("python is " + x)

x=5
print(type(x))

x="name" 
print(type(x))

x={"apple", "banana", "cherry"}
print(type(x))

x="good"
print(range(x))

x=56
y=10
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

my_list=["apple","banana","cherry"]
print(my_list[1])
print(my_list[-1])

my_list=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(my_list[2:5])

my_list=["apple","banana",1,3,5,7]

my_list[2:5]=["abc"]

print(my_list)

my_list=[1,2,4,5,6]

my_list.insert(2,3)

print(my_list)

my_list=[1,2,3,4,5]
my_list.insert(2,"hahahah")
my_list.append(6)
print(my_list)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)


list1=[1,2,3,"apple",4,5]

list1.pop(2)
print(list1)


# list1=[1,2,3,4,5,6]
# list1.insert(2,"apple")
# print(list1)
# list1.append("banana")
# print(list1)
# list1.remove("apple")
# print(list1)
# list1.pop()
# print(list1)
# list1.clear()
# print(list1)

list1=[]
list1.append(1)
print(list1)
list1[0]="hello" 
print(list1)

# loopslists

# list1=[1,2,3,4,4,4,4,5]
# for x in list1:
#     print(x)

    # sort
list=[2,5,1,4,8]
list.sort()
print(list)

list=[2,5,1,4,8]
list.sort(reverse=True)
print(list)

text="hello"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("hello","world"))
print(text.split())

# format strings



x="bob"
y=20
print(f"my name is {x} and my age is {y}")

x=5
x+=4
print(x)
x-=2
print(x)
x*=3
print(x)
x/=4
print(x)
x%=3
print(x)
x**=2
print(x)
x//=2
print(x)

x=5
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
x=8
y=x
z=12
# print(y)
print(x is y)
print(x is not y)

# colors=["red","green","blue"]
# for x in colors:
#     print(x)


students={"name":"bob","age":20,"city":"new york"}
students.pop("age")
del students["city"]
print(students)

# if else in python

age=20
if age>=18:
    print("you are adult")
elif age==18:
     print("you are teen")
else:

    print("you are minor")

    # nested if 

x=15
if x>10:
    print("x is greater than 10")

    if x>20:
        print("x is also greater than 20")
    else:
        print("x is greater than 20")

        x=15

        if x%2==0:
            print("x is even")
        else:
            print("x is odd")

            #  python for loops

fruits={"apple","banana","cherry"}
for fruit in fruits:
        print(fruits)


word="python"
for x in word:
    print(x)

for i in range(5):
        print(i)


for i in range(1,10,2):
       print(i)

# nested for loop

for i in range(1,4):
       for j in range(1,3):
              print(f"i={i},j={j}")

# break

for i in range(1,6):
  if i==4:
       break
print(i)    

# print all number from 1 to 20 using a for loop
for i in range(1,21):
    print(i)

# print all even numbwr less than 30 using range()
for i in range(2,30,2):
    print(i)

# iterate over a list of your favorite colors and print them
colors=["red","blue","green","yellow"]
for color in colors:
    print(color)

# use a nestedfor loops to print a 3*3 multiplication table
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}*{j}={i*j}") 
# python function 

def greet():
    print("hello world")
greet()

# function with parameters

def greet(name):
    print(f"hello {name}")
greet("Alice")
greet("Bob")

# fuction with return value

def add(a,b=10):
    return a+b
result=add(5,3)
print(result) # 8

#function with default parameter

def greet(name="Guest"):
    print(f"hello {name}")
greet()  # hello Guest

 # scope of variables 

x=10 # global

def my_function():
    y=5
    print(x,y)
    my_function()
print(x)
    # oops in python 
# class and object 

# class
class Car:
    def __init__(self,brand,color):
      self.brand=brand # attribute
      self.color=color # attribute

    def drive(self): # method
      print(f"The {self.color} {self.brand} is driving🚘")

    #object
car1=Car("Toyota","Red")
car2=Car("Honda","Blue")

car1.drive()
car2.drive()

# python arrays 
# array is a collection of item of the same type 

# import array 
# numbers = array.array('i', [1, 2, 3, 4, 5])
# print(numbers)

# from numpy import random

# x= random.randint(100)
# print(x)

# x= random.rand()
# print(x)
# print(type(x))
from numpy import random

# x=random.randint(100,size=(5))
# print(x)

# x=random.randint(100,size=(3,4))
# print(x)

# x=random.randint(100,size=(3,4,5))
# print(x)

# x=random.choice([4,5,6],size=(2,3,5))
# print(x)

# pandas 

import pandas as pd
# data=[10,20,30,40]
# s=pd.Series(data)
# print(s)

# data frame

# similar to an exel spreadsheet or sql table
# a two dimensional data structure(row+colomn)
# each colomn is a series and all cloumns together form a data frame

# data={
#     "name":["Alice","Bob","Charlie"],
#     "age":[25,30,35],
#     "city":["New York","Los Angeles","Chicago"]
# } 


# import numpy as np
# arr=np.array([1,2,3,4,5])
# s=pd.Series(arr)
# print(s)

# from a dictionay

data={"math":90,"science":85,"english":88}
s=pd.Series(data)
print(s)

