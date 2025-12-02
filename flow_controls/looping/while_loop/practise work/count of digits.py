#12. Count the number of digits in a given number.
num=int(input("Enter a num: "))
count=0
while(num!=0):
    num//=10
    count+=1
print(count)