# Functions
def greet():
    print("Hi Hello Good Morning")
greet()

def marriage(boy, girl="Sanjana"): # Keyword Arguments
    print(f"Boy is {boy  }")
    print(f"Girl is {girl}")
    print(f"{boy} is married {girl}")
marriage("Sanjay")

# marriage("Pradeep", "deepa")  # Positional Arguments


def muggi(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")

muggi(5)


def function(num):
    return (num)*3
a = function(2)
b = 10
c = a + b
print(c)

# Local Variables and Global Variables
def func():
    x = "Pradeep" # Positional Arguments
    print("Hello World")
    print(y)

y = "Deepa" # Keyword Arguments
print(y)