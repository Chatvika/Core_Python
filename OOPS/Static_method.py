# static method
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))


class Employee:

    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return "Valid Salary"
        else:
            return "Invalid Salary"


# usage
print(Employee.is_valid_salary(25000))
print(Employee.is_valid_salary(-5000))


class Number:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"

print(Number.is_even(10))

class Student:
    college = "Anr"

    @staticmethod
    def change_college(name):
        Student.college = name

Student.change_college("Ntr")
print(Student.college)

  
class car:
    wheels=4

    def __init__(self,brand):
        self.brand=brand
car1=car("Toyota")
car2=car("BMW")
print(car1.wheels)
car.wheels=5
print(car2.wheels)