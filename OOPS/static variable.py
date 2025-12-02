# print the following : id,fname,lastname, gender, dept, company name using class,object and reference
class employee:
    dept='HR'
    company_name='zellis'
    def details(self,ID,fname,lname,gender):
        self.id=ID
        self.first_name=fname
        self.last_name=lname
        self.gender=gender
    def printdetails(self):
        print(self.id,self.first_name,self.last_name,self.gender,employee.dept,employee.company_name)
employee1=employee()
employee1.details(101,'Mezba','Sageer','F')
employee1.printdetails()

employee2=employee()
employee2.details(102,'Farseena','Azies','F')
employee2.printdetails()

employee3=employee()
employee3.details(103,'Jude','Alron','M')
employee3.printdetails()