# 10 star

# for i in range(1,11):
#     print("*")

#changes 

# # guessing game

# import random
# num=random.randint(1,20)
# guess=int(input("guess the number is less than 20: "))
# while num!=guess:
#      if guess>num:
#           print("your guess number is higher")
#      else:
#           print("your guess number is lower")
#           guess=int (input("guess again: "))  
               
# print ("you won")   
 
#  #list

# list_num=[]
# for i in range(1,11):
#     list_num.append(int(i))
# print(list_num)
# for j in list_num:
#     if j%2==0:
#         print("this number are even: ",str(j))
#     else:
#         print("this number is odd: ",str(j))

#number pattern

# for i in range(1,6):
#     for j in range(1,5):
#         print(j,end="")
#     print("")    

#pattern 
# n=1
# for i in range(1,5):
#     for j in range(0,n):
#         print("*",end="") 
#     n+=1
#     print("")    
    
# 15 table
# n=15
# for  i in range(0,11):
#     y=n*i
#     print("15 * "+str(i)+" = "+str(y))
    
# a=[1,2,3,4,5]
# for i in a:
#     a.remove(i)
#     print(a)
    
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# n=5
# for i in range(1,6):
#     if i<=n:
#         print(i,end=" ")
#         x=i         
#     for j in range(0,5):
#         if j<i-1:
#             x=x+((n-1)-j)   
#             print(x,end=" ") 
#     print(" ")
    
# thislist = list(("apple", "banana", "cherry"))
# thislist.remove("apple")
# print(thislist)

# W E L C O M 
# E T O Z O H 
# O C O R P O
# R A T I O N
# a="WELCOMETOZOHOCORPORATION"
# n=1
# for i in range(0,len(a)):
#     if i<=n:
#         print(a[i],end=" ")
#     if n%6==0:
#         print("")
#     n=n+1        
    
# a="hello world"
# print(a[::-1])

# rev=["hello","world","welcome","to","python"]
# i=len(rev)
# while 0<i:
#      i=i-1
#      print(rev[i])
    
# reverse word
list1=[]
a=" The Sky is blue"
b=a[::-1]
print(b)
c=b.split(" ") 
print(c)
for i in range (len(c)):
    d=c[i]
    e=d[::-1]
    print(e,end=" ")
   
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
# n=1
# for i in range(1,6):
#     for j in range(n,6):
#         print(j,end=" ")    
#     print(" ")    
#     n=n+1
    
# 1  
# 1 2  
# 1 2 3
# 1 2 3 4
# n=2
# for i in range(1,5):
#     for j in range(1,n):
#         print(j,end=" ")
#     print(" ")    
#     n=n+1
   
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4
# n=1
# for i in range(1,6):
#     for j in range(n,6):
#         print(j,end=" ")   
#     for k in range(1,n):
#         print(k,end=" ") 
#     print(" ")    
#     n=n+1

# s       
# s i
# s i m
# s i m p
# s i m p l
# s i m p l e 
# s1="Simple"
# for i in range(1,len(s1)+1):
#     for j in range(0,i):
#         print(s1[j],end=" ")
#      print(" ")
  
#  print the negative value index position
# list1=[-1,4,5,-6,7,8]
# for i in list1:
#     if i<0:
#         print(list1.index(i))

# [1,3,3,4,6,6,7] remove the duplicate value and insert the crt values
a={1,3,3,4,6,6,7}
print(a)
b=list(a)
print(b.insert(1,2))
print(b.insert(4,5))
print(b)
      #(or)
a=[1,3,3,4,6,6,7]
print(a.pop(1))
print(a.pop(4))
print(a.insert(1,2))
print(a.insert(4,5))
print(a)

# str=abdefgabde substring the 3 strings length is all string is equal
str="abdefgabde" 
# n=0 
m=4
for i in range(0,3):
    for j in range(i,m):
        print(str[j],end=" ")
    # n=n+1
    m=m+1
    print(" ")
    
# [1,2,3] = [1,3,2],[2,3,1],[2,1,3],[3,2,1],[3,1,2]
# a=[1,2,3]
# for i in range(1,4):
#     if i<0:
#         print("Hello")
# else:
#     print("world")
    
