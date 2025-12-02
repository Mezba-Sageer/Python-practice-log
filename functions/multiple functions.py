#print:-
#A. Addition
#B. Subtraction
#C. Multiplication
#D. Division
#Enter Your choice(a,b,c,d)
#display of the result according to the option

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")

num1=int(input("Enter no.1: "))
num2=int(input("Enter no.2: "))
choice=input("Enter your choice: ")
if choice=="A" or choice=="a":
    print("sum is: ",addition(num1,num2))
elif(choice=="b" or choice=="B"):
    print("Difference is: ",subtraction(num1,num2))
elif(choice=="c" or choice=="C"):
    print("product is: ",multiplication(num1,num2))
elif(choice=="d" or choice=="D"):
    print("division value is: ",division(num1,num2))
else:
    print("invalid choice")
print(addition(2,4)) #print statement used bcz return is used abv
#practice question
# def addition(x,y):
#     return x+y
# def difference(x,y):
#     return x-y
# def product(x,y):
#     return x*y
# def division(x,y):
#     return x/y
# print("sum: ",addition(10,12))
# print("difference : ",difference(12,15))
# print("product : ",product(3,4))
# print("division : ",division(6,3))