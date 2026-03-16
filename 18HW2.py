# four pillers of oops examples

# 1. Encapsulation ---> class | object | method
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        print(f"The balance is {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f" The balance amount is {self.__balance}")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient fund")
            return
        self.__balance -= amount
        print(f" withdraw is successful - balance : {self.__balance}")


a = BankAccount(account_number = 123, balance = 1100)
a.check_balance()
a.withdraw(1000)


# Abstraction --> Class Object Method
class Phone:
    def call_contact(self):
        print("contact calls")
    
    def take_picture(self):
        print("Take a picture")

c = Phone()
c.call_contact()
c.take_picture()

# 3. Inheritance --> parent class , child class, object and init in child class not in parent class 
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):
    def __init__(self, name):
        self.name = name

    def ride(self):
        print("The ride with safe")

b = Bike(Vehicle)
b.start()
b.ride()

# 4. Polymorphism  -->  inheritance like parent class and child class
class Shape:
    print("Area Calculated")

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        print(f" The area of the circle is {(22/7) * self.radius * self.radius}")

class rectangle(Shape):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def calc_area(self):
        print(f"Area of rectangle is { self.length * self.breadth * self.height}")

c = circle(2)
c.calc_area()
c = rectangle(2,3,5)
c.calc_area()