#
# number=int(input("enter the number is: "))
# for i in range(5): 
#     if number==5:
#         print("True")
#         break
#     else:
#         number=int(input("enter the number is: "))
# else:
#     print("your luse the game")

# second largest number
a=[45,67,89,99,10,20]
a.sort(reverse=True)
print(a)
print(a[1])

#football
# teamA=[1,3,56,7]
# teamB=[2,78,34,1]
# n=m=0
# for i in teamA:
#     n=n+i
# for j in teamB:
#     m=m+j
# if n<m:
#     print(m)
# else:
#     print(n)

name=["arun","van","bala","vanakkam","valkai","ravi","venam","vaali"]
for i in range(0,len(name)):
    if "v"==name[i][0]:
        if "a" ==name[i][1]:
            print("va")

# input =[1,2,3,4,5,6,7]
# output=[7,1,6,2,5,3,4]
        
a1=[1,4,7,9,3,0,3,6]
a2=[3,5,7,2,4,0,6,1]
a1.extend(a2)
print(a1)
b= set(a1)
c=list(b)
print(c)

# str =abcdefghijkl
# str = "abcdefghijkl"
# n=0
# m=4
# for i in range(1,4):
#     for j in range(n,m):
#         print(str[j],end=" ")
#     n=n+4
#     m=m+4
#     print(" ")
 
# a
# a b
# a b c
# a b c d
# a b c d e
# a b c d e f
# a b c d e f g
# a b c d e f g h
# a b c d e f g h i
# a b c d e f g h i j  
# a b c d e f g h i j k  
# a b c d e f g h i j k l     

str="abcdefghijkl"
for i in range(1,len(str)+1):
    for j in range(0,i):
        print(str[j],end=" ")
    print(" ")
    
#a
#bc
#def
#ghij
# n=0
# m=1
# str="abcdefghijkl"
# for i in range(1,len(str)+1):
#     for j in range(n,m):
#         print(str[j],end=" ")
#     n=n+1
#     m=m+2
#     print(" ")

# A
# B C
# D E F
# G H I J
# ascii value is a=97 and A=65
n=65
for i in range(4):
    for j in range(i+1):
        print(chr(n),end=" ")
        n+=1
    print(" ")

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15    
# n=1   
# for i in range(1,6):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print(" ")
    
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0   
# n=1
# m=6
# for i in range(1,6):
#     for j in range(0,n):
#         print(j,end=" ")
#     n=n+1
#     print(" ")
# for k in range(1,7):
#     for l in range(0,m):
#         print(l,end=" ")
#     m=m-1
#     print(" ")

# S
# S i
# S i m
# S i m p
# S i m p l
# S i m p l e
# S i m p l
# S i m p
# S i m
# S i
# S
# s1="Simple"
# n= len(s1)
# for i in range(1,len(s1)+1):
#     for j in range(0,i):
#         print(s1[j],end=" ")
#     print(" ")
# for k in range(0,len(s1)):
#     for l in range(0,n-1):
#         print(s1[l],end=" ")
#     n=n-1
#     print(" ")

# * * * * *
# * * * *
# * * *
# *
# * *
# n=6
# for i in range(0,6):
#     if i==3:
#         print("*")
#     for j in range(1,n):
#         print("*",end=" ")
#     n=n-1
#     if n==2:
#         break
#     print(" ")

# ASCII VALUES
# A :capital letter
# r :small letter
# u :small letter
# n :small letter
# J :capital letter
# U :capital letter
# N :capital letter
# a :small letter
# i :small letter
# R :capital letter
# a :small letter
# j :small letter
# a :small letter
# N :capital letter
# @ :Symbol
# 7 :number
# 0 :number
# 9 :number
# 2 :number 
# values = input(print("Enter the name"))
# for i in range(0,len(values)):
#     if ord(values[i])>=65 and ord(values[i])<=90:
#         print(values[i],":capital letter")
#     elif ord(values[i])>=97 and ord(values[i])<=122:
#         print(values[i],":small letter")
#     elif ord(values[i])>=48 and ord(values[i])<=57:
#         print(values[i],":number")
#     else:
#         print(values[i],":Symbol")
 
