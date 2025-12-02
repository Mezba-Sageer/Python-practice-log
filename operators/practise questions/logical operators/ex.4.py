#42.	Accept a number and check if it is divisible by both 2 and 3 but not by 5.
num=int(input("Enter a num: "))
if(num%2==0 and num%3==0):
    if(num%5!=0):
        print("Conditions are met")
    else:
        print("Divisible by 5")
else:
    print("Not divisible by any number")