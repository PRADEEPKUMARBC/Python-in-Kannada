# Getters, setters, overloadin, overriding

# Getter -->  Getter is a method used to get (read) private data from a class. 
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    

s = Student("Pradeep",44)
print(s.get_name())
print(s.get_age())

# Setter --> Setter is a method used to modify (set/update) private data safely.

class Student:
    def __init__(self, name):
        self.__name = name

    def user(self):
        print(f"My Name is {self.name}")

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

s = Student("Pradeep")
s.set_name("kumar")
print(s.get_name())

