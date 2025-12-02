#a constructor replaces method
#and enables to define values while creating the object itself without separately calling the method name.
class person:
    def __init__(self,id,fname,lname,age): #this is the syntax for creating constructor
        self.id=id #create instance variable as usual
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalues(self): #for printing all the variable we use a method
        print(self.id,self.fname,self.lname,self.age)
person1=person(101,'Mezba','Sageer',21)
#this is the difference btw method and a constructor
#within constructor we can pass the values while object creation itself
person1.printvalues()
person2=person(102,'Farseena','Azies',21)
person2.printvalues()
person3=person(103,'Jude','Alron',22)
person3.printvalues()
