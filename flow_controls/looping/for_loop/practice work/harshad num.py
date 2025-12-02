#22.Check if a number is a Harshad number
# (divisible by the sum of its digits).
num=int(input("Enter a number: "))
temp=num
sum=0
for i in str(num):
    sum+=int(i)
if(temp%sum==0):
    print(temp,"is a harshad number")
else:
    print("Not a harshad number")

