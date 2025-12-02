#q.9 Write a program that uses break and continue in a nested loop to find and
# print the first pair of numbers i, j) where i * j is greater than 10.
count=0
for i in range(1,11):
    for j in range(1,11):
        if(i*j<=10):
            continue
        elif(i*j>10):
            print(i,j)
            count=1
            break
    if(count==1):
        break

