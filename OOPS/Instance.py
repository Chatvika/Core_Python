class Employee:
    company="Nexus" # class attribute
    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of employee {self.name}.Salary is {self.salary} .the bond is {self.bond} years")
    
e1=Employee(34000, "chatvika", 3,"Tesla") 
print(e1.company) # instance attribute   
e1.get_info()
print(Employee.company) #this will always print class attribute

# object introspection
print(dir(e1))

# 
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name : {self.name}")
Person("sammer").show_name()


# 
class student:
    def __init__(self,random):
        self.random=random
    def shown(self):
        print(f" Random num:{self.random}")
student(98720283).shown()
# 
class Employee:
    def __init__(self,salary):
        self.salary=salary
    def display(self):
        print(f"salary : {self.salary}")
Employee(50000).display()
# 
class user:
    def __init__(self,age):
        self.age=age
    def show_age(self):
        print(f" Age: {self.age}")
user(30).show_age()


# 
class Employee:
    company = "Nexus"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name : {self.name} | Company : {self.company}")


e1 = Employee("Chatvika")
e2 = Employee("Anu")

e2.company = "TCS"   # instance level override

e1.show()
e2.show()
