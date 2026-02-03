# a = 33
# b = 12
# c = 45
# average = (a+b+c)/3
# print(average)

# a1 = 12
# b1 = 90
# c1 = 90
# average1 = (a1+b1+c1)/3
# print(average1)


def average(a,b,c):
    d=(a+b+c)/3
    print(d)
average(3,5,1)

def average(d,e,f):
    return d
o1 = average(8,9,3)
o2 = average(6,8,4)

print(o1)
print(o2)

#ARGUMENTS


#1).positinal Argument

def add (a,b):
    return a+b
print(add(5,3))


#2).default arguments

def greet (name = "Guest"):
    return f" Hello ,   {name}!"
print(greet())

#3).Function with parameters 
def add(a, b):
    print("Sum =", a + b)

add(10, 5)

#4). Function with return
def square(n):
    return n * n

result = square(4)
print(result)

#5).Function using multiple statements
def info(name, age):
    print("Name:", name)
    print("Age:", age)

info("Chatvika", 21)

#modules
import math

print(math.sqrt(15))

#
from math import sqrt

print(sqrt(25))

#
import math

print(math.sqrt(25))   # square root
print(math.pi)         # PI value
print(math.pow(2, 3))  # 2^3

#lamda
# square = lambda x= x *x
print(square(4))

def add(*args):
    return sum(args)
print(add(2,3))

def sum(**kwargs):
    print (kwargs)
sum(name="Chatvika",age=20)

