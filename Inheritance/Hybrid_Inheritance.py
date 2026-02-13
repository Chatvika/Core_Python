class person:
    def identity (self):
        print(" I am a person")

    def  basic(self):
        print("Basic details")



class Employee(person):

    def work(self):
        print("Employee works")

    def salary(self):
        print("Gets salary")




class student(person):

   def study(self):
        print("Student studies")

   def exam(self):
        print("Writes exam")


class intern(Employee,student):


    def role(self):
        print("Intern role")

    def duration(self):
        print("Internship duration")





i=intern()
i.identity()
i.basic()
i.work()
i.salary()
i.study()
i.exam()
i.role()
i.duration()

  

