#6.	Given a list of integers, print only those numbers which are palindrome.
for i in range(1,1001):
    rev=0
    temp=i
    while(temp>0):
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if(rev==i):
        print(i)