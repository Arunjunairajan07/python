#string slicing
 
#name="HAPPY"
# print(name[:1])
# print(name[0:2])
# print(name[0:3])
# print(name[0:4])
# print(name[0:5])
 
# print(name[4])
# print(name[3:5])
# print(name[2:5])
# print(name[1:5])
# print(name[0:5])

# x=slice(0,2)
# print(name[x])
 
#  #list
 
# cities=["coimbatore","madurai","trichy","chennai","salem"]

# #acessing the list
# print(cities[::3])

# #modified the list (Exchange the values)
# cities[4]="kerala"
# print(cities)

# #append the list (insert the last place)
# cities.append("thuthukudi")
# print(cities)

# #insert the value in the choose the user index place
# cities.insert(1,"bombay")
# print(cities)

# #pop the list (delete the value in list and display the deleted value)
# Delete=cities.pop(5)
# print(cities)
# print(Delete)

# #length of the list
# print(len(cities)) 

# #REVERSE THE list
# cities.reverse()
# print(cities)


# reverse = "hello world"
# print(reverse[::-1])

# x=slice(2,-2)
# print(reverse[x])

#dictinoary
# data=[]
# per_details={'name':'arun','age':21,'DOB':4/4/2003}
# data.append(per_details)
# print(data)
# edu_details={'school':'guru','high school':'grace','clg':'sit'}
# data.append(edu_details)
# print(data[1]['clg'])

# for key,value in per_details.items():
#     print("key",key)
#     print("value",value)
    
# for Z in per_details.items():
#     print(Z)
 
#  #set     
# varunam={"red","blue","green","yellow","orange","red"}
# list_color=list(varunam)
# print(list_color)

# #formatting
# name="arun"
# education="computer sciences and design"
# address="madurai"
# text="I am {} I am coming from {} I am studying in B.E {} department"
# print(text.format(name,address,education))

# print("I am {} I am coming from {} I am studying in B.E {} department".format(name,address,education))

# age=21
# print("My age is {}".format(age))

#function

# def fun(name,what):
#     print("hello",name)
#     print("hi",what)
# fun("ram","ganesh")

# function using list

# names=[]
# def list_name(name):
#     print("My name is",name)
#     names.append(name)
# list_name("arun kumar")
# list_name("dinesh kumar")
#print(names)

#natural number
# def sum(number):
#     for i in range(1,number):
#         print(i*i)
# sum(11)
# sum(21)

#even numbers

# def even(num):
#     if num%2== 0:
#         print("its is even number")
#     else:
#         print("its not the even number")
        
# even(30)
# even(31)

# sum of n number

# def sum(num):
#      res=num*(num+1)/2  
#      return res
# # print(sum(int(input("The values: "))))
# print(sum(11))

#add using function for gobal varaible
 
# a=10        #global variable
# b=30        #global variable
# def add():
#     a=5     #local variable
#     b=5     #local variable
#     c=a+b
#     return c
# res=add()
# print(res)
# c=b-a
# print("the answer is",c)   

# #multiply using function for local varaible

def mul():
    global a,b
    a=35
    b=7
    c=a*b
    return c
print(mul())
c=a/b
print(c)

# #local and global variable 

# a=10        #global variable
# b=30        #global variable
# def add():
#     c=a+b
#     return c
# res=add()
# print(res)
# c=b-a
# print("the answer is",c)   

# area of circle
# def circle(i):
#         area=3.14*i**2
#         return area
# print(circle(2))
                   
#default 

# def default(name,city="madurai"):
#     print("I am",name) 
#     print("I am comimg from",city)
# default("arun")     

#passing list

# num=["arun","kumar","praveen","ravi","rakesh"]

# def number(num):
#     for i in num:
#         x=print(i.capitalize())
#     return x  
# print(number(num))

#variable arguments

# def args(*cuboid):
#     for i in cuboid:
#         volume=i*i*i
#     return volume
# print(args(4,5,6))
    
# generate the OTP

import random

num=random.randint(1000,2000)
def otp(verified):
    print("enter the your otp",verified)
otp(num)

#exception handling

# try:
#         num1=int(input("Enter the num1 value: "))
#         num2=int(input("Enter the num2 value: "))
#         number=num3/num2
#         print(number)
        
# except NameError as e:
#     print(e)
#     print("NameError: check the assign the value")
             
# except Exception as e:
#     print(e)
#     print("identation error: please check the code arrangement ")
    
# finally:
#     print("please the correct the code")
    
#files
    
with open("if_condition.py") as file:
        print(file.read())
      