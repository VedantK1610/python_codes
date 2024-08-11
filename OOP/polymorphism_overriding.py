class A:
    def show(self):
        print("IN a")
class B(A):
    def show(self):
        print("In B")
x=B()
x.show()

