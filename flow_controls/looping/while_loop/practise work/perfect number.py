#25.	Check whether a number is a perfect number (sum of divisors equals the number).
num=int(input("enter a number: "))
temp=num
i=1
sum=0
while(i<temp):
    if(temp%i==0):
        sum+=i
    i+=1
if(num==sum):
    print(num,"is a perfect number")
else:
    print("not a perfect number ")