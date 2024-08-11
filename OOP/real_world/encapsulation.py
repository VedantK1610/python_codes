'''
1. Abstraction happens during design phase, here we decide what has to be shown.
2. Encapsulation is implementation of thought of abstraction
3. here we are giving access of name and validate to users
4. we don't want user to check the internal working of validate function and address var
5. so we used private methods checkname and checkadd
'''

class Employee:
    def __init__(self,name,add):
        self.name=name
        self.__add=add

    def validate(self):
        if self.__checkname() and self.__checkadd():
            return True
        return False
    def __checkname(self):
        if len(self.name)<5:
            return False
        return True
    def __checkadd(self):
        if len(self.__add)<10:
            return False
        return True

e= Employee('vedant','hello')
print(e.validate())
print(e.name)
# print(e.add) will throw error
# print(e.checkname())   will throw error