#13.	Calculate factorial of a number using a while loop.
num=int(input("enter a num: "))
fact=1
i=1
while(i<=num):
    fact*=i
    i+=1
print(fact)
