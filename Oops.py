#constructor

#constructor is a special method in a class that automatically gets called when an object is created.
# An instance variable is a unique variable for each object. Once it is created, it can be used in many methods within the same class."

class laptop:
    
    # price=0       class variable
    # processor=" "
    # ram=" "
    
    def __init__(self,price,processor,ram):     #constructor
        #instance variable
        self.price = price
        self.processor = processor
        self.ram = ram
        
    def dell1(self):
        print("Dell laptop prices is: ",Dell.price)
        print("Dell laptop processor is: ",Dell.processor)
        print("Dell laptop ram is: ",Dell.ram)
        
    def hp1(self):
        print("Hp laptop prices is: ",Hp.price)
        print("Hp laptop processor is: ",Hp.processor)
        print("Hp laptop ram is: ",Hp.ram)
    
    def lenovo1(self):
        print("lenovo laptop price is: ",lenovo.price)
        print("lenovo laptop processor is: ",lenovo.processor)
        print("lenovo laptop ram is: ",lenovo.ram)
      
       
Hp=laptop("45000","helio","8GB")
Dell=laptop("55000","mediatech","6GB")
lenovo=laptop("19000","intel","12GB")

# Hp.price=45000
# Hp.processor="helio"
# Hp.ram="8GB"

# Dell.price=55000
# Dell.processor="mediatech"
# Dell.ram="6GB"

# lenovo.price=19000
# lenovo.processor="intel"
# lenovo.ram="12GB"

print(Hp.hp1())
print(Dell.dell1())
print(Hp.lenovo1())
# print(lenovo.lenovo1())
# print(Dell.dell1())

class student():
    def __init__(self):
        self.name="arun"
        self.regno="5006"
    def display(self):
        print("student name: ",self.name)
        print("student regno: ",self.regno)
    def display1(self):  
        print("student name: ",s2.name)
        print("student regno: ",s2.regno)  
        
s1=student()
s2=student()
#s2= student("sham","5005")
s2.name="sham"
s2.regno="5005"

print(s1.display())
print(s2.display1())    

#calculator

class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        c = self.a + self.b
        print("The answer is: ",c)  
    def sub1(self):
        c = self.a - self.b
        print("The answer is: ",c)
    def mul1(self):
        c = self.a * self.b
        print("The answer is: ",c)
    def div1(self):
        c = self.a / self.b
        print("The answer is: ",c)     
        
add=calculator(5,5)
sub=calculator(10,5)
mul=calculator(5,5)
div=calculator(30,5)

print(add.sub1())
print(mul.add1())
print(div.add1())
# print(sub.sub1())
# print(mul.mul1())
# print(div.div1())

# The five types of inheritance in Python 
# single
# multiple
# multilevel 
# hierarchical and 
# hybrid inheritance.

# multiple inheritances

# two base class
# one dervied class

class sem1():
    def year1(self):
        print("The python subject")
        
class sem3():
    def year2(self):
        print("The data structure subject")
        
class sem5(sem3,sem1):
    def year3(self):
        print("The networking subject")
        
stu=sem5()
print(stu.year2())
print(stu.year3()) 
# print(stu.year2())   
#print(stu.year1()) 

# single inheritances

# one base class
# one dervied class

class selvam():
    def bank(self):
        print("The bank balances is 45000")
        
class Arun(selvam):
    def clgfees(self):
        print("The clg fees is 45000")
        
acc=Arun()
print(acc.bank())
print(acc.clgfees())

#MULTILEVEL INHERITANCES

#one base class
#one dervied class
# Base class → Derived class → Another derived class.
# its the chain format inheritances .

class webseries():
    def Theboys(self):
        print("The Boys series")
        
class cinema(webseries):
    def Goat(self):
        print("The Goat movies")
        
class Serial(cinema):
    def sarmen(self):
        print("The saravana meenaskshi serial")
        
class youtuber(Serial):
    def vjsiddhu(self):
        print("The housetower series")        

Tv=youtuber()
movies=cinema()
# print(Tv.vjsiddhu())
# print(Tv.sarmen())
print(movies.Theboys())
print(Tv.Theboys())
print(Tv.Goat())
print(movies.Goat())
print(Tv.Theboys())
print(Tv.sarmen())


#hierarchy inheritance

# one base class
# more dervied class

class mobile():
    def anbu(self):
        print("9734689456")
        
class whatsapp(mobile):
    def priyan(self):
        print("7092093611")
        
class insta(mobile):
    def arun(self):
        print("2498-08-8348")
        
class facebook(mobile):
    def rajan(self):
        print("8938095487")
        
app=insta()
ph=facebook()
# print(insta.arun())
print(ph.anbu())


# hybird inheritance
# hybird inheritance is single,multiple,multilevel,hieriarchy inheritance are known is hybird inheritance 

#super keyword

