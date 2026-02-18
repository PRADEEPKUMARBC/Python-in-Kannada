# Comparison Operaters 
a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Arithmatic Operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b) # Floor Division = remove the decimal numbers

# Logical Operators
a = 10
b = 20
print(a > 5 and b > 15) # True and True = True
print(a > 15 and b > 15) # False and True = False
print(a > 5 or b > 15) # True or True = True
print(not(a > 8))

# Membership operator
Name = "Pradeep Kumar"
print("Pradeep" in Name)
print("  " not in Name)

# Bitwise Operators
a = 3 # 011
b = 5 # 101
print(a & b) # Bitwise AND
print(a | b) # Bitwise OR
print(a ^ b) # Bitwise XOR
print(~a)    # Bitwise NOT
print(a << 1) # Left Shift
print(a >> 1) # Right Shift

#  H W
# Logical operaters
a = int(input("Enter your num1 : "))
b = int(input("Enter your num2 : "))
print(a > 10 and b > 10)
print(a < 5 or b < 5)
print(not(a > b))

#Comparision Operators
age = int(input("Enter your age : "))
if age >= 18:
    print("your in adult")
else:
    print("youe are a minor")

Whatever_you_type = input("Enter something : ")
print("a" in Whatever_you_type)
print(" " in Whatever_you_type)