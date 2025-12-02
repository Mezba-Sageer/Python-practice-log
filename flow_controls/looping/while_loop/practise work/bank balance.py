#37.	Simulate a bank ATM where balance is updated and loop continues until user exits.
#Starts with a predefined balance (e.g., ₹10,000).
# Asks the user to choose from:
# Check balance
# Deposit
# Withdraw
# Exit
# Updates the balance after each operation.
# Continues until the user selects Exit.
balance=10000
while(True):
    print("Choose from the below options: ")
    print("1. Check balance ")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Exit ")
    option = int(input("Enter your choice(1/2/3/4): "))
    if(option==1):
        print("your current balance is: ",balance)
        print()
    elif(option==2):
        deposit=int(input("Enter the amount you'd like to deposit: "))
        balance+=deposit
        print("You have deposited",deposit,"rupees")
        print()
    elif(option==3):
        withdraw=int(input("Enter the amount to withdraw: "))
        if(withdraw>balance):
            print("Insufficient balance")
        elif(withdraw<=0):
            print("Enter a valid amount")
        balance-=withdraw
        print("You have withdrawn",withdraw,"rupees")
        print()
    elif(option==4):
        print("you've chosen to exit")
        break
    else:
        print("enter a valid choice")
        print()

