class Test:
    def __del__(self):
        print("Object destroyed")


# working with Gc modules
# useless object
# useful object
# desturctor

# useful
class Employee:
    def __init__(self):
        self.name = "Ravi"
        print("Employee created")

    def __del__(self):
        print("Employee destroyed")

e = Employee()
del e
# Destructor USELESS
class A:
    def __init__(self):
        self.b = None

    def __del__(self):
        print("A destroyed")

class B:
    def __init__(self):
        self.a = None

    def __del__(self):
        print("B destroyed")

a = A()
b = B()

a.b = b
b.a = a   # circular reference

del a
del b
