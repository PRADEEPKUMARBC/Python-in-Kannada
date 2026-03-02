class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is walking")

Names = Human("Pradeep", 20)
Names2 = Human("Panther", 21)

Names.run()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My Name is {self.name} and I am {self.age} years old.")

person1 = Person("Arjun", 22)
person1.introduce()
