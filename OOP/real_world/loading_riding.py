'''
1. overloading is Function overloading is the feature when multiple functions have the same name,
   but the number of parameters in the functions varies.
2. In Python, method overloading is not supported because the language uses a concept called "duck typing".
   Duck typing means that the type of an object is determined by its behavior
   (i.e. the methods and properties it has), rather than its class or type. This means that when you
   define a method in Python, you don't have to specify the types of the arguments it takes.
   Instead, the interpreter will look at the behavior of the arguments to determine what to do.
   For example, if you have a method that takes an argument that is a string, and you call the method
   with an integer, the interpreter will try to convert the integer to a string and then call the method.
   This makes the code more flexible and less verbose, but it also means that you can't have multiple
   methods with the same name that take different types of arguments.So, to achieve method overloading,
   you can use default values for arguments and also use variable length arguments.
3. But we can achieve it by using multipledispatch library

4. Method overriding is a concept in inheritance, where a subclass provides a specific implementation
   for a method that is already defined in its parent (base) class. When a method is overridden, the
   version in the subclass takes precedence over the version in the parent class.
'''
from multipledispatch import dispatch

class Shape:
    def __init__(self,l=0,b=0):
        self.l=l
        self.b=b

    @dispatch(int)
    def calculate(self,l):
        area=l*l
        return area
    @dispatch(int,int)
    def calculate(self,l,b):
        area=l*b
        return area

#method overrriding
class Triangle(Shape):
    def __init__(self,l,b):
        super.__init__(l,b)

    def calculate(l,b):
        area=0.5*l*b
        return area

s=Shape()
# print(s.calculate(3)) throw error before dispatch
print(s.calculate(3,5))
print(s.calculate(3)) #after dispatch it won't throw error

s2=Triangle
print("\n")
print(s2.calculate(3,5))