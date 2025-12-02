#there are 4 types of function arguments
#1.default arguments
#2.keyword arguments
#3.required arguments
#4.variable length arguments

#ex: of keyword arguments
def employee(name,company,salary,location):
    print("Name: ",name)
    print("Company: ",company)
    print("Salary: ",salary)
    print("Location: ",location)
employee(company="EY",location="Kochi",name="Mezba",salary=50000)
#variable name is mentioned along with value while calling the function, even if the order is not right
# the correct values get assigned automatically this is keyword argument
#if it's given in different order other than this method, values get assigned wrong

def rectangle(length,breadth):
    area=length*breadth
    perimeter=2*(length+breadth)
    print("The area is: ",area)
    print("The perimeter is: ",perimeter)
print(rectangle(breadth=6,length=10))


