class parent:
    def __init__(self,pname):
        self.pname=pname
class son(parent):
    def __init__(self,pname,sname):
        self.sname=sname
class daughter(parent):
    def __init__(self,pname,dname):
        self.dname=dname

    def show(self):
        print("parent name :",self.pname)
        print("son name :",self.sname)
        print("Daughter name:",self.dname)
d=daughter("amala","amal","babu")
d.show()