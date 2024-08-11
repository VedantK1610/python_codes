'''
are those members of the class that cannot be accessed outside the class but can be accessed
from within the class and its subclasses.


'''



class Base:
    def __init__(self):
        self._a=2

class new:
    def trial(self):
        print(self._a)
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Base Class:",self._a)

        self._a=3
        print("calling modified value:",self._a)

d=Derived()
print("\n")
b=Base()
print(b._a)
print("\n")
print(d._a)

n=new()
# n.trial() it will throw error
