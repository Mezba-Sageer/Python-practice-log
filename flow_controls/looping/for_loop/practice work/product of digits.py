#15.	Find the product of all digits in a number input by the user.
n=int(input("Enter a number: "))
temp=n
pro=1
digit_count=0
while(temp!=0): #56 #5
    digit_count+=1 #C=1 #C=2
    temp//=10 #5 #0
for i in range(digit_count):
    digit=n%10
    pro*=digit
    n//=10
print(pro)