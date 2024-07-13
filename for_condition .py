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
n=1
for i in range(1,5):
    for j in range(0,n):
        print("*",end="") 
    n+=1
    print("")    
    
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

n=5
for i in range(1,6):
    if i<=n:
        print(i,end=" ")
        x=i
           
    for j in range(0,5):
        if j<i-1:
            x=x+((n-1)-j)   
            print(x,end=" ") 
    print(" ")
    
# thislist = list(("apple", "banana", "cherry"))
# thislist.remove("apple")
# print(thislist)

a="WELCOMETOZOHOCORPORATION"
n=1
for i in range(0,len(a)):
    if i<=n:
        print(a[i],end=" ")
    for j in range(0,1):
        if n%5==0:
            print("")
    n=n+1        
