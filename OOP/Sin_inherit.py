class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printValue(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
cr=Student(2,38,"anu",22)
cr.printValue()
cr.print()