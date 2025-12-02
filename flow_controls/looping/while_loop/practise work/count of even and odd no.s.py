#38.	Accept numbers until user enters “stop” and display count of even and odd numbers.
even=0
odd=0
while(True):
    num1=input("Enter a number to continue or enter stop: ").lower()
    if(num1=="stop"):
        break
    else:
        num=int(num1)
        if(num%2==0):
            even+=1
        else:
            odd+=1
print("the count of even number is: ",even)
print("the count of odd number is: ",odd)
