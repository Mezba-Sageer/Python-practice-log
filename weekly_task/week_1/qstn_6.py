# Write a program that takes inputs from user and prints the
# multiplication table of that number
num=int(input("Enter a number: "))
for i in range(1,11):
    print(i,"*",num,"=",i*num)
    