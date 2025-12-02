#22.	Accept an employee's salary and increase it by 10% if less than ₹50,000; else by 5%.
salary=int(input("Enter your salary: "))
if(salary<50000):
    increment=salary*0.1
    print("new salary is: ",salary+increment)
else:
    increment=salary*0.05
    print("New salary is: ",salary+increment)