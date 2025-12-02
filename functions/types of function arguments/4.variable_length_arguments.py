#eg of: variable length arguments
#the star before skills is used to pass multiple arguments into one variable
def employee(name,*skills,age):
    print("name: ",name)
    print("skills: ",skills)
    print("Age: ",age)
employee("mezba","python","EDA","Power BI",age=21)
#('python', 'EDA', 'Power BI') - this is tuple
