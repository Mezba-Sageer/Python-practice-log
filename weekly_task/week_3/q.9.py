#count the total number of digits in a number
num=int(input("Enter a number: "))
temp=num
count=0
while(num!=0): #153 #15
    num//=10 #15 #1
    count+=1
print(temp,"has",count,"digits")
