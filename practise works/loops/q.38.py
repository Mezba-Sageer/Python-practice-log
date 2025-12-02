#038
# Change program 037 to also ask for a number.
# Display their name (one letter at a time on each line) and repeat this for the number of times they entered.
name=input("enter your name: ") #eg:mez
num=int(input("enter a number: ")) #eg:5
i=1
while(i<=num): #1<=5 T 2<=5T
    index = 0 #this is set to 0 inside a loop to ensure that it resets to 0 bfr it runs the 2nd loop
    while(index<len(name)): #0<3 T 1<3T 2<3T
        print(name[index]) #m e z
        index += 1
    i+=1




