#17.	Print all perfect numbers between 1 and 1000.
# (Perfect number = sum of its divisors excluding itself equals the number)
for i in range(1,1001):
    sum=0
    temp=i
    for j in range(1,temp):
        if(temp%j==0):
            sum+=j
    if(sum==i):
        print(i)