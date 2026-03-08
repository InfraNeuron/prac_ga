class Fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def greeting(self):
        return "Hi "+self.name
    
    def showsentence(self):
        print(self.greeting() , "You are welcome here and color of fruit is",self.color)

f1=Fruits("Abhishek","Yellow")
f1.showsentence()