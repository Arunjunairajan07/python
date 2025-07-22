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

# # #acessing the list
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
data=[]
per_details={'name':'arun','age':21,'DOB':4/4/2003}
data.append(per_details)
print(data)
edu_details={'school':'guru','high school':'grace','clg':'sit'}
data.append(edu_details)
print(data[1]['clg'])

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

a=10        #global variable
b=30        #global variable
def add():
    c=a+b
    return c
res=add()
print(res)
c=b-a
print("the answer is",c)   

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

num=random.randint(1000,2000)+1
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

#modules

# import if_condition as m
# print(m.num(5))

#high order function
def happy():
    print("jumping")
happy()
veryhappy = happy
veryhappy()

def angry():
    print("anonyms")
angry()

def feeling(func):
    func()
    print("sad")
feeling(angry)

#lambda
rectangle = lambda l,b: l*b
print(rectangle(2,3))

age = lambda a : "your 5std " if a<10  else "your 10std"
print(age(15))

#sorted with key
# item = [(1,"arun",90),(5,"vasanth",25),(3,"mahesh",50)]
# item.sort()
# print(item)
# item.sort(key=lambda item:item[2])
# print(item)

item = ((1,"arun",90),(5,"vasanth",25),(3,"mahesh",50))
a= list(item)
print(a)
a.sort(key=lambda item:item[2])
print(a)
# print(sorted(item))
# print(sorted(item,key=lambda item:item[2]))

#map
item = [(1,"arun",90),(5,"vasanth",25),(3,"mahesh",50)]
product = lambda item :(item[0],item[1],float("{:.2f}".format (item[2]/74)))
shop = list(map(product,item))
print(shop)


#sqr with map
val=[2,5,7,9,4]
mul= lambda x: x*x
sqr=list(map(mul,val))
print(sqr)

# even or odd in function
num=[22,45,32,12]
# def sqr (*a):
#     if a%2==0:
#         print("even")
#     elif a%2!=0:
#         print("odd")
# sqr(num[22,45,32,12])
sqr=lambda a: "even" if a%2==0 else "odd"
c=list(map(sqr,num))
print(c)
    
temp=[102,99,89,70,103]
con=lambda a:float("{:.2f}".format((a-32)*5/9))
b=list(map(con,temp))
print(b)

#fliter
item = [(1,"arun",90),(5,"vasanth",25),(3,"mahesh",50)]
fil=lambda item: (item[2]<=50)
scan=list(filter(fil,item))
print(scan)

num=[34,56,90,67,21,56,90]
a=lambda num : num<=70
b=list(filter(a,num))
print(b)

#Reduce
import functools
a=[32,45,67,89,2]
b= lambda add,addd: add+addd
c=functools.reduce(b,a)
print(c)

#Map
temp=[102,99,89,70,103]
a=lambda x : float("{:.2f}".format((x-32)*5/9))
b= list(map(a,temp))
print(b)

#list comperhension
#[expn foe item in interable if condition]
#[expn if-else for item in interable]
temp=[102,99,89,70,103]
celsius = [float("{:.2f}".format((i-32)*5/9))for i in temp]
print(celsius)

num=[2,4,8,12,34,56]
number=[i if i<=10 else 10 for i in num]
print(number)

# Dictionary comprehension
#{expn if-else for (key,val) in interable}
a={"phone":16000,"Airpods":1000,"laptop":19000,"bike":80000,"camera":35000}
b={key:val*.9 if val >10000 else val for (key,val) in a.items()}
print(b)
 
a={"phone":16000,"Airpods":1000,"laptop":19000,"bike":80000,"camera":35000}
b={key:val*.9 for (key,val) in a.items()}
print(b)

#zip
a=["redmi","realme","oppo","vivo","apple","oneplus"]
b=[15000,16500,20000,18000,150000,25000]
c=[20,8,5,3,1]
d=list(zip(a,b,c))
print(d)

#Multithreading

# import threading
# import time
# def number(num):
#     for i in range(1,num+1):
#         a=i*i
#         print(a)
#         time.sleep(2)
        
# print("hello")    
# def add(a,b):
#     c=a+b
#     print(c)
    
# add(10,20)
# number(10)

# a=threading.thread(target=add)
# a.start()
# print(threading.action_count())

def even(n):
    for i in n:
        if i%2==0:
            print(i)
        else:
            print("false")
         
a=[1,2,3,4,5,6]   
print(even(a))

def args(*cuboid):
    for i in cuboid:
        volume=i*i*i
        print(volume)
print(args(4,5,6))

num =112
num1 = num%10
print(num1)
n= num//10
print(n)

n=123
m=0
while n>0:
    num = n%10
    n = n//10
    m+=1
    # m+= num
print(m)
for i in range(m):
    print(i)

    
    