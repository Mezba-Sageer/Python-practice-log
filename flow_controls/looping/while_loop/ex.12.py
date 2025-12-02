#print lower to upper range's odd number
lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
while(lower<=upper):
    if(lower%2==1): #if a num divided by 2 and the reminder is 1 odd #or (lower%2!=0)
        print(lower)
    lower+=1



