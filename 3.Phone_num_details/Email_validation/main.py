# a-z small letter wscube@gmail.com
# 0-9 digits and . _ have tobe one 
# @ one time
#  . is in sec and third position
import re
email_condition= "^[a-z]+[\._]?[a-z 0-9]+[@]\W[.]\W{2,3}$"
user_email= input ("Enter your Email: ")

if re.search(email_condition, user_email):
    print(" Right Email")
else:
    print(" Wrong Email")

# Not working Properly