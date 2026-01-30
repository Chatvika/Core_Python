class Animal:
    location="Australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Generic animal sound")
class dog(Animal):# this is how inheritance  done in py
    def speak(self):     #we are using speak function of the parent class
        super().speak()
        print("Woof!")
d=dog("jimmy")
d.speak()
print(d.location)
 



class Employee:
    def __init__