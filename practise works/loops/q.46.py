#046
#ask the user to enter a number.Keep asking until they enter a value over 5 and then display the message
#"The last number you entered was a [number]" and stop the program
num=int(input("Enter a number: "))
while(num<=5): #1<=5 T 2<=5T
    num=int(input("Enter another number: ")) #eg:2
print("The last number you entered was",num)



