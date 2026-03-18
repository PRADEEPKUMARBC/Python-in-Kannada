# Simple calculator

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def show_menu():
    print("$$ Simple Calculator ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

while(True):
    show_menu()
    choice = int(input("Enter your choice (1 - 5) : "))
    if choice in {1,2,3,4}:
        a = int(input("Enter the first number  : "))
        b = int(input("Enter the second number : "))

    if choice == 1:
        print("Result : ", add(a,b))

    elif choice == 2:
        print("Result : ", sub(a,b))

    elif choice == 3:
        print("Result : ", mul(a,b))

    elif choice == 4:
        print("Result : ", div(a,b))

    elif choice == 5:
        print("Quit...")
        break
    else:
        print("Invalid choice. Try again!")