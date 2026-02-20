# Dictionaries Operations ,  Methods and Functions
# 1. Create a dictionary

my_dict = {
    "Name": "Pradeep kumar",
    "Age": 30,
    "city": "davanagere",
}
print(my_dict)

# 2. Accessing values
print(my_dict["Name"])
print(my_dict["Age"])
print(type(my_dict))
print(my_dict.get("Name3", "Pradeeppppuuu"))

print("after adding the elememts to the dictionary")
my_dict["Height"] = 5.8
print(my_dict)

print("update the value of the key")
my_dict["Name"] = "Pink Panther"
print(my_dict)

print("Removing the key value pair from the dictionary")
my_dict.pop("Name")
print(my_dict)

print("delete the value of the key")
del my_dict["Age"]
print(my_dict)

# Dictionary methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print("clear the dictionary")
print(my_dict.clear())

Meals = {
    "Day1" : {
        "Breakfast": "Oats",
        "Price1": 50,
        "Calories1": 200,
    },
    "Day2" : {
        "Lunch": "Chicken and Mutton Biryani",
        "Price2": 25,
        "Calories2": 800,
        },
    "Day3" : {
        "Breakfast": "Oats",
        "Price3": 500,
        "Calories3": 200,
    },
    }

price_values = [Meals["Day1"]["Price1"], Meals["Day2"]["Price2"], Meals["Day3"]["Price3"]]
print(f"before sorting the price is : {price_values}",price_values)

before_sorting = 0
for i in range(len(price_values)):
    for j in range(i + 1, len(price_values)):
        if price_values[i] > price_values[j]:
            before_sorting = price_values[i]
            price_values[i] = price_values[j]
            price_values[j] = before_sorting

print(f"after sorting the price is : {price_values}",price_values)
# print(f"Price of the Breakfast and lunch is : {Day1['Price1'] + Day2['Price2']}Kg")
# print(f"Calories of Breakfast and Lunch is : {Day1['Calories1'] + Day2['Calories2']} ")

# # another method is
# total_price = Day1["Calories1"] + Day2["Calories2"]
# print(f"Total price of the calories is : {total_price} rs" )


# How to calculate the Average calories in the Meals dictionary

Number_of_days = len(Meals)

total_calories = Meals["Day1"]["Calories1"] + Meals["Day2"]["Calories2"]
Average_calories = total_calories / Number_of_days
print(f"Average calories in the meals is : {Average_calories} calories")

# How to sort by the price of the meals in the Meals dictionary
