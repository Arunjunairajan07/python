# #sum of n natural number
# num=int(input("Enter the Number is: "))
# c=(num*(num+1))/2
# print("The natural number is: ",c)

# # +ve and -ve number
# num=int(input("Enter the number is: "))
# if num>0:
#     print("its positive number")
# else:
#     print("its negative number")

# # odd and even number
# num=int(input("Enter the number is: "))
# if num%2==0:
#     print("its Even number")
# else:
#     print("its Odd number")
    
# sum of n in range
num=0
for i in range(2,9):
    num=num+i
print(num)

#greatest three number
a=10
b=30
c=20
if a<b and b>c:
    print("b is great than a and c")
elif a>b and b<c:
    print("a is great than b and c")
elif a<b and b<c:
    print("c is great than a and b")
    
#leap and non-leap year
# year=int(input("Enter the year: "))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print("this is leap year")
# else:
#     print("this is not a leap year")
    
#prime number
# def prime(n):
#     flag=0
#     for i in range(2,n):
#         if n<2:
#             flag=1
#         elif n%i==0:
#             flag=1
#             break
#     if flag==1:
#         print("its not the prime number")
#     else:
#         print("its the prime number")
# prime(33)

#prime number with given range
prime=[]
for i in range(2,10+1):
    flag=0
    # if i<2:
    #     continue
    # if i==2:
    #     prime.append(2)
    #     continue
    for x in range(2,i):
        if i%x==0:
            flag=1
            break
    if flag==0:
        prime.append(i)
print(prime)
        
#reverse the number
num="123"
rev=num[::-1]
print(rev)

#palindrom
# num=str(input("Enter the word is: "))
# rev=num[::-1]
# if num==rev:
#     print("its the palindrom")
# else:
#     print("its not the palindrom")
    
#factorial number
# fac=int(input("Enter the factorial number is: "))
# fact=1
# for i in range(1,fac+1):
#     fact=fact*i
# print(fact)

#power of number
print(5**2)
        
#fibonacci series
n1=0
n2=1
num=int(input("Enter the number is: " ))
for i in range(1,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
    
#factor
# n=21
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")
         
#armstrong number
#Explanation : 371 can also be represented as 3^3 + 7^3 + 1^3 therefore it's an Armstrong Number.
# number=371
# num=number
# digit,sum=0,0
# length=len (str(number))
# for i in range(length):
#     digit=int(num%10)
#     num=num/10
#     sum=sum+digit**length
# if sum==number:
#     print("armstrong number")
# else:
#     print("Not a armstrong number")
        
#perfect number
#Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number
num=28
n=0
for i in range(1,num):
    if num%i==0:
        n=n+i    
if n==num:
    print("Its the prefect number")
else:
    print("its not the perfect number")
    
#perfect square
import math
num=4
n=math.sqrt(num)
print(n)
check=n*n
if num==check:
    print("its the perfect square")
else:
    print("its the not perfect square")    

#square table
for i in range(1,11):
    n=i*i
    print(i,"*",i,"=",n)
    
#automorphism number
#Explanation : Number = 5
#Square of number = 25
num=376
lenght=len(str(num))
n1=376**2
n2=10**lenght
if n1%n2==num:
    print("its the automorphism")
else:
    print(print("its not the automorphism"))
print(n1)
print(n1%n2)

#harshad number 
#The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.
number=21
num=number
dig=num%10
num=num//10
har=dig+num
print(har)
if number%har==0:
    print("its the harshad number")
else:
    print("its not the harshad number")
    
# another method of harshad number
# n = 112
# p=n
# l=[]
# sum1=0
# while(n>0):
#     x=n%10
#     l.append(x)
#     n=n//10
# sum1=sum(l)
# if(p%sum1==0):
#     print("Harshad number")
# else:
#     print("Not harshad number")

#Abudant number
#Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.
num=21
sum=1
li=[]
for i in range(2,num):
    if num%i==0:
        li.append(i)
        print(li)
        sum=sum+i
        print(sum)
if sum>num:
    print("its Abundant number")
else:
    print("its not Abundant number")

# #largest element in the list
# a=[23,56,78,45,98]
# mac=a[0]
# for i in a:
#     if mac < i:
#         mac=i
# print(mac)    

#smallest element in the list
# a=[23,56,78,45,98]
# mac=a[0]
# for i in a:
#     if mac > i:
#         mac=i
# print("its the smallest number in the list: ",mac) 

#calculate the sum of the list
a=[1,2,3,4,5]
sum=0
for i in a:
    sum=sum+i
print(sum)

#find the smallest and largest number element in the list
a=[23,56,78,45,98]
mac=a[0]
mac1=a[0]
for i in a:
    if mac > i:
        mac=i
    if mac1 < i:
        mac1=i
print("its the smallest number: ",mac)
print("its the largest number: ",mac1)

