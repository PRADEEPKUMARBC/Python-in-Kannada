# write method
file = open("file.txt", "w")
content = file.write("Hello, this is a sample text file.\nThis file is used for demonstrating file handling in Python.")
print(content)
file.close()

# Read method
file = open("file.txt", "r")
content = file.readlines()
print(content)
file.close()

# write method
file = open("sample.txt", "w")
content = file.write("Appending a new line to the file.")
print(content)
file.close()

# Append method
file = open("sample.txt", "a")
content = file.write("Appending madtaedini")
print(content)
file.close()

try:
    file = open("smaple2.txt", "w")
    file.write("This will raise an error because the file is opened in read mode.")
    file.close()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File operations completed successfully.")
finally:
    print("This block will always execute, regardless of whether an error occurred or not.")



file = open("sample.txt", "r")
file.close()

# Instead of manually opening and closing files, we can use the with statement which ensures that the file is properly closed after its suite finishes, even if an exception is raised.

with open("sample.txt", "r") as file:

    friends = []

# Homework
for i in range(3):
    name = input(f"Enter your friend's name {i+1}: ")
    friends.append(name)

with open("dosta.txt", "w") as file:
    for friend in friends:
        file.write(friend + "\n")

student_name1 = input("Enter the name of student 1: ")
student_marks1 = int(input("Enter the marks of student 1: "))

with open("marks.txt", "w") as file:
    file.write(f"{student_name1} - {student_marks1}\n")

with open("file.txt", "r") as file:
    content = file.readlines()
    print("total lines in the file: ", len(content))
