# Fibonacci 
# feb = int(input("Enter the number: "))
# a = 0
# b = 1
# if feb == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,feb):
#         c = a+b
#         a = b
#         b = c
#         print(c)

# feb = int(input("Enter the number: "))
# l1 = []
# a = 0
# b = 1
# if feb == 1:
#     l1.append(a)
# else:
#     l1.append(a)
#     l1.append(b)
#     for i in range(2,feb):
#         c = a+b
#         a = b
#         b = c
#         l1.append(c)

# print(l1)

 
# # Function for nth fibonacci number
# def fun(n):
#     l1 = []
#     a=0
#     b=1
#     if n < 0:
#        print("Invalid number") 
#     elif n == 0:
#         l1.append(a)
#     elif n == 1:
#         l1.append(b)
#     else:
#         l1.append(a)
#         l1.append(b)
        
#         for i in range(2,n):
#             c= a+b
#             a = b
#             b = c            
#             l1.append(b)
#     return(l1)
    
# n = int(input("Enter the number: "))
# print(fun(n))

# PRO LEVEL

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


n = int(input("Enter the number: "))
result = fibonacci(n)
print(result)