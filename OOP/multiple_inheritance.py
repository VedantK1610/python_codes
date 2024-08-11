class Father:
    def __init__(self, Fname):
        self.Fname = Fname


class Mother:
    def __init__(self, Mname):
        self.Mname = Mname


class child(Father, Mother):
    def __init__(self, Fname, Mname, Cname):
        self.Cname = Cname
        Father.__init__(self,Fname)
        Mother.__init__(self,Mname)
        # super().__init__(Fname)
        # super(Father, self).__init__(Mname)

    def display(self):
        print(self.Cname, self.Fname, self.Mname)


c = child("F", "M", "C")
c.display()