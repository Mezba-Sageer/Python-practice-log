#9.	Print the sum of even numbers between 1 and n.
sum=0
n=int(input("Enter the limit: "))
i=1
while(i<=n): #1<=10T
    if(i%2==0):
        sum+=i
    i+=1
print("sum of even numbers is: ",sum)
