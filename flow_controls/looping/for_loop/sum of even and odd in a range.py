#sum of even nd odd num btw lower and upper limit
lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))
even=0
odd=0
for i in range(lower,upper+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print("The sum of even numbers is",even)
print("The sum of odd numbers is",odd)
