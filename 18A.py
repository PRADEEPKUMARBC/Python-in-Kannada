# Method Overloading
# Overloading ---> Method overloading is the ability to define the multiple methods with the same name with differnt parameters

class ArithmaticOperation:

    def add(self, a, b, c=5):
        return a + b + c
    
math = ArithmaticOperation()
print(math.add(1, 2))
print(math.add(4, 2, 3))


# Overriding
# Method of overriding allows a child class to provide a specific implementation for a method that is already defined in its parent


class Animal:
    def make_sound(self):
        print("This animal make a sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")
    
animal = Dog()
animal.make_sound()