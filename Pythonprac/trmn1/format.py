def greeting(name):
    print(f"Hello how are you {name}")

def greetingdictionary(name,**args):
    print(f"Name is {name}")
    print(f"Age is {args["age"]}")
    print(f"City is {args["city"]}")

greeting("Abhi")
greeting("Shikha")
greetingdictionary("Rahul",age=28,city="Amritsar")
