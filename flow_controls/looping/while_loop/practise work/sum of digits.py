#15.	Find the sum of digits of a number.
num=int(input("enter a number:" ))
sum=0
temp=num
div=1
while(num>10): #1234>10 #123>10 #12>10
    num//=10 #123 #12 #1
    div*=10 #div=10 #div=100 #div=1000
print(div)
while(div!=0):
    digit=temp//div
    sum+=digit
    temp%=div
    div//=10
print(sum)
