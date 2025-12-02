#guide to creating a class
#here 'class' - is a keyword to create class and person is the class name
#so syntax for class creation is : #class (class name)
#a function created within a class is known as method
#self -is a instance keyword
#an instance keyword creates instance variable-self(this is the instance keyword)
#an instance variable is a variable used within a method which can be used within multiple methods
#instance variable is also known as dynamic variable
class person:
    def printa(self): #here printa is the method name
        print("reading a book")
    def printb(self):
        print("Write a book")

#how to create an object:
obj1=person() #this is the first object
obj1.printa() #this is the operations to be performed within that object which is called using the method name
obj1.printb() #i.e reference

obj2=person() #this is the 2nd object created to perform the operations mentioned within the class person
obj2.printb() #this is calling the method within that class