#23.	Accept a number and find its HCF and LCM with another number.
num1=int(input("enter a number: "))
num2=int(input("Enter another number: "))
a=num1
b=num2
hcf=0
if(num1>num2):
    lowest=num2
else:
    lowest=num1
i=1
while(i<=lowest):
    if(num1%i==0) and (num2%i==0):
        hcf=i
    i+=1
print("hcf is: ",hcf)
if(a>b):
    greatest=a
else:
    greatest=b
while(True):
    if(greatest%a==0 and greatest%b==0):
        lcm=greatest
        break
    greatest+=1
print("LCM is: ",lcm)




