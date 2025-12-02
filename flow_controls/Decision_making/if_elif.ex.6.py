#calculate electricity bill
#units
#first 100 units- no payment
#101-200 units- 1unit = 5 rupees
#abv 200 units - 1 unit= 10rupees

#method1
units=int(input("Enter the units of electricity used: "))
if(units<=100):
    pay=0
elif(units>100&units<=200):
    pay=(units-100)*5
else:
    pay=(units-200)*10+500

print("the payment is",pay)






