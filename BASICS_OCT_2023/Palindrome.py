# n = input("Enter the number")
# rev = n[::-1]
# print(rev)
# if n == rev:
#     print(f"{n} is palindrome")
# else:
#     print(f"{n} is not a palindrome")


# def pal(s):
#     Rev_str = s[::-1]
#     if s == Rev_str:
#         return f"{Rev_str} is palindrome"
#     else:
#         return f"{Rev_str} is not a palindrome"

# s = input("Enter the string: ")
# print(pal(s))


# str = input("Enter the string: ")
# rev_str = ""
# for i in str:
#     rev_str = i + rev_str

# if str == rev_str:
   
#     print(f"{rev_str} is palindrome") 
# else:
#     print(f"{rev_str} is not a palindrome")

def pal(str):
    rev_str = ""
    for i in str:
        rev_str = i + rev_str
    if str == rev_str:
        return f"{rev_str} is palindrome"
    else:
        return f"{rev_str} is not a palindrome"
    
str = input("Enter the string: ")
print(pal(str)) 