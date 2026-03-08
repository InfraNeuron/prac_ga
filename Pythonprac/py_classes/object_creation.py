class Demo:
    x=7

n1=Demo()

print(n1.x)

class Person:
    def __init__(self,name,age):
        self.newname=name
        self.age=age

p1=Person("Abhi",34)
print(f"Name of person1 is {p1.newname}")
