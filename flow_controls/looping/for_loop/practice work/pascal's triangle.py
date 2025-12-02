n=int(input("Enter the no.of rows: "))
for i in range(n):
    for s in range(n-i):
        print(" ",end=" ")
    val=1
    for j in range(i+1):
        print(val,end=" ")
    print()
