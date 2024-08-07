#star

# for i in range(1,11):
#     print("*")

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
#         print("this number are even: "+str(j))
#     else:
#         print("this number is odd: "+str(j))

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
    
a=[1,2,3,4,5]
for i in a:
    a.remove(i)
    print(a)
    
#number pattern

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

# a="WELCOMETOZOHOCORPORATION"
# n=1
# for i in range(0,len(a)):
#     if i<=n:
#         print(a[i],end=" ")
#     for j in range(0,1):
#         if n%5==0:
#             print("")
#     n=n+1        
    
# a="hello world"
# print(a[::-1])

# rev=["hello","world","welcome","to","python"]
# i=5
# while i>0:
#      i=i-1
#      print(rev[i])
     
     
# reverse word

list1=[]
a="hello world"
b=a[::-1]
c=b.split(" ") 
print(c)
for n in range(0,2):
    d=c[n]
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
#     print(" ")
    
