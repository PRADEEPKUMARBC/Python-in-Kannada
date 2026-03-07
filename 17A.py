# Home Work
# Encapsulation

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited amount is {amount}. and the balance is {self.__balance}")
    
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Withdraw amount is {amount} and the balnce is {self.__balance}")

ba = BankAccount(35441564,5800)
ba.deposit(1000)
ba.withdraw(1000)

#  Abstraction --> Design a phone class with two methods to call_contact and take_picture. Abstract away any internal processing and focus on creating a user-friendly interface 


from abc import ABC, abstractmethod

class Phone(ABC):

    @abstractmethod
    def call_contact(self, contact):
        pass

    @abstractmethod
    def take_picture(self):
        pass

    #abc --> Abstract base class method