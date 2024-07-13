class laptop:
    
    # price=0       class variable
    # processor=" "
    # ram=" "
    
    def __init__(self,price,processor,ram):     #instance variable
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
#print(lenovo.lenovo1())
# print(Dell.dell1())

class student():
    def __init__(self):
        self.name="arun"
        self.regno="5006"
    def display(self):
        print("student name: ",self.name)
        print("student regno: ",self.regno)
    def display1(self):  
        print("student name: ",self.name)
        print("student regno: ",self.regno)  
        
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

print(add.add1())
print(sub.sub1())
print(mul.mul1())
print(div.div1())

        
           