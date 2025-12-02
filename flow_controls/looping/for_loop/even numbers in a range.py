#print lower to upper limit even numbers only
lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))
for i in range(lower,upper+1): #here i is the value getting incremented and not lower,bcz i is the variable #
                               # lower nd upper is jst the range
                               #i=value given for the lower limit, if lwr limit=2, i=2,i=3,.......i=upper limit
    if(i%2==0):
        print(i)

