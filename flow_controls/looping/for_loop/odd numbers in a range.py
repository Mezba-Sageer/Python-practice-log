#print the odd numbers btw lower to upper limit

lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
