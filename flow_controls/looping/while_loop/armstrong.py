#armstrong number
#eg:153= 1^3+5^3+3^3
#eg: 1234: 1^4+2^4+3^4+4^4
n=int(input("Enter a number: "))
temp=n
temp2=n
sum=0
count=0
#code to find the no.of digits
while(temp2!=0): #153
    temp2//=10 #15
    count+=1
#code to find if the user input is an armstrong number
while(n!=0): #conditional loop
      x=n%10
      sum+=x**count
      n//=10
if(sum==temp):
    print(temp,"is an armstrong")
else:
    print(temp,"is not armstrong")
