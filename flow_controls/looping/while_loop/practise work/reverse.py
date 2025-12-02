#reverse a number
num=int(input("Enter a number: "))
rev=0
while(num!=0): #153 #15 #1
    digit=num%10 #3 #5 #1
    rev=rev*10+digit #0*10+3=3 #3*10+5=35 #350+1=351
    num//=10 #15 #1 #0

