# multiple child  class inherit from the same parent class
class Bank:
    def rules(self):
        print("Bank rules")
    def intrest(self):
        print("bank give intrest")
class savingsaccount(Bank):
    def savings(self):
        print("Savings account")
    def limit(self):
        print("Savings account")
class currentaccount(Bank):
    def current(self):
        print("Current account")
    def overdraft(self):
        print("Overdraft facility")
o=savingsaccount()
w=currentaccount()

o.rules()
o.intrest()
o.savings()
o.limit()



w.rules()
w.intrest()
w.current()
w.overdraft()
# 
class shape:
    def draw(self):
        print(" Drawing shape")
    def color(self):
        print(" Shape has color")

class rectangle(shape):
    def rect_area(self):
        print("Rectangle area = l * b")

class circle(shape):
    def circle_area(self):
        print("Circle area = π * r * r")

s=rectangle()
b=circle()

s.rect_area()
s.draw()
s.color()

b.draw()
b.color()
b.circle_area()