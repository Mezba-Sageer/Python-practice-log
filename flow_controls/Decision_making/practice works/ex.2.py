#Accept a number and check if it's a 3-digit even number using chained conditions.
num=int(input("Enter a number: "))
if(100<=num<=999):
    if(num%2==0):
        print("It is a 3 digit even number")
    else:
        print("It is a 3 digit odd number")
else:
    print("it is not a three digit number")