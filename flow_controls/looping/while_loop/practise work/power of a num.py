#24.	Display the power of a number (base^exp) without using **.
base=int(input("Enter the number: "))
exp=int(input("enter the no.of time you want it multiplied: "))
power=1
i=1
while(i<=exp):
    power*=base
    i+=1
print("power of the number is: ",power)