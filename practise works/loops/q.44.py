#044
# Ask how many people the user wants to invite to a party.
# If they enter a number below 10, ask for the names and after each name display "[name] has been invited".
# If they enter a number which is 10 or higher, display the message "Too many people".
num=int(input("Enter the no.of ppl you'd like to invite: "))
if(num<10):
    for _ in range(num):
        name=input("Enter the name: ")
        print(name,"has been invited")
else:
    print("Too many people")