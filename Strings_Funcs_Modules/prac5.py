ch ="Chatvika"
print(ch[::-1])
print(ch[3])
for i in ch:
    if i=="h":
        print(i)




#FUNCTIONS
#  keyword arguments
# behave like dictinary
# SYNTAX
def function_name(**kwargs):
    print(kwargs)

# ex:
def student_details(**kwargs):
    print(kwargs)
student_details(name="asd",age=21,skill="py")

# ex 2:Acess values
def emp_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
emp_details(name="John", age=30, department="HR")

# ex: 3 with other arguments
def demo(a,b,**kwargs):
    print(a)
    print(b)
    print(kwargs)
demo(10,20,x=30,y=40)


# Print all keyword arguments
def show(**kwargs):
    print(kwargs)
show(a=10,b=20)

# 2). Display student details
def student_details(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
student_details(name="Alice", age=22, course="Math")
# 3).Print only keys
def keys_values(**kwargs):
    for k in kwargs:
        print(k)
keys_values(a=10,b=20)
# 4).print only values 
def values(**kwargs):
    for v in kwargs.values():
        print(v)
values(x=10,y=50)
# 5).Check if key "age" exists
def check_age(**kwargs):
    print("age" in kwargs)
check_age(name="Bob", age=25)


# lambda functions 
marks=[30,10,20,50]
bonus =list(filter(lambda x: x>=50,marks))
passed= list(filter(lambda x : x>=50,bonus))
from functools import reduce
total=reduce(lambda a,b:a+b,passed)
print(bonus)
print(passed)
print(total) 

# list comprehension:List comprehension is a short way to create a list in a single line using .
# expression + for loop + optional condition.
# syntax :
# [expression for item in iterable if condition]

# ex:
square=[x*x for x in range(1,6)]
print(square)

# tuple  :Python does NOT have real tuple comprehension.
# When we use parentheses (), it creates a generator expression, not a tuple.
# ex:
squares=(t*t for t in range(1,6))
print(squares)


# ex 2:
squares=tuple(t*t for t in range(1,6))
print(squares)

# generate a random phone number.
import random

phone_number = random.randint(6000000000, 9999999999)
print(phone_number)



#set comprehension : to remove aduplicates.
# ex:
names=["rama","sita","rama","swetha"]
unique_names={n for n in names}
print(unique_names)


# questions practise comprhensions
# list comprhensions
# 1). Numbers from 1 to 10
nums=[i for i in range(1,21)]
print(nums)

# 2). Squares of numbers from 1 to 10
square=[i*i for i in range(1,21)]
print(square)
# 3).even numbers from 1 to 10.
even=[i for i in range(1,21) if i%2==0]
print(even)
# 4). Odd numbers from 1 to 20
odd=[i for i in range(1,21) if i%2!=0]
print(odd)
# 5). Multiply each element by 3
lst=[2,4,6,8]
result=[i*3 for i in lst]
print(result)
# 6).Even numbers only
lst1=[1,2,3,4,5]
result1=[i for i in lst1 if i%2==0]
print(result1)
# 7). Characters from string
str="Chatvika"
res=[i for i in str]
print(res)
# 8). Numbers greater than 20
x=[1,2,3,4,5,6,7,29,27]
final=[i for i in x if i>20]
print(final)
# 9). Square of even numbers only
lst=[1,2,3,4,5,6,7]
sqr=[i*i for i in lst if i%2==0]
print(sqr)
# 10). Vowels from string
s="Hy hello world"
vowels=[ch for ch in s if ch.lower() in "aeiou"]
print(vowels)

# set comprhensions
#1). Square of even numbers only
lst=[1,2,3,4,5,6,7]
sqr={i*i for i in lst if i%2==0}
print(sqr)

# 2). Divisible by 3 (1–30)
nums={i for i in range(1,31) if i%3==0}
print(nums)

# 3).Characters from string
sum="tvika"
s={ch for ch in sum }
print(s)
# 4). Unique lowercase letters
letters = {ch.lower() for ch in "Python Programming" if ch.isalpha()}
print(letters)
# 5). Numbers greater than 25
lst = [10, 20, 30, 40, 50]
result = {i for i in lst if i > 25}
print(result)

# List comprehension → [ ] → ordered, duplicates allowed

# Set comprehension → { } → unordered, duplicates removed


# nested  loops
#  nested for loop
for i in range(2, 4): # Outer loop
   for j in range(1, 11): # Inner loop
       print(f"{i} * {j} = {i*j}")
   print() # Blank line after each table

# 2). 
adj= ["red","big","orange"]
colors=["apple","banana","pineapple"]
for fruit in adj:
    for color in colors:
        print(fruit,color)


# 3)
rows=int(input("Entera number of rows: "))
columns=int(input("Enter a number of columns:"))
symbol=input("Enter a  symbol to  use:")
for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()
# 4).

rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# 5).
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print() 