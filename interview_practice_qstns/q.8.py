#A school has asked you to write a program that will calculate teachers' salaries.
# The program should ask the user to enter the teacher's name, the number of periods taught in a month,
# and the rate per period. The monthly salary is calculated by multiplying the number of periods by the monthly rate.
# The current monthly rate per period is $20. If a teacher has more than 100 periods in a month,
# everything above 100 is overtime. Overtime is $25 per period. For example, if a teacher has taught 105 periods,
#their monthly gross salary should be 2,125. Write a function called your_salary that calculates a teacher's gross salary.
# The function should return the teacher's name, periods taught, and gross salary. Here is how you should format your output:
def your_salary(tchr_name,no_of_periods):
    if(no_of_periods<=100):
        gross_salary=no_of_periods*20
    else:
        overtime=no_of_periods-100
        gross_salary=100*20+overtime*25
    # print("Teacher's name is: ",tchr_name)
    # print("The number of periods taught is: ",no_of_periods)
    # print("Your monthly salary is: ",gross_salary)
    return f"Teacher's name: {tchr_name}\nPeriods taught: {no_of_periods}\nYour monthly salary: {gross_salary}"
tchr_name=input("Enter the teacher's name: ")
no_of_periods=int(input("Enter the number of periods taught: "))
print(your_salary(tchr_name,no_of_periods))
