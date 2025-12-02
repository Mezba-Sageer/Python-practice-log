lower=int(input("enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
sum=0
while(lower<=upper):
    if(lower%2==1):
        sum+=lower
    lower+=1
print(sum)
#print the sum of odd number btw the lower to upper range
