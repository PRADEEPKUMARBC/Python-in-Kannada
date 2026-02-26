l = [44, 448, 4886, 68, 868]
dl = []

for num in l:
    dl.append(num)
    print(dl)

# Looping through Dictionaries
student_marks = {"Anand": 86 ,"Geetha": 56, "Kumar": 55}
# student , marks --> After writting this it is assign like (tuples) in [list] like [("Anand" : "86" , "Geetha" : "56" , "Kumar" : "55")]
for student , marks in student_marks.items():
    print(f"{student} : {marks}")



# For Loops with Range()
students = ["Anand", "geetha", "Kumar"]
marks = [85, 90, 77]

student_marks = {}

# using enumerate()

for index, students in enumerate(students):
    student_marks[students] = marks[index]
print(student_marks)

# using for loop range 
for i in range(len(students)):
    student_marks[students[i]] = marks[i]
print(student_marks)



# List Comprehension
List = [num for num in range(1,11)]
double_list = []

for num in List:
    # double_list.append(num)  for reducing of this code lines -->  using the List comprehension

# for num in List:
    double_list.append(num)
print(double_list)

# Syntax for List Comprehension is new_list = [expression for item in collections if condition]
print(List)

new_List = [num**2 for num in List if num % 2 == 0]
print(new_List)




# Dictionary Comprehension
names = ["Anand", "Geetha", "Kumar"]

d = { name:len(name) for name in names }
print(d)

# Find the Large city
city_population = {
    "Bengaluru" : 84,
    "Mysuru" : 55,
    "Hubballi": 99,
    "Mangaluru": 56
}

lcity = { city:pop for city, pop in city_population.items() if pop > 80}
lc = tuple(lcity)
print(f"The large city is {lc}")


x = input("Enter Any thing : ").split()
l = [ int(num) for num in x ]
print(l)
