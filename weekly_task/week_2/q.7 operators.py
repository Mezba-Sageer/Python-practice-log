#Q7. Write a program to accept two numbers and mathematical operators
# and perform operation accordingly.

num1=int(input("enter no.1: "))
num2=int(input("enter no.2: "))
operator=input("Enter an operator (+,-,/,*): ")
if(operator=='+'):
    sum=num1+num2
    print("the sum is: ",sum)
elif(operator=='-'):
    difference=num1-num2
    print("the difference is: ",difference)
elif(operator=='*'):
    product=num1*num2
    print("the product is: ",product)
elif(operator=='/'):
    division=num1/num2
    print("The division value is: ",division)
else:
    print("invalid operator")