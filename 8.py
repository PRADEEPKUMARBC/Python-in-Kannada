# Conditional Statements
gender = input("Enter your gender : ")
age = int(input("Enter your age : "))

if gender == "male":
    if age < 5:
        print("Bus ticket price is free")
    elif age > 5 and age < 18:
        print("Discoumt for children")
    elif age > 60:
        print("Discount for senior citizens")
    else:
        print("Full Price for Bus Ticket")
else :
        print("Bus Ticket Price is free for women without consider of any age")

