#21.	Keep asking the user to enter positive numbers; stop on negative and print the average.
num=int(input("Enter a positive number: "))
count=0
sum=0
while(num>0):
    sum+=num
    count+=1
    num = int(input("Enter a positive number: "))
avg=sum/count
print(avg)