# hand cricket       
# import random
# n=0
# m=0
# for i in range(0,6):
#         num=int(input(print("enter the score")))
#         n=n+num
# print("human",n)
# for j in range(0,6):
#     ran=random.randint(0,10)     
#     m=m+ran
# print("system",m)   
# if n<m:
#     print("loose")
# else:
#     print("win")

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(1,i):
#         print("*",end=" ")
#     print(" ")

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# for i in range(1,6):
#     for j in range(0,6-i):
#         print("*",end=" ")
#     for k in range(1,6-i):
#         print("*",end=" ")
#     print(" ")
#     for l in range(i):
#         print(" ",end=" ")

# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *    
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     print("* "*(n-i))
# for k in reversed(range(5-1)):
#     for m in range(k):
#         print(" ",end="")
#     print("* "*(n-k))
#           #(OR)
# n=5
# for i in range(n):
#     print(" "*i,end="")
#     print("* "*(n-i))
# for k in reversed(range(n-1)):
#     print(" "*k,end="")
#     print("* "*(n-k))
#         #(OR)
# n=5    
# for i in range(n):
#     print(" "*i,"* "*(n-i))
# for k in reversed(range(n-1)):
#     print(" "*k,"* "*(n-k))
  
#     *
#    **
#   ***
#  ****
# *****
# for i in range(0,6):
#     for j in range(i,5):
#         print(" ",end="")
#     print("*"*(i))
# print(" ")

# n = m = 0
# list_num=[]
# for i in range(1,11):
#     list_num.append(int(i))
# print(list_num)
# for j in list_num:
#     if j%2==0:
#         n+=1
#     else:
#         m+=1
# print("total even number: ",n)
# print("total odd number: ",m)

# 7table
# for i in range(1,11):
#     print("7 X",i,"=",i*7)

# m=1
# n=1
# for i in range(0,5):
#     for j in range(m,6):
#         print(j,end=" ")
#     for k in range(1,n):
#         print(k,end=" ")
#     print(" ")
#     m=m+1
#     n=n+1

# 2
# 4 6
# 8 10 12
# 14 16 18 20
# 22 24 26 28 30
# n=1   
# for i in range(1,6):
#     for j in range(i):
#         print(n*(2),end=" ")
#         n+=1
#     print(" ")

#          *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(1,i):
#         print("*",end=" ")
#     print(" ")
# for i in reversed(range(1,6-1)):
#     for j in range(6-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(1,i):
#         print("*",end=" ")
#     print(" ")

n=0
list2=[]
list1=[5,2,6,1,4,3,8,9,12,7]
for i in list1:
    for j in range(0,len(list1)):
        a=i+list1[j] 
        if a==7 :
            # print("[",i,",",list1[j],"]")
            print(list((i,list1[j])))
            n+=1
        else:
            continue
print("possible in 7: ",n) 

# Decimal to Binary Converter
# num= int(input("Enter the NUmber: "))
# def Binary_Converter(n):
#     if n>1:
#         Binary_Converter(n//2)
#     print(n%2,end="")
#     # a=n%2
#     # print(a,end="")
# Binary_Converter(num)

# Inbulit method for decimal to Binary converter
def number(num):
    a=bin(num)[2:] # this is inbuilt method
    print(a)
number(8)

# num=int(input("enter the number: "))
# b=bin(num)[2:]
# a=list(reversed(b))
# c=" ".join(a)
# if c==b:
#     print("its true")
# else:
#     print("flase")
# print(c)
# print(a)
# print(type(b))

# num=int(input("enter the number: "))
# b=bin(num)[2:]
# a=b[::-1]
# print(b)
# print(a)
# if b==a:
#     print("its true")
# else:
#     print("its false")
    
# Swap two number using without third characters
# a=21
# b=11
# a=a+b
# b=a-b
# a=a-b
# print("a: ",a)
# print("b: ",b)

