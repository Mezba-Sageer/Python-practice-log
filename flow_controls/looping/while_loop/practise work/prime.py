#18.	Accept a number and print whether it's a prime.
num=int(input("enter a number: "))
i=2
count=0
while(i<num):
    if num%i==0:
        count+=1
    i+=1
if(count>=1):
    print("number is not a prime")
else:
    print("Number is prime")