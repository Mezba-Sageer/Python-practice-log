class student:
    coll="RMIT" #static variable created outside method.
    def details(self,ID,fname,lname,course,gender): #method name with arguments
        self.ID=ID #creation of instance variable
        self.first_name=fname
        self.last_name=lname
        self.course=course
        self.gender=gender  #creation of instance variable using the keyword self
    def printdetails(self):
        print(self.first_name,self.last_name,self.course,self.gender,student.coll)
        #in the print statement for instance variables we use the keyword self
        #while for printing static variable we use class name
student1=student() #object creation - obj 1
student1.details(19,'Mezba','Sageer','analytics','female')
#defining instance variable while passing the operation
student1.printdetails()

student2=student()
student2.details(20,'farsi','azies','analytics','female')
student2.printdetails()

student3=student()
student1.details(21,'Jude','Alron','analytics','male')
student1.printdetails()

student4=student()
student4.details(22,'aryan','nair','analytics','male')
student4.printdetails()