# for loop
# syntax for For loop is --> for item in sequence
cities = ["manguluru", "Bengaluru", "Mysuru","davanagere"]
for city in cities:
    print(city)

i = 1
while i <= 10:
    print(i, end="  ")
    i = i + 1
print(" ")
for i in range(1,11):
    print(i, end="  ")

Name = "Pradeepkumarbc"

for index,letter in enumerate(Name):
    print(letter*(index + 1))


Numbers = ["55", "86", "523", "56"]
for index, number in enumerate(Numbers):
    print(f"{number} is the {index}th index")

cities = ["manguluru", "Bengaluru", "Mysuru","davanagere"]
for city in cities:
    if city == "Mysuru":
        break
    print(city)\
    
print(" ")

cities = ["manguluru", "Bengaluru", "Mysuru","davanagere"]
for city in cities:
    if city == "Mysuru":
        continue
    print(city)


# using else with for loop
nums = ["52", "33", "44", "85"]

for number in nums:
    if number == "33":
        continue
    print(number)
else:
    print("All printed")


# Dictionary Items
my_dict = {"Name": "Pradeep" , "Age" : 22, "Height": 5.7}
for key, value in my_dict.items():
    print(key, ":", value)

for i in range(2,11):
    for j in range(1,11):
        print(i, "-", j)

for i in range(-11,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")
        j = j + 1
    i = i + 1
    print(" ")

