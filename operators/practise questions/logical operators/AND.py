#21.	Accept two numbers and check if both are even using and.
num1=int(input("Enter the 1st num: "))
num2=int(input("Enter the 2nd num: "))
if(num1%2==0 and num2%2==0):
    print("even")
else:
    print("Odd")
#22.	Accept two numbers and check if at least one is odd using or.
if(num1%2!=0 or num2%2!=0):
    print("At least one is odd")
else:
    print("both even ")

#23.	Accept a number and check if it's between 10 and 20 using and.
num3=int(input("Enter a num: "))
if(num3>=10 and num3<=20):
    print("yes")
else:
    print("no")