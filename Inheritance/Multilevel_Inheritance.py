#  When a class inherits from another class which is already inherited from another class, it is called Multilevel Inheritance.
class Grandfather:
    def own(self):
        print("Grand father owns house")
class father(Grandfather):
    def car(self):
        print("Grandfather ownsa car")
class son(father):
    def bike(self):
        print("Son owns bike")

    def asserts(self):
        print("son njoy family asserts")
obj=son()
obj.own()
obj.car()
obj.bike()
obj.asserts()



# 
class father:
    def father_skill(self):
        print("Father: Driving")
    def father_job(self):
        print("Office work")

class mother:
    def mother_skill(self):
        print("Mother:Cooking")
    def mother_role(self):
            print("Mother :Home maker")

class child(father,mother):
    def child_skill(self):
        print("Child:Coding")
    def child_role(self):
        print("Child:Student")

obj=child()
obj.father_skill()
obj.father_job()
obj.mother_skill()
obj.mother_role()
obj.child_skill()
obj.child_role()
