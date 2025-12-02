#20.	Accept numbers from user until they enter 0, then print the total sum.
num=int(input("Enter a number: "))
sum=0
while(num!=0):
    sum+=num
    num = int(input("Enter a number: "))
print(sum)
