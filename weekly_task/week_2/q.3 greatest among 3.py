#Write a program to find the greatest number among three numbers.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if(num1>num2 and num1>num3):
    print(num1,"is the greatest")
elif(num2>num3 and num2>num1):
    print(num2,"is the greatest")
else:
    print(num3,"is the greatest")