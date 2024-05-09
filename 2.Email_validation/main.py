email = input("Enter your Email: ")
k,j,d = 0,0,0
if len(email)>= 6: # Wrong Email 1
    if email[0].isalpha():# Wrong Email 2
        if ("@" in email) and (email.count("@") == 1): # Wrong Email 3
            # XOR 0^0= 0 1^1=0 O/P= true if any one I/P should be true
            if (email[-4] == ".") ^ (email[-3] == "."): # Wrong Email 4
                for i in email:
                    if i == i.isspace(): # Wrong Email 5
                        k = 1
                    elif i.isalpha():
                        if i == i.upper(): # Wrong Email 5
                            j = 1
                    elif i.isdigit(): # Wrong Email 5
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else: # Wrong Email 5
                            d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else: 
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")