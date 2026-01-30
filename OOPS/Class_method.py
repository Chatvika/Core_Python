# classs method
class Myclass:
    count=0
    @classmethod
    def class_method(cls):
        cls.count+=1
        print(f"class method is called. Count ={cls.count}")
Myclass.class_method()



class Myclass:
    count=0
    @classmethod
    def class_method(cls):
        cls.count+=1
        print(f"Class method is called.Count{cls.count}")
Myclass.class_method()


class Student:
    college = "JNTU"

    @classmethod
    def change_college(cls, name):
        cls.college = name

Student.change_college("OU")
print(Student.college)



class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls, name):
        return cls(name, "ADMIN")

u = User.create_admin("Sharika")
print(u.name, u.role)




class Employee:
    company = "Infosys"   # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company   # modifying class variable
        print("Company changed to:", cls.company)


# usage
emp1 = Employee("Ravi", 25000)
emp2 = Employee("Sita", 30000)

Employee.change_company("TCS")
print(emp1.company)
print(emp2.company)

 

class Employee:
    bonus = 3000

    @classmethod
    def set_bonus(cls, amount):
        cls.bonus = amount

Employee.set_bonus(5000)
print(Employee.bonus)



class student:
    college="Anr"
    @classmethod
    def change_college(cls,name):
        cls.college=name
student.change_college("Ntr")
print(student.change_college )







class car:
    def __init__(self):
        var=[1,2,3,4]
        print(var)
var=car()





