#assign the varaiable

Name="Anand"
Days= 15
Years= 2021
print("Dear" +" "+ str( Name))
print("you have" +" "+ str (Days) + "days of leave balance for this year" + str (Years))

# get the user details

# User_name=input("what is your name :")
# User_Email=input("enter the emila_id :")
# User_ph=input("enter the phone number :")
# print("my name is :" + User_name)
# print("my email_id :"+ User_Email)
# print("my number is : 91"+ User_ph)

#using in import math

import math
num=2
n=0
print(math.log2(num))
print(math.cos(n))
print(math.e)

#addition program

# arun= int(input("enter the A values :"))
# bala= int(input("enter the B values :"))
# Adds= int(arun) + int(bala)
# print("the answer is" + str(Adds))

prime=[]
for i in range(2,11):
    n=0
    for j in range(2,i):
        if i%j==0:
            n=1
            break
    if n==0:
        prime.append(i)
print(prime)

n=5      
for i in range(1,6):
    for j in range(0,n):
        print("_",end=" ")
        print("*",end=" ")
        n=n-1
    print(" ")
    
# from getpass import getpass
# name =input("Enter the Name: ")
# password = getpass("Enter the password: ")
# print(name)
# print(password)

n=0
num=1200
while(num>0):
    num=num//10
    n=n+1
print(n)

# s= input("Enter the values: ")
# result = ""
# i = 0
# while i < len(s):
#     count = 0
#     for j in range(i , len(s)):
#         if s[i] == s[j]:
#             count += 1
#         else:
#             break
#     result += s[i] + str(count)
#     i += count  
# print("Output:", result)
arr=[2,8,11,7,15]
for i in arr:
    for j in arr:
        if i+j==9:
            print(i,j)

# count =0         
# num= input("Enter the value: ")
# for i in range(0,len(num)):
#     count +=int(num)&1
#     num=int(num)>>1
# print(count)

n="aabcbba"
list=[]
list1=[]
for i in n:
    list.append(i)
print(list)
i=0
count=0
while i < len(n):
    for k in list:
        if list[i]!=k:
            list1.append(k)
        else:
            continue
count=count+1  
i=count          
print(list1)          
