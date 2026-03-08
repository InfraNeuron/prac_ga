class Person:
    def __init__(self,name):
        self.name=name

    def printname(self):
        print("Name is", self.name)



p1=Person("Abhishek")
p2=Person("Bob")

p1.printname()