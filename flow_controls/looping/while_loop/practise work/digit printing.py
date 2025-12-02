#Accept a number and print its digits (one per line).
n=int(input("Enter a number: ")) #1234
div=1
temp=n
while(temp>10): #1234>10T #123>10T #12T #1>10F
    temp//=10 #1234//10=123 #123//10=12 #12//10=1
    div*=10 #10 #10*10=100 #100*10=1000

while(div!=0): #1000!=0T #100!=0T #10T #1T
    digit=n//div #1234//1000=1 #234//100=2 #34//10=3
    print(digit)
    n=n%div #1234%1000=234 #234%100=34 #34%10=4
    div//=10 #1000//10=100 #100//10=10 #10//10=1



