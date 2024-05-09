# # In shallow copy Changes made to the nested objects inside the copy will affect the original object and vice versa.

# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# shallow_copy = copy.copy(original_list)

# # Both original_list and shallow_copy share the same nested lists.
# shallow_copy[0][0] = 99
# print("original list:",original_list)  # Output: [[99, 2, 3], [4, 5, 6]]
# -------------------------------------------------------------------------------

# # A deep copy of an object creates a completely independent copy of the original object,
# # including copies of all the objects contained within it. 
# # This means that changes made to the nested objects inside the copy won't affect the original object, and they are entirely separate.

# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# deep_copy = copy.deepcopy(original_list)

# # Modifying the deep copy does not affect the original list.
# deep_copy[0][0] = 99
# print(original_list)  # Output: [[1, 2, 3], [4, 5, 6]]

# # # ____________________________________________________________________________________

# # In summary, a shallow copy creates a new object that shares references to the same nested objects as the original, 
# # while a deep copy creates a new object with entirely independent copies of all nested objects. The choice between using a shallow copy 
# # or a deep copy depends on your specific use case and whether you want changes in the copied object to affect the original or not.

# Shallow Copy, Deep Copy, and Monkey Patching are all concepts in Python related to manipulating or copying objects, 
# but they serve different purposes and have distinct characteristics:

# # 1. Shallow Copy:
# #    - **Purpose**: Create a new object that is a copy of the original object, with references to the same nested objects as the original (i.e., nested objects are not deeply copied).
# #    - **Usage**: When you want a new object that shares some of its internal structure with the original object.
# #    - **Example**: Using `copy.copy()` or `[:]` for lists, or `copy.copy()` for dictionaries.

# # 2. Deep Copy:
# #    - **Purpose**: Create a new object that is a completely independent copy of the original object, including deep copies of all nested objects.
# #    - **Usage**: When you want a new object that is entirely separate from the original, and changes to the copy won't affect the original.
# #    - **Example**: Using `copy.deepcopy()`.

# # 3. Monkey Patching:
# #    - **Purpose**: Dynamically modifying or extending the behavior of existing classes or modules during runtime, typically by adding or modifying methods, attributes, or functions.
# #    - **Usage**: When you need to modify or extend the behavior of a class or module from a third-party library or when you want to change the behavior of built-in Python objects temporarily.
# #    - **Example**: Adding new methods to a class, modifying the behavior of an existing function, or patching the behavior of an external library without modifying its source code.

# # Here's a brief example illustrating each concept:


# # Shallow Copy
# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# print("original list:",original_list)
# shallow_copy = copy.copy(original_list)
# shallow_copy[0][0] = 99 
# print("shallow_copy :",original_list)  # Output: [[99, 2, 3], [4, 5, 6]]

# # Deep Copy
# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# print("original list:",original_list)
# deep_copy = copy.deepcopy(original_list)
# deep_copy[0][0] = 99
# print("deep_copy:",original_list)  # Output: [[1, 2, 3], [4, 5, 6]]

# # Monkey Patching
# class MyClass:
#     def say_hello(self):
#         return "Hello"

# # Monkey patching to modify the behavior of MyClass
# def new_hello(self):
#     return "New Hello"

# MyClass.say_hello = new_hello

# obj = MyClass()
# print(obj.say_hello())  # Output: "New Hello"

# # In summary, shallow copy and deep copy relate to copying objects, 
# # while monkey patching is a technique for modifying the behavior of classes or modules at runtime. 
# # The choice of which to use depends on your specific requirements and the problem you are trying to solve.