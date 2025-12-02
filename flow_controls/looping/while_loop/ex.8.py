#sum of n numbers
limit=int(input("enter a number"))
i=1
sum=0 #setting zero to get the value 1
while(i<=limit): #1<=5 2<=5 3<=3 eg:
    sum+=i #0+1=1, 1(sum)+2(i)=3, 3+3=6, 6+4=10
    i+=1 #i increment
print("the sum is",sum) #printing out of the while to get the sum printed once


