# Definition : nested class is a class that defined "Inside another cass"
# syntax
class outer:
    class inner:
        pass
# ex:

class college:
    class student:
        def display(self):
            print("Student belongs to college")
s=college.student()
s.display()

# Using Constructor in Nested Class

class Company:
    class Employee:
        def __init__(self,name,salary):
            self.name= name
            self.salary=salary

        def show(self):
            print(self.name)
            print(self.salary)
c=Company.Employee("dulqar",29000)
c.show()

# Access Inner Class using Outer Class Object

class Outer:
    def __init__(self):
        self.inner=self.Inner()
    
    class Inner:
        def msg(self):
            print("Hello WOrld")
o=Outer()
o.inner.msg()

# Real-Time Example
class Bank:
    def __init__(self):
        self.acc=self.Account()
    class Account():
        def details(self):
            print("Account details displayed")
b=Bank()
b.acc.details()