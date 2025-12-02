#to check if a number is prime number(to see if only 1 and that number is their factor)
limit=int(input("Enter a number: "))
if(limit<0):
    print("Please enter a positive integer")
elif(limit==0):
    print("You have entered zero")
elif(limit==1):
    print("1 is a composite number")
else:
    for i in range(2,limit):
        if(limit%i==0):
            print(limit,"is not prime")
            break #if the number is divisible by one number, break is used to not execute the loop further
                  # (not to increment the i value) i.e the reason why multiple not prime statement is not printed
    else: #this else for the for loop
        print(limit,"is prime number")






