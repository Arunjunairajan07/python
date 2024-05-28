#star

for i in range(1,11):
    print("*")

# guessing game

import random

num=random.randint(1,20)
guess=int(input("guess the number is less than 20: "))

while num!=guess:
     if guess>num:
      print("your guess number is higher")
     else:
      print("your guess number is lower")
     guess=int (input("guess again: "))   
 
print ("you won")   
 
 #list

list_num=[]
for i in range(1,11):
    list_num.append(int(i))
print(list_num)
for j in list_num:
    if j%2==0:
        print("this number are even: "+str(j))
    else:
        print("this number is odd: "+str(j))

#pattern 
n=1
for i in range(1,5):
    for j in range(0,n):
        print("*",end="") 
        n+=1
    print("")    
    
    

   
        
 
    
     
    
