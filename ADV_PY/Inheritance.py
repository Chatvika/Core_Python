# SINGLE LEVEL INHERITANCE

# In Inheritance ,we uusually create a an object of child class because of it can access both parent and child class.
# One parent → one child
class a:
    def show(self):
        print("Class A")
class b(a):
    def display(self):
        print("Class B")
obj=b()
obj.show()
obj.display()



# 

class Animal:
    def held(self):
        print(" ***")
class Dog(Animal):
    def display(self):
        print("Bow Bow")
obj=Dog()
obj.held()
obj.display()

# 
class Vehicle:
    def ride(self):
        print("Vehicle is riding")
class Bike(Vehicle):
    def start(self):
        print("Bike is started")
obj=Bike()
obj.ride()
obj.start()

# multiple
        # Multiple parents → one child
class Father:
    def f(self):
        print("Father Method")
class Mother:
    def m(self):
        print("Mother Method")
class child(Father,Mother):
    def c(self):
        print("Child method")
obj=child()
obj.f()
obj.m()
obj.c()


# 
class method:
    def xyz(self):
        print("XYZ")
class solid:
    def abc(self):
        print("ABC")
class coil(method,solid):
    def ghi(self):
        print("GHI")
obj=coil()
obj.xyz()
obj.abc()
obj.ghi()


class ajhf:
    def sksjd(self):
        print("sdsjhd")
class pqoei:
    def pqowe(self):
        print("qoieur")
class qoeiur(ajhf,pqoei):
    def adj(self):
        print("ksjdh")
obj=qoeiur()
obj.sksjd()
obj.pqowe()
obj.adj()