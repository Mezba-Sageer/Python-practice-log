#32.	Accept a number and use /= to halve it until it’s less than 1.
num=int(input("Enter a number: "))
while(num>1):
     num/=2
     print("the half is",num)
