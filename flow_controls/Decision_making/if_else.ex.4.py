#bonus 5% - if experience>5

# yr_exp=int(input("Enter your year of experience"))
# salary=int(input("Enter your year of salary"))
# if(yr_exp>=5):
#     net_bonus=salary*0.05 #or (salary*5)/100
#     print("your net bonus is",net_bonus)
# else:
#     print("no bonus")

yoe=int(input("Enter you year of experience: "))
salary=int(input("Enter your salary: "))
if(yoe>=5):
    bonus=salary*0.05
    print("Your current salary is: ",salary+bonus)
    print("Your bonus is: ",bonus)
else:
    print("Your salary is: ",salary)