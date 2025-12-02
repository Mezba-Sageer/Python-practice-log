#Write a program to accept a number and check whether its a perfect number or not.
# Perfect number is a number which is equal to sum of its divisors.
# For ex: 6, its divisors are 1,2,3. So sum of divisors 1+2+3 is also 6

num=int(input("enter a number: ")) #6
temp=num #6
i=1
sum=0
while(i<num): #1<6T
    if(num%i==0): #6%1==0
        sum+=i #1
    i+=1
if(temp==sum): #
    print(temp,"is a perfect number")
else:
    print(temp,"not a perfect number")
    