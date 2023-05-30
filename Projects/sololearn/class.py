class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
print(felix.color)

class Dog:
    legs = 4
    def __init__(self,name,color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi from "+self.name)
s1 = Student("Amy")
s1.sayHi()

class Rectangle:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour
rect = Rectangle(7,8,"red")
print(rect.colour)
