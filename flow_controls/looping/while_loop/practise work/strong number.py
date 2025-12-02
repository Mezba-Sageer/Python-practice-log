#30.Accept a number and check if it’s a strong number (sum of factorial of digits equals number).
num=int(input("enter a number: ")) #145
temp=num #temp=145
sum=0
while(num!=0): #145!=0
    fact=1
    i=1
    rem=num%10 #145%10=5
    while(i<=rem): #1<=5T #2<=5T #3<=5T #4<=5T #5=5T
        fact*=i #factorial: #1 #2 #2*3=6 #6*4=24 #24*5=120 #similarly for 4=24 #for 1=1
        i+=1
    sum+=fact #120+24+1=145
    num//=10
if(temp==sum):
    print("It's a strong number")
else:
    print("It's not a strong number")


