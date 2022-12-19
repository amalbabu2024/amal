class school:
    def func(self):
        print("This is in school function")
class stu1(school):
    def func1(self):
        print("This is in student 1 function.")
class stu2(school):
    def func2(self):
        print("This is in school 2 function")
class mca(stu1,stu2):
    def func3(self):
        print("This is in mca function.")
o=mca()
o.func()
o.func1()
o.func2()
o.func3()