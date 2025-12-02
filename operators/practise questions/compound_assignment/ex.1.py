#31.	Accept a number and use *=2 in a loop to double it 3 times.
num=int(input("Enter a number: "))
i=1
while(i<=3):
    num*=2
    i+=1
print("the doubled value is: ",num)