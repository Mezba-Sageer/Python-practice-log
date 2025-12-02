#print lower to upper range divisible by 5 (multiples of 5)

lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
while(lower<=upper):
    if(lower%5==0):
        print(lower)
    lower+=1
