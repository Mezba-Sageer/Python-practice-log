#only syntax and concept is necessary, no indepth study required.
#1. Inheritance
#2.Polymorphism
#3.Abstraction
#4.Encapsulation
# presentation on tuesday(08/07/2025) on polymorphism, abstraction, encapsulation with example.
#1. Inheritance:
#there must be a minimum of 2 classes for inheritance
# first class being the parent class and the 2nd class is child class
#the child class can use the features within the parent class,(features include: methods, instance variable etc.)
#the child class has features of its own and also has access to the parent class features

#eg: for inheritance
class A: #parent or base class
    def printa(self,num1):
        self.no1=num1
        print("Inside class A",self.no1)
class B(A):#derived class
     #giving 'A' class within parenthesis is inheritance. or i.e the syntax
    def printb(self,num2):
        self.no2=num2
        print("Inside class B",self.no2)

obj1=B() #here within object created for class B
obj1.printb(12)
obj1.printa(10) #we can call features or methods within A because we mentioned class A next to B