# str="india is my country"
# voewls=["a","i","e","o","u"]
# count=0
# b=len(str)
# print(b)
# for i in voewls:
#     for j in range(0,len(str)):
#         if str[j]==i:
#           count=count+1
# c=b-count
# print(count,": no of vowels")
# print(c,": no of contencenes")

# text = "india is my country in 2025"
# vowels = ["a", "e", "i", "o", "u"]
# for ch in text:
#     if ch.lower() in vowels:
#         print(ch, ": is a vowel")
#     elif ch.isalpha():
#         print(ch, ": is a consonant")
#     elif ch.isdigit():
#         print(ch, ": is digit")

# n=5    
# m=1
# for i in range(1,6):
#     for j in range(0,n):
#         print(" ",end=" ")
#     for k in range(0,m):
#         print("*",end=" ")
#     print(" ")
#     n=n-1
#     m=m+1

n=5
m=1
for i in range(1,6):
    for j in range(0,n):
        print(" ",end=" ")
    for k in range(0,m):
        print("*",end=" ")
    print(" ")
    n=n-1
    m=m+2

#            *   
#          *   *   
#        *   *   *   
#      *   *   *   *   
#    *   *   *   *   *   
 
# n=5  
# m=1
# for i in range(1,6):
#     for j in range(1,n):
#         print(" ",end=" ")
#     for k in range(0,m):
#         print(" * ",end=" ")
#     n=n-1
#     m=m+1

# #      * 
# #     * * 
# #    * * * 
# #   * * * * 
# #  * * * * * 
# for i in range(1, 6 ):
#     print(" " * (6 - i), end="")
#     print("* " * i)
  
# #     * 
# #    * * 
# #   * * * 
# #  * * * * 
# # * * * * *   
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end=" ")
#     print()

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * *
# n=6
# m=2
# for i in range(1, 6):
#     for j in range(1,n):
#         print(" ", end="")
#     for k in range(1,m):
#         print("*", end=" ")
#     print()
#     n=n-1
#     m=m+1         
        
# n=0
# arr=[1,2,3,6,8,5]
# for i in arr:
#     if i != 5:
#         n=n+1
#     else:
#         break
# print("index value for 5:",n)

# n=0
# m=1
# for i in range(0,5):
#     a=n+m
#     n=m
#     m=a
#     print(a)

# arr = [4,5,2,3,1]
# for i in range(0,len(arr)):
#     print(i)

#Ascending Order
# arr= [7, 3, 1, 4, 9]
# for i in range(0,len(arr)-1):
#     for j in range (0,len(arr)-1):
#         if arr[j]>arr[j+1]:
#             temp = arr[j+1]
#             arr[j+1]= arr[j]
#             arr[j] =temp
# print(arr)

# Descending Order
# arr1=[2, 5, 8, 1, 3]
# swap =0
# for i in range(0,len(arr)-1):
#     for j in range (0,len(arr)-1):
#         if arr1[j]<arr1[j+1]:
#             temp = arr1[j+1]
#             arr1[j+1]= arr1[j]
#             arr1[j] =temp
#             swap+=1
# print(arr1)
# print(swap)

#Count the Swap value
arr1=[4, 3, 2, 1]
swap=0
for i in range(0,len(arr1)-1):
    for j in range (0,len(arr1)-1):
        if arr1[j]>arr1[j+1]:
            temp = arr1[j+1]
            arr1[j+1]= arr1[j]
            arr1[j] =temp
            swap+=1
print(arr1)
print(swap)

arr1=[9, 5, 2, 8, 3]
swap=0
for i in range(0,len(arr1)-1):
    for j in range (0,len(arr1)-1):
        if arr1[j]>arr1[j+1]:
            temp = arr1[j+1]
            arr1[j+1]= arr1[j]
            arr1[j] =temp
            swap+=1
    if swap == 1:
        n=len(arr1)
print(arr1)
print(arr1[n-1])
            
def length(a,b=None):
    # m=3
    num = number(a,b)
def number(e,f):
    if e==f:
        print("hi",e*f)
print(length(3,3))
        
thistuple = ("apple", "banana", "cherry")
a =list(thistuple)
a.insert(1,"orange")
c= tuple(a)
print(c)