#calculate road tax of bike

#above 1 lakh  - 15% road tax
#50k-1 lakh - 10% road tax
#below 50k - 5%
price=int(input("Enter the price of the bike: "))
if(price>100000):
    tax=(15/100)*price
elif(50000<=price<=100000):
    tax=(10/100)*price
else:
    tax=(5/100)*price
print("the tax amount is",tax)

#can avoid entering print statement in each if block


