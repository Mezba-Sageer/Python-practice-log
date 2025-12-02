#36.	Accept two numbers and check if one is a multiple of the other using == and %.
num1=int(input("Enter no.1: "))
num2=int(input("Enter no.2: "))
if(num1%num2==0):
    print("num1 is a multiple of num2")
elif(num2%num1==0):
    print("num2 is a multiple of num1")
else:
    print("not a multiple")