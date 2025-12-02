#read lower and upper limit and print the sum of even nums frm lower to upper limit
lower=int(input("enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
sum=0
while(lower<=upper):
    if(lower%2==0):
        sum+=lower
    lower+=1
print(sum)
