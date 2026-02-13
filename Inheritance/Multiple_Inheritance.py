# Multiple parents → one child
class Father:
    def f(self):
        print("Father Method")
class Mother:
    def m(self):
        print("Mother Method")
class child(Father,Mother):
    def c(self):
        print("Child method")
obj=child()
obj.f()
obj.m()
obj.c()


# 
class method:
    def xyz(self):
        print("XYZ")
class solid:
    def abc(self):
        print("ABC")
class coil(method,solid):
    def ghi(self):
        print("GHI")
obj=coil()
obj.xyz()
obj.abc()
obj.ghi()


class ajhf:
    def sksjd(self):
        print("sdsjhd")
class pqoei:
    def pqowe(self):
        print("qoieur")
class qoeiur(ajhf,pqoei):
    def adj(self):
        print("ksjdh")
obj=qoeiur()
obj.sksjd()
obj.pqowe()
obj.adj()