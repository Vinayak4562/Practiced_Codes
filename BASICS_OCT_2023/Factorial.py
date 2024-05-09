# num  = int(input("Enter the number: "))
# a = 1
# for i in range(1,num):

#     a = (i+1)*a
# print(a)

# Factorial using Functions
def fact(n):
    a = 1
    for i in range(1,n):
        a = a*(i+1)
    return a
    
n = int(input("Enter the number: "))
b = fact(n)
print(b)
