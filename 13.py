# Advanced Function Concept
# The method *args
def add(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result
print(add(199,1,11))

#  **kwargs method
def student_info(**details):
    print(type(details))
    for key, value in details.items():
        print(f" {key} : {value}")
student_info(name = "Pradeep" , Age = 22, Height = 5.8)

# Recursion ---> Recursion Occurs when a function calls itself
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


# Nested Functions
def calculate(a,b):
    def add():
        print(a + b)
    def sub():
        print(a - b)
    def mul():
        print(a * b)
    add()
    sub()
    mul()
    
calculate(4,4)

# lambda function --> Write a lambda function that multiple the two numbers
a = int(input("Enter a Number a : "))
b = int(input("Enter a Number b : "))
my_list = [ a * b for i in range(a,b) ]
print(my_list)

# Recursion Number --> Write a Recursive function that calculates the sum of first n numbers.
n = int(input("Enter the n number : "))
def sum_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_num(n - 1)

print(sum_num(n))

def average(*number):
    for num in number:
        result = sum((number))/len(number)
    return result

print(average(5,5))