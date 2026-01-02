# 1. Built-in Functions

# Predefined in Python and available without importing any module.
# Examples:
# print(), len(), type(), sum(), max(), min()

print(len("Python"))


#2).  user define function

# Created by the programmer using the def keyword.
# Can take parameters and return values.

def greet (name):
    return f"Hello,{name}"
print(greet("chatvika"))


def hello (s):
    return f"hey ,{s}"
print(hello("dfgh"))

#3) .lambda function

square=lambda x:x*x
print(square(5))



# 4. Recursive Functions

# Functions that call themselves to solve a problem.
# Useful for problems like factorial, Fibonacci, tree traversal.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 5. Functions with Different Argument Types
# Python supports multiple ways to pass arguments:


# Positional Arguments
# Passed in order
def add(a, b): return a+b


# Keyword Arguments
# Passed with parameter names
add(b=3, a=2)               





# 5. Functions with Different Argument Types
# Python supports multiple ways to pass arguments:
# Positional Arguments
# Passed in order
def add(a, b): return a+b


# Keyword Arguments
# Passed with parameter names
add(b=3, a=2)


# Default Arguments
# Have default values
# def greet(name="Guest"):


# Variable-length Arguments
# Accept multiple values
# *args (tuple), **kwargs (dict)


# def demo(a, b=10, *args, **kwargs):
    # print(a, b, args, kwargs)

# demo(1, 2, 3, 4, x=5, y=6)

# Built-in
# print(), len()


# User-defined
# def my_func(): ...


# Lambda
# lambda x: x+1


# Recursive
# factorial()


# Argument Variations
# Positional, Keyword, Default, *args, **kwargs

def fact_n(n):
   if n==0:
        return 1
   return n* fact_n(n-1)
n=int(input("Enter a number:"))
print(fact_n(n))

# EXAMPLES
# 1️). Predict the Output   
def show(a,b,c):
    print(a,b,c)
show(10,c=30,b=20 )

# 2).identify the errorr
def func(a,b):
    print(a,b)
# func(a=10, 20) # SyntaxError: positional argument follows keyword argument
# 3).Predict the Output
def add(a, b=5):
    return a + b

print(add(10))
print(add(10, 20))

# 4)Default Argument Concept
def test(x, data=[]):
    data.append(x)
    return data

print(test(1))
print(test(2))
# 5). Predict the Output
def demo(a, *b, c):
    print(a, b, c)

demo(10, 20, 30, c=40)
# 6).Predict the Output
def details(**info):
    print(info)

details(name="Sharik", age=21)
# 7). 
def mix(*args, **kwargs):
    print(args)
    print(kwargs)

mix(1, 2, 3, course="Python", level="Intermediate")

# 8).Find the Error
# def f(a, **b, *c)
    # print(a)     SyntaxError: invalid syntax

# 9). Predict the Output
def func(a, b=10, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)

func(5, 20, 30, 40, x=50, y=60)
# 10). Keyword-Only Argument Question
def fun(a, *, b):
    print(a, b)

# fun(10, 20)     
# add item in empty list 
def test(x,data={1,2}):
    data.add(x)
    return data
print(test(3))
print(test(6))

# positinal arguments
def func(a,b):
    print(a+b)
func(10,20)


def add_user():
    name=(input("Enter the number:"))
    age=int(input("Enter age:"))
    email=(input("Enter your email:"))
    user = {
        "name": name,
        "age": age,
        "email": email
    }
    return user
gef=add_user()
print(gef)
