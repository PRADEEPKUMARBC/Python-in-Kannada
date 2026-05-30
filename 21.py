# Errors and exception Handling

a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError: # error occurs
    print("An error occurred:")
else: # no error occurs
    print("The division was successful.")
finally:
    print("the block is always executed")

try:
    boy = input("who do you want to marry ? -- ")
    if boy.lower() != "pradeep":
        raise Exception("you only marry Pradeep") # we can possible to raise the exception
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Congratulations on your marriage!")



# Home Work
try:
    age = int(input("Enter your age : "))
    if age >= 0:
        years_left = 100 - age
        print(f"You have {years_left} years left until you turn 100.")
    else:
        print("Age cannot be negative.")
except ValueError:
    print("Invalid input. Please enter a valid age.")
else:
    print("There is no error in the code.")
finally:
    print("Thank you for using the age calculator!")

a = int(input("Enter a number A :"))
b = int(input("Enter a number B: "))

try:
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
else:
    print("The division was successful.")
finally:
    print("Thank you for using the division calculator!")    


# | Mode | Meaning                  |
# | ---- | ------------------------ |
# | r    | Read                     |
# | w    | Write (overwrite)        |
# | a    | Append                   |
# | r+   | Read + Write             |
# | w+   | Write + Read (overwrite) |
# | a+   | Append + Read            |
