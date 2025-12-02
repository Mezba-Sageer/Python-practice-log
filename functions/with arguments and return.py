#count number of digits in a users input
def count(x):
    digit=0
    while(x>0): #if (x=12345)(x>0=T) (x=1234) (x=123) (x=12) (x=1) (1>0=T)
        x//=10 #(x=12345//10=1234) (x=1234//10=123) (x=123//10=12) (x=12//10=1) (x=1//10=0)
        digit+=1 #increment value digit=1 digit=2 digit=3 digit=4 digit=5
    return digit
x=int(input("Enter a number: "))
print("The number of digits is: ",count(x))

#in order to remove each digit from a given input number is to do floor division
#while to store that removed digit we use mod
