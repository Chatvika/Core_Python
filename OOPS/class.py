# class : class is the bluprint or templete. eg:form for an exam fill details,name,father name name,age.



# 1)
company="HP"
class Employee:
# company="HP"


    def get_salary(self):   
                              # ''' self is imp here bcoz self is way to reference to the object of classs which is being created
        return 34000
e1=Employee()
print(e1.get_salary())

e2=Employee()
print(e2.get_salary())
# print(e2.company)

#  encapsulation

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)
s = Student("chatvika")
s.show()

# Encapsulation → data + methods in one class

# Abstraction → hide logic, show only function

# Inheritance → child uses parent properties

# Polymorphism → same method, different output 


# inheritance

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

c = Child()
c.show()


class company:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
w=company("Harika")
w.show()

# Print all characters in a string one by one.
s="chatvika"
for ch in s:
    print(ch)
    
# Print all characters in a string one by one.
s="banana"
ch="a"
count=0
for i in s:
    if i==ch:
        count+=1
print(count)

# Reverse a string without using slicing.
s="chatvika"
rev=""
for i in s:
    rev=i+rev
print(rev)
# Check whether a number is even or odd.
ch=int(input("enter a anumber:"))
if ch %2==0:
    print("Even")
else:
    print("odd")
# Find the largest of three numbers.
a=10
b=20
c=40
print("Largest number: " ,max(a,b,c))
        #    or

a,b,c=10,20,15
if a>b and a>c:
    print("Largest num is :" , a)
elif b>=a and b>=c:
    print("Largest num is", b)
else:
    print("Largest num is:",c)
# Check if a string is a palindrome.
s="madam"
rev=""
for i in s:
    rev=i+rev
if s==rev:
    print("palindrome")
else:
    print("Not palindrome")