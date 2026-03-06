# Four Pillers of Object Oriented Programming (oops)
# 1. Abstraction
# 2. Polymorphism
# 3. Inheritence
# 4. Encapsulation

# 1. Abstraction
class Car:
    def start_engine(self):
        print("Engine Started")
    
    def accelerate(self):
        print("Car Accelerating")

    def brake(self):
        print("Car Stopping")

car = Car()
car.start_engine()
car.accelerate()
car.brake()

# 2. Encapsulation
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New Balance : {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount} . New Balance: {self.__balance}")
        else:
            print("Insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.deposit(300)
# print(atm.__balance)
atm.check_balance()


# small and simple project using abstraction and encapsulation

class Database:
    def __init__(self):
        self.storage = {} # Public
        # self._storage = {} # Protected
        # self.__storage = {} # Private

    def write(self, key, value):
        self.storage[key] = value

    def read(self, key):
        if key in self.storage:
            print(self.storage)
        else:
            print("DB item is not available")

db = Database()
db.write("Subscribers", "EIK")
db.read("Subscribers")
