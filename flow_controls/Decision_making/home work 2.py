#calculate age - by comparing year,month and date
#input:-
#current_year
#current_month
#current_date

#birth year
#birth month
#birthdate

#using nested if
current_yr=int(input("Enter the current year: ")) #2025
current_mnth=int(input("Enter the current month: ")) #5
current_date=int(input("Enter the current date: ")) #28
brth_yr=int(input("enter your birth year: ")) #2003
brth_mnth=int(input("Enter your birth month: ")) #7
birth_date=int(input("Enter you birth date: ")) #19

age=current_yr-brth_yr #2025-2003 = 22

if(current_mnth<brth_mnth): #5<7 T
    age-=1 #22-1=21
    print(age)

elif(current_mnth==brth_mnth): #5=5 T (suppose birth month is 5)
    if(current_date<birth_date):
        #(if birthdate is 30 and current date is 28) i.e 28<30 in may
        age-=1

print("your current age is",age)
