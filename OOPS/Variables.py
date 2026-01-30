# In Python OOP, variables can be categorized into instance variables,
#  class/static variables, local variables, and default arguments.

# 1)local variable
class student:
    def display(self):
        message="Hello"
        print(message)
s1=student()
s1.display()

# 1.1)
class Employee:
    def calculate(self):
        # Defining & Declaring 
        bonus=3000 #local variable

        # accesssing &printing
        print("bonus",bonus)

        bonus = bonus +2000
        print("Updated bonus",bonus)

          # Deleting (manual delete)
        del bonus
        print("Local variable deleted")


M=Employee()
M.calculate()





#2) instance variable
class Student:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age        # Instance variable

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

print(s1.name, s1.age)  # Alice 20
print(s2.name, s2.age)  # Bob 22


# 2.1)
class Employee:
    #Defining & Declaring instance variables
    def __init__(self,name,salary,bond):
        self.name=name
        self.salary=salary
        self.bond=bond
    def operations(self):
        #  Accessing
        print(f"name:{self.name}")
        #  Printing
        print(f"name:{self.name},salary:{self.salary},bond:{self.bond}")
        # 
        self.salary+=5000 #updating
        print(self.salary)

        print(f"Employee Info -> Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} yrs")

        # deleting
        del self.bond
        print("Bond variable deleted")

e1 = Employee("Chatvika", 34000, 3)

# Perform all operations
e1.operations()   


# 3) static variable

class Student:
    school_name = "Kranti School"  # Class/Static variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school_name)  
print(s2.school_name)  
Student.school_name = "XYZ School"  
print(s1.school_name)  


# 3.1)
class Employee:
    company="Infosys"
    
    def show(self):
        print("Company:",Employee.company)

    # updating
    Employee.company="TCS"
    print(" Updated Company:",  Employee.company)


    # deleting
    del Employee.company
    print("Static variables are deleted")

emp=Employee()
emp.show()






#4)   default variable

class Student:
    def __init__(self, name="Unknown", age=18):  # Default arguments
        self.name = name
        self.age = age

s1 = Student()  
s2 = Student("Alice", 20)

print(s1.name, s1.age)  # Unknown 18
print(s2.name, s2.age)  # Alice 20



# 4.1)
class Employee:
    def __init__(self,name,salary=20000):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)
        # updating
        self.salary+=5000
        print("After updated salary:",self.salary)
        # delete
        del self.salary
        print("Declared variable deleted")
e1=Employee("Rohan")
e1.display()


 
class Employee:
    def __init__(self):
        lst=[1,2,3]
        print(lst)
e1=Employee()
         