#8.	Print all pairs of numbers from 1 to 50 whose product is divisible by 24.
for i in range(1,51):
    for j in range(i,51):
        if((i*j)%24==0):
            print(i,j)