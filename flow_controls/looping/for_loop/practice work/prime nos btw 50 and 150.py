#4.	Find all prime numbers between 50 and 150.
for i in range(50,151):
    count=0
    for num in range(2,i):
        if(i%num==0):
            count+=1
            break
    if(count==0):
        print(i)