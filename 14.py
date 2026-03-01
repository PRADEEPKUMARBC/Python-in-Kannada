# Object oriented programming

# Example 1
class Human: #class
    def __init__(self, name):
        self.name = name # attribute

    def walk(self):  # Method
        print(f"{self.name} is walking")

chandan = Human("chandan") #Object
darshan = Human("darshan") 

darshan.walk()

# Example 2
class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def samsung(self):
        print(f"The phone brand is {self.brand} and the price is {self.price} ")

oppo = mobile("2026", "3000")
galaxy = mobile("2036", "4000")

oppo.samsung()

# Example 3
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"the name of the student is {self.name} and the marks is {self.marks} ")

Student1 = Student("Pradeep", "95")
Student2 = Student("Beeresh", "96")

Student1.display_info()
Student2.display_info()

# Syntax 
class className:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        