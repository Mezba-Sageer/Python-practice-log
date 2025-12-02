#19.	Accept a number and print the Fibonacci sequence up to that number.
num=int(input("enter a number: "))
num1=0
num2=1
i=2
print(num1,num2,end=" ")
while(i<=num):
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum, end=" ")
    i+=1
