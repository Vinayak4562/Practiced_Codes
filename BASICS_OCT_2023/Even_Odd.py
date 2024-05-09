# n = int(input("Enter th number: "))

# if n % 2 == 0:
#     print(f"The {n} is Even number")
# else:
#     print(f"The {n} is Odd number")



def Even_Odd(num):
    if num % 2 == 0:
        return f"The {num} is Even number"
    else:
        return f"The {num} is Odd number"


num = int(input("Enter th number: "))
print(Even_Odd(num))