class a():
    def __init__(self):
        print("A")
    def pin(self):
        print("hello world")
        
class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def pins(self):
        print("python")
        
class c(b):
    def letters(self):
        super().pins()
        print("hi bro")
        
let=c()
print(let.letters())

#method overriding

class student():
    def name(self):
        print("arunjunai")
        
class pera():
    def rollno(self):
        print("21cd010")
        
class namm():
    def reg(self):
        print("921721115006")
        
class manavan(pera,namm,student):
    def name(self):
        print("rajan")
        
# s1=student()
# s2=pera()
# s3=namm()
s4=manavan()

print(s4.name())
print(s4.rollno())
print(s4.reg())

#super keyword
#Once a constructor is created in the parent class, it can be used in the child class using the super keyword."
class car():
    def __init__(self,color,num):
        self.color=color
        self.num=num
    def sukui(self):
        print("car",self.num)
        print("car",self.color)
        
class bike(car):
    def __init__(self,color,num,model):
        super().__init__(num,color)
        self.model =model
    def duke(self):
        print("bike",self.num)
        print("bike",self.color)
        print("bike",self.model)
        
class auto(bike):
    def __init__(self,num,color,model):
        super().__init__(num,color,model)
    def hero(self):
        print("auto",self.num)
        print("auto",self.color)
        print("auto",self.model)
        
v1=auto("7845","red","v4")

print(v1.duke())
print(v1.sukui())
print(v1.hero())

#polymorphism
#"Poly" = many,"Morphism" = forms.one operator behaving different performs is polymorphism
#method overloading

# class shape():
#     def area(self,a):
#         self.a=a
#         self.b=self.a*self.a
#         print("the answer is: ",self.b)
    
# class rectangle(shape):
#     # def __init__(self,l,b):
#     #     self.l=l
#     #     self.b=b  
#     def area(self,l,b):
#         self.l=l
#         self.b=b
#         c=self.l*self.b
#         print("area of rectangle is: ",c)
    
# rec=rectangle()
# print(rec.area(5,3))
# print(rec.area(5))

#Encapsulation
#Encapsulation is the concept of bundling the data (variables) and the methods (functions) that operate on that data into a single unit 
#private -(private is used in __) don't call directly in dress varriable,only function used call the dress variable
class shop():
    def __init__(self):
        self.__dress="shirt"
    def birthday(self):
        print("shop :",self.__dress)
        
class pant(shop):
    def __init__(self):
        super().__init__()
    def dress(self):
        print("pant",self.__dress) 
    def private_acess(self):
        self.birthday()   
  
s1=pant()
print(s1.dress())
#print(s1.private_acess())

#protector-(protector is used in _)protector is that variable are used in derived class of inherit the that class
class car():
    def __init__(self):
        self._color="red"
        self._num=6543
    def sukui(self):
        print("car",self._num)
        print("car",self._color)
        
class bike(car):
    def __init__(self):
        super().__init__()
    def duke(self):
        print("bike",self._num)
        print("bike",self._color)

        
b1=bike()
print(b1.duke())
print(b1.sukui())

#method Overloading
# class Parent:
#     def display(self,a=None,b=None):
#         # if a is not None and b is not None:
#         #     print(f"Parent: Two arguments: {a} and {b}")
#         # elif a is not None:
#         #     print(f"Parent: One argument: {a}")
#         # else:
#         #     print("Parent: No arguments")
#         c=int(a*b)
#         print(c)

# class Child(Parent):
#     def display(self,a=None,b=None,c=None):
#         # if a is not None and b is not None and c is not None:
#         #     print(f"Child: Three arguments: {a}, {b}, and {c}")
#         # elif a is not None and b is not None:
#         #     print(f"Child: Two arguments: {a} and {b}")
#         # elif a is not None:
#         #     print(f"Child: One argument: {a}")
#         # else:
#         #     print("Child: No arguments")
#         d=int(a*b*c)
#         print(d)
        
# c = Child()
# print(c.display(5,3))
# print(c.display(5,3,2))
# # c = Child()
# # c.display()
# # c.display(10)
# # c.display(10, 20)
# # c.display(10, 20, 30)

# method Overriding
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class")
        super().show()  # Call the parent class method
        

c = Child()
print(c.show())
# Parent.show(c) # Only call the Parent's method

#abstraction 
from abc import ABC,abstractmethod

class bike(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def gear(self):
        pass
    
    @abstractmethod
    def off (self):
        pass
    
class splender(bike):
    def start(self):
        print("start the bike splender")
        
    def gear(self):
        print("gear the bike splender")
        
    def off(self):
        print("off the bike splender")
        
class xplus(bike):
    def start(self):
        print("start the bike xplus ")
        
    def gear(self):
        print("gear the bike xplus")
        
    def off(self):
        print("off the bike xplus")
        
hero=splender()
print(hero.off())
         
    