#Write a program to check whether a given year is leap year or not.
year=int(input("enter an year: "))
if(year%4==0):
    if(year%100!=0 or year%400==0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
else:
    print("The year is not a leap year")