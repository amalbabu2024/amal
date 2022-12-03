class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
            print(self.name,self.age)

class student(person):
    def __init__(self,name,age,year):
     super().__init__(name,age)
     self.academicyear=year
    def output(self):
        print("My name is",self.name,"My age is",self.age,"Year is",self.year)
x=person("mike","25",2022)
x.myfunc()

