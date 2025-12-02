#2.	Find all numbers between 100 and 999 where the sum of the cubes of digits equals the number. (Armstrong numbers)
for i in range(100,1000):
    sum=0
    temp=i
    while(temp!=0):
        digit=temp%10
        sum+=digit**3
        temp//=10
    if(sum==i):
        print(i)

