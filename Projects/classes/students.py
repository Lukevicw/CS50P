class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

#By making it a class method, you can call it before the object is instantiated
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
#returns a Student<-(cls) which we know is a name and a house

def main():
    student = Student.get() #After moving the function into the class, it is now called here
    print(student)



if __name__ == "__main__":
    main()
