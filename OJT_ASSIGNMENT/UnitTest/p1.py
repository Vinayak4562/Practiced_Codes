# l = [1,2,3,4,5]
# print(l)
# l.append(11)
# print(l)

# t = (1,2,3,4,5)
# print(t)
# # t.append(11)
# print(t)

"""List comprehensions:
List comprehensions are a concise way to create lists in 
various programming languages, such as Python. They provide a more readable 
and compact syntax for creating lists by applying an expression to each 
item in an existing iterable (like a list or a range) and optionally 
filtering the items based on a condition.

In Python, a basic list comprehension looks like this:

new_list = [expression for item in iterable if condition]
"""

# original_list = [1, 2, 3, 4, 5, 6]
# squared_evens = [x**2 for x in original_list if x % 2 == 0]
# print("original_list: ", original_list)
# print("Even Num squares List: ",squared_evens)  # Output: [4, 16, 36]

"""In Python, a lambda function, also known as an anonymous function 
or a lambda expression, is a small, unnamed function defined 
using the lambda keyword. Lambda functions are typically used for short, 
simple operations that can be defined in a single line of code. 
They are a way to create functions on the fly without giving them a 
formal name.

The basic syntax of a lambda function is as follows:
lambda arguments: expression """

# data = [(1, 5), (3, 2), (2, 8), (4, 1)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # Output: [(4, 1), (3, 2), (1, 5), (2, 8)]

"""In this example, the lambda function lambda x: x[1] extracts the second element (index 1) from each tuple for sorting.

While lambda functions are useful for simple tasks, 
they are limited in their capabilities compared to regular named functions 
defined with def. Lambda functions are best suited for concise operations 
and not for complex or lengthy functions."""

# -------------------------------------------------------
# # FILE HANDELING:
# # -------------------------------------------------------

# fp = open("D:\\CODES\\OJT_ASSIGNMENT\\UnitTest\\my_file.txt")
# Data = fp.read()
# # print(Data)

# lines = Data.split("\n")
# # print(lines)
# for i in lines:
#     # print(i)   
#     words = i.split(" ")
#     # print(words)
#     for i in words:
#             print(i)

# fp.close()

# ----------------------------------------------------------

# # ______________________________
# # MURGING DICTIONARY:
# # ----------------------------
# dict1 = {1:"apple", 2:"Banana", 3:"Mango"}
# dict2 = {4:"rose", 5:"lilly"}
# print("first dict",dict1)
# print("second dict",dict2)

# # dict1.update(dict2)
# # print("Updated Dict",dict1)

# dict3 = {**dict1,**dict2}
# print("dict3",dict3)


arr = [1,2,3,2,4,3,5,6,7,5,2,4,3]
# arr2 = set(arr)
# print(arr2)

# arr3 = []
# for i in arr:
#     if (i not in arr3):
#         arr3.append(i)
# print(arr3)

# remv = lambda arr:set(arr)
# print(remv(arr))

# dict1 = {"name":["vinayak","pramod","vinayak","pramod"],
#          "nick":["vinz","prom","vinz","prom"]}
# dict2 = {}
# for key,value in dict1.items():
#     dict2[key] = set(value)
# print(dict2)

# set1 = {1,2,3,4,5}
# set2 = {5,4,3,8,7}
# dup_ele = set1.symmetric_difference(set2)
# print(dup_ele)

# ________________________________________________________
