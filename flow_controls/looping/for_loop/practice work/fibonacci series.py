#7.	Write a loop that prints the Fibonacci series up to the N-th term (N given by user).
n=int(input("Enter the limit: "))
num1=0
num2=1
print(num1,end=" ")
print(num2,end=" ")
for i in range(2,n+1):
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum,end=" ")