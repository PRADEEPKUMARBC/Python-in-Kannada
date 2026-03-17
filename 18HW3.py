# Getters and Setters
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance < 0:
            print("The balance can not be negative")
            return
        self.__balance = new_balance

ba = BankAccount(100)
ba.set_balance(30)

# OverLoading  --> 
class calculator:
    def multiply(self, a, b, c=0):
        return a * b * c

m = calculator()
print(m.multiply(2, 3))


# Over riding
class Shape:
    def draw(self):
        print("Drawing the shape")

class Circle(Shape):
    def draw(self):
        super().draw()
        print("Drawing the circle")

s = Circle()
print(s.draw())

# Abstract
from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Manager's salary is calculated")