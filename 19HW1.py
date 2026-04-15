def show_menu():
    print("Simple Banking System : ")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

balance = 0

while(True):
    show_menu()
    choice = int(input("Enter the choice (1 - 4) : "))

    if choice == 1:
        print("Balance is : ", balance)

    elif choice == 2:
        amount = int(input("Enter the amount to deposit : "))
        balance += amount
        print("Deposit Money is " , balance)

    elif choice == 3:
        amount = int(input("Enter the amount to withdraw : "))
        if balance <= amount:
            print("Amount is not sufficient1")
        else : 
            balance -= amount
            print("Withdraw money is ", balance)

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid Try again")

