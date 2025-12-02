#print all arm strong numbers between the upper and lower limit
upper=int(input("Enter the upper limit: "))
lower=int(input("enter the lower limit: "))
for i in range(lower,upper+1): #to check no.s btw upper nd lower limit
    count=0 #within the loop to keep the count incrementing
    sum=0 #count and sum set as 0 within the loop so that when the next value
          # is being checked in the i loop the sum and count is set back to 0
    num=i #i value is kept constant by assigning to another variable for first while loop
    num2=i #for 2nd loop
    while(num>0): #to check how much digits(or length) are there in the user input from lower to upper
       num//=10
       count+=1
    while(num2>0):
        digit=num2%10
        sum+=digit**count
        num2//=10
    if(i==sum):
        print(i,end=" ") #end=" " to print in a single line







