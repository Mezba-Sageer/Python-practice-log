#example for single inheritance
#in class person: fname,lname,age,location
#in class profession: ID,dept, qualification
#print all the details in the second class profession in the following order:
#id,fname,lname,age,dept,qualification,location
#there is also multiple inheritance and multi level inheritance
class person:
    def details(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.location=location
        self.age=age
class profession(person):
    def prof_deets(self,id,dept,qualification):
        self.id=id
        self.dept=dept
        self.qualification=qualification
        print(self.id,self.fname,self.lname,self.age,self.dept,self.qualification,self.location)

obj2=profession()
obj2.details('mezba','sageer',21,'kochi')
obj2.prof_deets(101,'IT','bachelors')


