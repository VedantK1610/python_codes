from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def program(self):
        pass

class Laptop(Computer):
    def program(self):
        print("Its running")

class Management(Computer):
    # def program(self):    #it's thrwong error because abstract method is not defined here, uncomment and it will work
    #     print("hey")
    def manage(self):
        print("managing")

class Programmer:
    def work(self,device):
        print("Solving Bugs")
        device.program()


#com1=Computer()       #Can't instantiate abstract class Computer with abstract method program
com2=Laptop()
com2.program()
print("\n")
com3=Programmer()
com3.work(com2)
print("\n")
# com4=Management()


