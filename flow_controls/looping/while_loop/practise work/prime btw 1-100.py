#31.	Print all prime numbers between 1 and 100 using nested while loops.
i=2
while(i<=100):
    count=0
    j=2
    while(j<i):
        if(i%j==0):
            count+=1
        j+=1
    if(count==0):
        print(i,end=" ")
    i+=1

