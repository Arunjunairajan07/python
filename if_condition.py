 # password 
 
# password="arunjunai"
# email=input("enter the email")
# security=input("Enter the password: ")
# if password == security:
#     print("you password is correct")
# else:
#     print("your password is incorrect")


#elif
# number=int(input("Enthe number value: "))
# if number>0:
#     print("this number is positive")
# elif number<0:
#     print("this number is negative")
# elif number==0:
#     print("this number is zero")



# arjunai -> false
# arjunai123 -> true
# arjunai 124 -> false

# password=input("Enter the password: ")
# if password.isalpha():
#     print("please enter some numbers")
# elif password.isdigit():
#     print("please enter some alphas")
# else:
#     print("Correct")

# if password.isalnum():
#     print("Correct")
# else:
#     print("Wrong")

#modules

def num(number):
    if number>0:
        print("this number is positive")
    elif number<0:
        print("this number is negative")
    elif number==0:
        print("this number is zero")
print(num(5))
#palindrome

# a = input("Enter the value: ")
# b = a[::-1]
# print(a)
# if a == b:
#     print("Its is palindrome")
# else:
#     print("Its not a palindrome")

# a="madam"
# b=a[::-1]
# if a == b:
#     print("palindrome")
# else:
#     print("not palindrome")
    
#swap two number

# a = input("Enter the value A: ")
# b = input("Enter the value B: ")
# c=a
# a=b
# b=c
# print("swap the number a: ",a)
# print("swap the number b: ",b)

#vowels,consensts,digits

str="india is my country in 2024"
vowels=["a","e","i","o","u"]
num=[0,1,2,3,4,5,6,7,8,9]
count=0
con=0
for i in str:
    for j in vowels:
        if i==j:
            count=count+1
print("vowels is: ",count)  
n=len(str)
d=n-count
print("constents is: ",d)

#normal pattern

# for i in range(1,5):
#     for j in range(0,4):
#         print("*",end=" ")
#     print(" ")
    
# patter1

n=0
for i in range(0,6):
    for j in range(0,n):
        print("*",end=" ")
    print(" ")
    n=n+1

# # patter2

# n=5
# for i in range(0,5):
#     for j in range(0,n):
#         print("*",end=" ")
#     print(" ")
#     n=n-1
    
#max and min
# num=["5","6","7","2","9"]
# num.sort()
# val=int(input("Enter the mini=0 or Max=1 values: "))
# if val==0:
#     print(num[0])
# elif val==1:
#     print(num[4])
# else:
#     print("not founder")

#swap three number

# a = input("Enter the value A: ")
# b = input("Enter the value B: ")
# c = input("Enter the value C: ")
# d=c
# c=b
# b=a
# a=d
# print("swap the number a: ",a)
# print("swap the number b: ",b)
# print("swap the number c: ",c)

num=31
n=0
for i in range(2,num):
    if num%i==0:
        n=1
        break
if n==0:
    print(num,"its prime")
else:
    print (num,"its not prime")
    
    
num=28
n=0
for i in range(1,num):
    if num%i==0:
        n=n+i
if n==num:
    print("its perfect squqre")
else:
    print("its not perfect square")
print(n)

n=5
fac=1
for i in range(1,n+1):
    fac= fac*i
print(fac)
    
# length=len (str((376)))
# n1=376**2
# n2=10**length
# print(n1%n2)
# print(n1)
# print(n2)

# num=371
# n1=n2=0
# length=len(str(num))
# for i in range(length):
#     n2=int(num%10)
#     num=num/10
#     n1 =n1+n2**length
# print(n1)

# a=b=0
# num=112
# length =len(str(num))
# for i in range(length):
#     a=num%10
#     num=num//10
#     b=a+b
# print(b)
# if num%b==0:
#     print("its true")
# else:
#     print("its false")
    
list1=[34,67,12,110,31]
mac=list1[0]
mac1=list1[0]
for i in list1:
    if mac < i:
        mac=i
    if mac1 > i:
        mac1 =i
print(mac)
print(mac1)

n=0
lis=[12,45,78,90,23,43,51]
for i in lis:
    n=n+i
print(n)

def reversearray(arr):
    n=len(arr)
    temp=[0]*n
    for i in range(n):
        temp[i]=arr[n-i-1]
    for i in range (n):
        arr[i]=temp[i]
if __name__=="__main__":
    arr=[1,4,3,2,6,5]
    reversearray(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")        
arr1=[9,8,7,6,5,4]
print(arr1[::-1])

import random
resp=["hello","welcome","thank u"]
# input("enter the number: ")
print(random.choice(resp))


# error handling
try:
    a=int(input("enter the number: "))
    b=int(input("enter the number: "))
    ans=a+b
    print(ans)

except Exception:
    print("hello")
finally :
    print("hoops")