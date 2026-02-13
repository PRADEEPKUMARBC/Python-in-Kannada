# # Concatenation
# Name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# print("My Name is " + Name + " and My age is " + str(age))

# # # repitation
# print("Hello " * 5)

# #String Methods
# Name = "Pradeep Kumar"
# print(Name.upper())
# print(Name.lower())
# print(Name.strip())
# print(Name.lstrip())
# print(Name.rstrip())
# print(Name.replace("Pradeep", "Kumar"))
# print(Name.split())
# print(Name.find("Kumar"))
# print(Name.islower())
# print(Name.isupper())
# print(Name.startswith("P"))
# print(Name.endswith("r"))


# # Slicing Strings
# # Sequence[start:stop:step]

# Name = "Pradeep Kumar"
# print(Name[0:14])
# print(Name[0:14:2])

# #Reverse a String
# print(Name[::-1])

# # array
# #      0  1  2  3  4 
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Syntax : array[start:stop:step]

# print(arr[0:5])
# print(arr[:2])
# print(arr[2:])
# print(arr[::3])
# print(arr[:-1]) # reverse array
# print(arr[::-1])
# print(arr[::-2])
# print(arr[-1::])
# # print(arr[start:stop:step])


# nums = [1, 2, 3, 4, 5]
# copy_nums = nums[:]
# print(copy_nums)

# nums = [1, 2, 3, 4, 5]
# k = 2
# rotated = nums[-k:] + nums[:-k]
# print(rotated)

# nums = [1, 2, 3, 4, 5]
# print(nums[1:-1])


# # Pattern        | Use
# # ---------------|--------------------------------------
# # [:]            | Copy entire sequence
# # [::-1]         | Reverse sequence
# # [::2]          | Every 2nd element
# # [1::2]         | Every 2nd element (starting from index 1)
# # [:k]           | First k elements
# # [k:]           | Elements from index k to end
# # [-k:]          | Last k elements
# # [:-k]          | All except last k elements
# # [1:-1]         | Remove first and last element
# # [-1]           | Last element
# # [0]            | First element
# # [::-2]         | Reverse & take every 2nd element
# # [k:k+n]        | Subarray of length n starting at k
# # [::3]          | Every 3rd element
# # [-3:-1]        | 3rd last to 2nd last elements
# # [k:-k]         | Remove first k and last k elements
# # [1:]           | Remove first element
# # [:-1]          | Remove last element
# # [::-k]         | Reverse with step k

# # Pattern              | Use
# # ---------------------|----------------------------------------
# # nums[-k:] + nums[:-k] | Rotate array right by k
# # nums[k:] + nums[:k]   | Rotate array left by k
# # nums[:mid]            | First half
# # nums[mid:]            | Second half
# # nums[a:b] == nums[a:b][::-1] | Check subarray palindrome
# # s[:i] + s[i+1:]       | Remove character at index i

# Escape Sequences
Name = "Pradeep \nKumar"
name = "Pradeep \tKumar"
print(Name)
print(name)