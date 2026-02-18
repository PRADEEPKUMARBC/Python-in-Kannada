#  List Operations , Methods , and Functions
items = ["apple", "banana", "cherry", "date", "elderberry"]

print(items.index("apple"))

# Acessing the elemnts
print(items[0]) # first element
print(items[2]) # third element
print(items[-1]) # last element

#  Modifying the list
print(items.pop())
print(items)
print(items.append("fig"))
print(items)
print(items.insert(1,"grape"))
print(items)
print(items.remove("apple"))
print(items)
print(items.clear())
print(items)

# Common Function
print(len(items))
print(sorted(items))
print(items.count("apple"))
print(items.reverse())
print(items )

M = [[1 , 2] , [3 , 4]]
#     0    1    0   1
#        0         1
print(M)