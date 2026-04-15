# Banking System 

class Account:
    def __init__(self, id, holder_name, balance):
        self.id = id
        self.holder_name = holder_name
        self._balance = balance

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"deposit successfull. Update Balance : {self._balance}" )

    def withdraw(self, amount):
        if self._balance >= amount:          
            self._balance -= amount
            print(f"withdraw successfull. Update Balance : {self._balance}" )
        else:
            print("Funds not available")


class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.04
        interest = self._balance * INTEREST_RATE
        print(f"Interest : {interest}")

class CurrentAccount(Account):
    def withdraw(self, amount):  #Polymorphism
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f" Withdraw Successful. Updated Balance: ")
        else:
            print("Ask is Over Limit")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, type):
        if type == "Savings":
            new_account = SavingsAccount(id, holder_name)
        elif type == 'current':
            new_account = CurrentAccount(id, holder_name)
        self.__accounts[id] = new_account
        print("Account creation successfull")
        return new_account


    def get_account(self, id):
        if id not in self.__accounts:
            print("Accounts are not found")
        else:
            account = self.__accounts[id]
            print(f"ID : {account.id} \n Holder Name : {account.holder_name}")


pbi = Bank("Pradeep Bank of India", "Mysore")

s1 = pbi.create_account("1", "Darshan", "savings")
c1 = pbi.create_account("2", "Virat", "current")
