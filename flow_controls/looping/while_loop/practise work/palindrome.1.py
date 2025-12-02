#14.	Check if a number is a palindrome.
num=int(input("Enter a number: "))
rev=0
temp=num
while(num!=0):
    digit=num%10
    rev=rev*10+digit
    num//=10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")