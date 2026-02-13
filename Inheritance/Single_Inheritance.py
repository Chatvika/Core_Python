# Single → One parent, one child

# Multilevel → Parent → Child → Grandchild

# Multiple → Many parents, one child

# Hierarchical → One parent, many children

# Hybrid → Combination of inheritance types



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

# 
