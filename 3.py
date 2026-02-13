# Input/Output , String Manupulation and comments
boys_name = input("Enter Boys Name : ")
boys_age = int(input("Enter your age : "))
girls_name = input("Enter Girls  name : ")
girls_age = int(input("Enter your age : "))

age_difference = abs(boys_age - girls_age)
print(boys_name + " loves " + girls_name + " and  age_difference is " + str(age_difference)  )
print(f"{boys_name} loves {girls_name}  and age difference is {age_difference}")