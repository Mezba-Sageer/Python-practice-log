#armstrong number
num=int(input("Enter a number: "))
temp=num
temp2=num
digit=0
armstrong=0
while(num>0): #153T #15 #1
    digit+=1 #1 #2 #3
    num //= 10  # 15 #1 #0
while(temp>0):
       last_digit=temp%10
       armstrong+=last_digit**digit
       temp//=10
if(temp2==armstrong):
    print("number is armstrong")
else:
    print("not armstrong")



