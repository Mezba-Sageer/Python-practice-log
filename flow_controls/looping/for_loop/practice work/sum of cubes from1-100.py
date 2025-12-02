# 1.	Sum of cubes of odd numbers from 1 to 100.
sum=0
for i in range(1,101):
    if(i%2!=0):
        sum+=i**3
print("Sum of cubes of odd numbers from 1-100 is: ",sum)
