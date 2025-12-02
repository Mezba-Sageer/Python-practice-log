#47
#ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they
#want to add another numer. if they enter "y", ask them to enter another number and keep adding numbers until
#they do not answer "y".Once the loop has stopped, display the total.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("sum of first two numbers is: ",num1+num2)
sum=num1+num2
another_num = input("Do you want to enter another number(y/n) : ").lower()
while(another_num=="y"):
    if(another_num=="y"):
        num3=int(input("enter another number: "))
        sum+=num3
        another_num = input("Do you want to enter another number: ").lower()
    else:
        break
print("The total sum is: ",sum)
