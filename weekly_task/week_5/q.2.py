#2. Write a program that iterates over a list of integers and breaks the loop when a negative number is encountered.
num=[]
n=int(input("Enter the number of elements you'd like to add to the list: "))
for i in range(n):
    num2=int(input("Enter a number: "))
    num.append(num2)
for i in num:
    if(i<0):
        break
    print(i)
