'''
Private members are similar to protected members, the difference is that the class members declared private should
neither be accessed outside the class nor by any base class.


'''

class Base:
    def __init__(self):
        self.a="vedant"
        self.__b="kulkarni"  #private var

    def Lname(self):
        print("last name:",self.__b)
class Derived(Base):
    def __init__(self):
        Base.__init__(self)

    def Fname(self):
        print("first name",self.a)
    def Lname(self):
        print("first name",self.__b)

d=Derived()
d.Fname()
#d.Lname() 'Derived' object has no attribute '_Derived__b'

b=Base()
b.Lname()