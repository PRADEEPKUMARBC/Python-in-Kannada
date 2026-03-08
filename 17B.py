# Inheritance and Polymorphism

# 1. Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(slef):
        print("Animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

acments = Dog()
acments.sleep()
acments.eat()

# Polymorphism
class Dog:
    def sound(self):
        print("Bark")
    
class Cat:
    def sound(self):
        print("meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# Inheritance 

class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} is Logged In")
    
class Admin(User):
    def delete_user(self):
        print("Admin deleted the user ")

s = Admin("Pradeep")
s.login()
s.delete_user()

class Family:
    def __init__(self, surname):
        self.surname = surname
    
class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name
        print(f"Surname is {self.surname}  and name is {self.name}")

# class GChild(Family):

child = Child("Chatrad", "Pradeep")


# Polymorphism
class Animal:
    def make_sound(self):
    # def __init__(self, name, sound):
    #     self.name = name
    #     self.sound = sound
        print("Animal making sound")

    # def hesru(self):
    #     print(f"I am {self.name}")

    # def shabda(self):
    #     print(f"I make sound like this {self.sound} {self.sound}")

class Dog(Animal):
    def make_sound(self):
        print("Bow")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()

# a = Dog("Dog", "Bow")
# a.hesru()
# a.shabda()