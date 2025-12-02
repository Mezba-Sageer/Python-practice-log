#049
# Create a variable called compnum and set the value to 50.
# Ask the user to enter a number. While their guess is not the same as the compnum value,
# tell them if their guess is too low or too high and ask them to have another guess.
# If they enter the same value as compnum, display the message "Well done, you took [count) attempts".

compnum=50
num=int(input("Enter a number: "))
count=1
while(num!=compnum):
    if(num>compnum):
        print("your guess is too high")
        num=int(input("Take another guess: "))
    else:
        print("your guess is too low")
        num=int(input("Take another guess: "))
    count += 1

print("well done, you took",count,"attempts")

