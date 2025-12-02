num1=int(input("Enter no.1: "))
num2=int(input("Enter no.2: "))
sum = lambda a,b:a+b
difference = lambda a,b:a-b
product = lambda a,b:a*b
division = lambda a,b:a/b
print("sum is: ",sum(num1,num2))
print("Difference is: ",difference(num1,num2))
print("Product is: ",product(num1,num2))
print("Divided value is: ",division(num1,num2))
