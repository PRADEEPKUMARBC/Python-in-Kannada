# # tuples and sets

a = ("2")
b = 'n'

tol = list(a)
tol.append(b)
print(tuple(tol))

set = {"apple", "banana", "cherry", "date", "elderberry"}
print(set)

s1 = {1, 2, 70, 3, 40}
s2 = {4, 50, 6, 7}

# Union
print(s1 | s2) #union
print(s1 & s2) #intersection
print(s1 - s2) #difference

s1.add(100)
s1.discard(700)
print(s1)

# list are used the square brackets and are ordered and changeable. allow duplicate members.
# tuple are used the round brackets
# set are used the flower brackets 

# Home work 
# Tuple operations
fruits1 = ("apple", "banana", "cherry", "date", "elderberry")
fruits2 = ("fig", "grape", "honeydew", "kiwi", "lemon")

fruits = fruits1 + fruits2 # Concatenation
print(fruits)
print(fruits[1:3]) # Accessing elements


# set operations
set1 = {"apple", "banana", "cherry", "date", "elderberry"}
set2 = {"fig", "grape", "honeydew", "kiwi", "lemon"}
print(set1 | set2) # Union
print(set1 & set2) # Intersection
print(set1 - set2) # Difference
set1.add("mango")
print(set1)
set1.discard("bana") # if the elments is not present in the set it will not give any error
print(set1)