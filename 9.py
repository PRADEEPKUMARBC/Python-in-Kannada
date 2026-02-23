# While Loops
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The code inside the loop will continue to execute as long as the condition is true.

is_temprature_high = False
temp = 30
while is_temprature_high:
    print("The Temprature is high")
    temp = temp + 1
    if temp < 40 :
        is_temprature_high = False
print("The Temprature is normal")

is_student = True
Student = 0
while is_student:
    print(f"The student is studying {Student}")
    Student = Student + 1
    if Student % 2 == 0:
        continue
    if Student > 10:    
        break
    

i = 0
while i <= 10:
    print("Pradeep "*i)
    i = i + 1

i = 0
while i <= 10:
    y = 0
    while y <= i:
        print(f"Yes it is correct {i}")
        y = y + 1
    i = i + 1

password = "Pradeep@2006"
trials = 1
while trials <= 3:
    input_password = input(f"Enter a password it is Trai {trials} : ")
    trials = trials + 1
    if input_password == password:
        print("password is correct")
        print("congrats you have entered the correct password")
        break
    else:
        print("password id incorrect")


# home work
# 1 write a program to print the 1 to 10 numbers using while loop
i = 1
while i < 11:
    print(i)
    i = i + 1

# 2 write a program that prints all odd numbers from 1 to 20 using while loop
i = 0
while i <= 21:
    if i % 2 != 0:
        print(i)
    i = i + 1
    
# 3 write a program that prints from 10 to 1 usint the while loop after prints the 'Happy New Year'
i = 10
while i > 0:
    print(i)
    print("Happy New Year")
    i = i - 1


# Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."
seats_available = 8
while seats_available <= 8 and seats_available > 0:
    seat_wanted = input("Do you want to seat a book (yes/no) : ".lower())
    
    if seat_wanted == "yes":
        print("Your seat is booked")
        print(f"Seats Available : {seats_available}")
        seats_available = seats_available - 1
        print("if you want to book another seat please enter yes or no")
        seat_wanted = input("Do you want to seat a book (yes/no) : ".lower())
        if seat_wanted == "yes":
            print("Your seat is booked")
            print(f"Seats Available : {seats_available}")
            seats_available = seats_available - 1
        else:
                print("Thank you for visiting us")
                break
        
    elif seat_wanted == "no":
        print("Thank you for visiting us")
        break
    else:
        print("Invalid input please enter yes or no")
        break