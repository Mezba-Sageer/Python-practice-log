#17.	Find the product of digits of a number.
num=int(input("enter a num: "))
product=1
while(num!=0):
    digits=num%10
    product*=digits
    num//=10
print(product)
