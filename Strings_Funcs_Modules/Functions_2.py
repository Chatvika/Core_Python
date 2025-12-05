# Function: A function is a block of code written to perform a specific task. It is reusable and helps reduce repetition.

# TYPES of Functions
# 1. Pre-defined functions (Built-in)

# Already available in Python.
# Examples: print(), len(), type(), input()

#  2. User-defined functions

# Functions created by the programmer using def.

#ex:
def greet():
    print("Hello")


#Parameters
#1).Formal parameters: variables declared in function definition.
#2). Actual parameters : values you pass when calling the function.

#ex:
def add(a,b): #a,b are formal
    return a+b
add(5,3)   #5,3 are actual

#Types of Arguments
#1).Positional Arguments :Order matters
def student(name,age):
    print(name,age)
student("chatvika","21")


#2). keyword Arguments: order dos'nt matter.

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
student(age=21, name="Chatvika", course="MCA")

#3).Default Arguments : provide default values.

#ex:
def greet(name="Guest"):
    print("Hello", name)
greet("Chatvika")

#4).Variable-Length Arguments : *args → multiple values
#                                **kwargs → multiple keyword values
def add(*nums):
    print(sum(nums))

def info(**data):
    print(data)


x = 10   # global

def show():
    global x
    x = 20

show()
print(x)   # 20





