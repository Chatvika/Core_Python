'''  Polymorphism : one thing many forms.
the same method name or operator behaves differently based on the object or data type'''
print(len("Chatvika"))
print(len([1,2,3]))

'''Types :

1). Overloading: 

             Types of Overloading:

                              --Operator Overloading

                              --Method Overloading

                              --Constructor Overloading
2). overridding
                        --method overriding
                        --
                        --
3). ducktype'''




#1.1)   Operator OverLoading:

        # # All Arithmetic Magic Methods : Operator overloading allows operators to behave differently using magic methods.



class calculate:
        def __init__(self,value):
                self.value=value

        def __add__(self,other):
              return  self.value + other .value
        def __sub__(self,other):
              return  self.value - other.value
        def __mul__(self,other):
               return self.value * other .value
        def __truediv__(self,other):
              return  self.value / other.value
        def __floordiv__(self,other):
               return self.value //other.value
        def __mod__(self,other):
               return self.value % other.value
        def __pow__(self,other):
                return self.value ** other.value
        
a=calculate(20)
b=calculate(6)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# 1.2)  Method Overloading : Method overloading is achieved in Python using default arguments or *args.

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(10))          # 10
print(obj.add(10, 20))      # 30
print(obj.add(10, 20, 30))  # 60


# method over loading
print(10+20)
print("Hello" +"py")
print([1,2]+[3,4])

 

# ) Method Overloading using *args
class Calculator:
    def add(self, *args):
        return sum(args)

obj = Calculator()
print(obj.add(10))
print(obj.add(10, 20))
print(obj.add(10, 20, 30))

# 1.3). Constructor Overloading:  Creating objects using different arguments.

#   Python allows only one __init__ method,
#    but we simulate constructor overloading using default values


class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

s1 = Student("Ram")
s2 = Student("Sita", 20)

print(s1.name, s1.age)
print(s2.name, s2.age)






# method over loading
# print(10+20)
# print("Hello" +"py")
# print([1,2]+[3,4])

# 2.1).method overiding
class A:
      def show(self):
            print("iin A show ")
class B(A):
      def show(self):
            print("iin B show ")
obj=B()
obj.show()
 
# 2.2) constructor overiding:When a child class defines its own __init__() method, it replaces (overrides) the parent class constructor.

# If a child class has its own constructor, the parent constructor  will not run by default.
# We need to use super() to call the parent constructor manually.    
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        print("Child constructor")

obj = Child()


# DUCKTYPE: