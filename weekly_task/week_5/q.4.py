#4. Write a program that prints the sum of all positive numbers in a list using
# a for loop and continue statement.
lst1=[1,-8,-3,56,7,-6,-12,10,22,25]
sum=0
for i in lst1:
    if(i<0):
        continue
    else:
        sum+=i
print(sum)
