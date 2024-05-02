 # password 

password="arunjunai"
email=input("enter the email")
security=input("Enter the password: ")
if password == security:
    print("you password is correct")
else:
    print("your password is incorrect")


#elif

number=int(input("enter the number"))
if number>0:
    print("this number is positive")
elif number<0:
    print("this number is negative")
elif number==0:
    print("this number is zero")


# arjunai -> false
# arjunai123 -> true
# arjunai 124 -> false

password=input("Enter the password: ")
if password.isalpha():
    print("please enter some numbers")
elif password.isdigit():
    print("please enter some alphas")
else:
    print("Correct")

# if password.isalnum():
#     print("Correct")
# else:
#     print("Wrong")