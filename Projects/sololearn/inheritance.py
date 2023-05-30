class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")
billy = Cat("Billy", "white")
fido = Dog("Fido", "brown"):
print(fido.color)
fido.bark()
print(billy.name)
billy.purr()