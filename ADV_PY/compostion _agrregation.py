# Aggregation – Syntax
class A:
    pass
class B:
    def __init__(self,obj):
        self.obj=obj  #Aggregation

# ex:
class College():
    def __init__(self,name):
        self.name=name
class Student():
    def __init__(self,student_name,college):
        self.student_name= student_name
        self.college=college
    def display(self):
        print(self.student_name)
        print(self.college)
c=College("ANR")
s=Student("CHATVIKA" , c)
s.display()


# composition -Syntax
class B:
    pass
class C:
    def __init__(self):
        self.obj=B()

# ex
class Engine():
   def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

c = Car()
c.drive()

