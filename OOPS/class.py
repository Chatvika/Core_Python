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
print(e2.company)

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






