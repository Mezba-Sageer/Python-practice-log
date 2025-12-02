#reverse a number 569 eg:965
num=int(input("Enter a number")) #569
rev=0
while(num>0): #num!=0 - this code can also be used #569>0 56>0 T
    num2=num%10 #9 569/10=9 is the remainder 56%10=6
    rev=rev*10+num2 #0*10+9=9 9*10+6= 96
    num//=10 #increment 569/10=56 is the answer 56*10=560 56/10=5
print(rev)



