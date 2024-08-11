class Person(object):
    clg_name='walchand'

    def __init__(self,name,pid):
        self.name=name
        self.pid=pid
    def display(self):
        print(self.name)
        print(self.pid)

    def isEmployee(self):
        return False
class Employee(Person):
    def __init__(self,name,pid,post):
        super().__init__(name,pid)       #invoking parent constructor
        self.post=post
    def details(self):
        print("hey {} with id no:{} and post:{}".format(self.name,self.pid,self.post))

    def isEmployee(self):
        return True
#driver code
e1=Employee("vk",1610,"manager")
e1.display()
e1.details()
print(e1.isEmployee())
print("clg name:",e1.clg_name)
print(e1.post)
print("\n")
e2=Person("sanket",1203)
e2.display()
print(e2.isEmployee())
print("clg name:",e2.clg_name)   #both objects can access class variable
# print(e2.post)  it will throw Atrribute Error as post is instance variable
#e2.details()   it will throw Atrribute Error