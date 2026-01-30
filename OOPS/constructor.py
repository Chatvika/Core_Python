
# constructor
class Employee:
    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of employee {self.name}.Salary is {self.salary} .the bond is {self.bond} years")
    
e1=Employee(34000, "chatvika", 3) 
print(e1.get_salary())
e1.get_info()


class student:
    def fsdname(self):
        sar="asdfg"
        tee="ertys"
        fee="rete"
        print(tee)
        print(sar)
    def __init__(self):
        yar="asdoo"
        ram="retet"
        sri="ghuuu"
var=student()
var.fsdname()



# .
class Employee:
    def __init__(self,salary):
        self.salary=salary
    def show(self):
        print(self.salary)
e1=Employee(34000)
e1.show()

# 
class Student:
    def __init__(self,sname,sid):
        self.sname=sname
        self.sid=sid
    def display(self):
        print(self.sname)
        print(self.sid)
s=Student("ANR",123)
s.display()


# 
class person:
    def __init__(self,name="Unknown",age=0):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name : {self.name} . Age: {self.age}")
c1=person("Chatvika", 2)
c2=person()  #use defaullt values 

c1.display()
c2.display()

# 
class Employee:
    def __init__(self,name,id,salary,hike):
        self.name=name
        self.id=id
        self.salary=salary
        self.hike=hike
    def show(self):
        print(f"name:{self.name}|,age {self.id} ,| salary {self.salary} | hike {self.hike}")
e2=Employee(" williams",23,87000,2000)
e2.show()