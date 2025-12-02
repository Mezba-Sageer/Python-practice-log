#38.	Accept an amount and apply discount only if amount > 1000 and customer is a “member”.
amount=int(input("Enter the amount: "))
membership=input("Are you a member or not(yes/no): ").lower()
if(amount>1000 and membership=="yes"):
    discount=amount*0.1
    final_amt=amount-discount
    print("price after discount is: ",final_amt)
else:
    print("no discount",amount)

    