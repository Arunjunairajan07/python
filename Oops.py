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
print(Dell.hp1())
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
    def bank(self,a):
        print("The bank balances is 45000")
        
class Arun(selvam):
    def clgfees(self,a):
        print("The clg fees is 45000")
        
acc=Arun()
print(acc.bank())
print(acc.clgfees())

#MULTILEVEL INHERITANCES

#one base class
#two or more dervied class

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
print(Tv.Goat())
print(Tv.Theboys())
print(Tv.sarmen())


#hierarchy inheritance

# one base class
# two dervied class

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
        
ph=facebook()

print(ph.rajan())
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

class car():
    def __init__(self,color,num):
        self.color=color
        self.num=num
    def sukui(self):
        print("car",self.num)
        print("car",self.color)
        
class bike(car):
    def __init__(self,color,num):
        super().__init__(num,color)
    def duke(self):
        print("bike",self.num)
        print("bike",self.color)
        
class auto(bike):
    def __init__(self,num,color):
        super().__init__(num,color)
    def hero(self):
        print("auto",self.num)
        print("auto",self.color)
        
v1=auto("7845","red")

print(v1.duke())
print(v1.sukui())
print(v1.hero())

#polymorphism
#method overloading

class shape():
    def area(self,a):
        self.a=5
        self.b=self.a*self.a
        print("the answer is: ",self.b)
    
class rectangle(shape):
    # def __init__(self,l,b):
    #     self.l=l
    #     self.b=b  
    def area(self,l,b):
        self.l=l
        self.b=b
        c=self.l*self.b
        print("area of rectangle is: ",c)
        

rec=rectangle()
print(rec.area(5,3))

#Encapsulation

#private -(private is used in __) don't call directly in dress varriable,only function used call the dress variable
class shop():
     def __init__(self):
         self.__dress="shirt"
     def birthday(self):
         print("shop :",self.__dress)
    
s1=shop()
print(s1.birthday())

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