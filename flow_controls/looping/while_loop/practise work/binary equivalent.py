#26.	Accept a number and print its binary equivalent using a while loop.
num=int(input("Enter a number: "))
binary=""
while(num!=0): #10
    reminder=num%2
    binary=str(reminder)+binary
    num//=2
print(binary)