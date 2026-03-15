class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f" The brand is {self.brand} and price is {self.price}")

m1 = Mobile("Oppo", "12000")
m2 = Mobile("vivo", "13000")
m1.display()
m2.display()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display_info(self):
        print(f"The student name is {self.name} and student marks is {self.marks}")

s1 = Student("Pradeep", 95)
s2 = Student("Panther", 98)
s1.display_info()
s2.display_info()


class Employee:
    def __init__(self, name, designation, salary = "30000"):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print(f"Employee Name is {self.name} and designation is {self.designation} and salary is {self.salary}")

E1 = Employee("Pradeep", "python developer", 120000)
E2 = Employee("Beeresh", "backend developer", )
E3 = Employee("Naveen", "frontend developer", )

E1.display_details()
E2.display_details()
E3.display_details()