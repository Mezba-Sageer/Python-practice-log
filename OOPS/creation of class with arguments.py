#creation of class,methods and object using instance variable
class person:
    def values(self,fname,lname,age,gender,phno):
        #this is a method name with variable names to create instance variable
        self.first_name=fname
        #this is the creation of instance variable
        # syntax: self.variable name= variable mentioned at the argument of the class name
        self.lasl_name=lname
        self.age=age
        self.gender=gender
        self.phone_num=phno
    def printvlaues(self):
        print(self.first_name,self.lasl_name,self.age,self.gender,self.phone_num) #here we print the instance variables

person1=person() #creation of object
person1.values('Mezba','sageer',21,'female',8891333905)
#we define the values when creating the reference
person1.printvlaues() #this is calling next operation