#5.	Count how many numbers between 1 and 1000 are divisible by 7 but not by 5.
count=0
for i in range(1,1001):
    if(i%7==0 and i%5!=0):
        count+=1
print("Count of numbers divisible by 7 and not by 5 are: ",count)
