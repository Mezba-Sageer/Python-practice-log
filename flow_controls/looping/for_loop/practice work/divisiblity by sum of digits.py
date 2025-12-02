#12.	Print all numbers between 10 and 99 that are divisible by the sum of their digits.
for i in range(10,100):
    temp=i
    sum=0
    while(temp!=0):
       digit=temp%10
       sum+=digit
       temp//=10
    if(i%sum==0):
        print(i)



