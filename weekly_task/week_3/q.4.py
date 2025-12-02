#python program to check if a given no. is armstrong
num=int(input("Enter a number: "))
temp=num
temp2=num
count=0
sum=0
while(temp!=0): #153 #15
    temp//=10 #15 #1
    count+=1 #1,2
while(temp2!=0):
    digit=temp2%10
    sum+=digit**count
    temp2//=10
if(num==sum):
    print("Armstrong")
else:
    print("not armstrong")

