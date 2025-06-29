#Accept the age, sex(‘M’&’F’), number of days and display the wages accordingly.
age=int(input("Enter the age: "))
sex=input("male or female: ").upper()
days=int(input("Enter the no.of days: "))
if(18<=age<30):
    if(sex=="MALE" or sex=="M"):
        print("Wage is ",700*days)
    elif(sex=="FEMALE" or sex=="F"):
        print("Wage is ",750*days)
    else:
        print("Invalid input")
elif(30<=age<=40):
    if(sex=="MALE" or sex=="M"):
        print("Wage is ",800*days)
    elif(sex=="FEMALE" or sex=="F"):
        print("Wage is ",850*days)
    else:
        print("invalid input")
else:
    print("No wage")

