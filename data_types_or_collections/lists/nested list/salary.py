#total salary of all employees in a list
lst=[[1,"Mez","sageer",21,"python",50000],[2,"aryan","nair",29,"python",150000],[3,"farseena","azies",29,"python",250000],
     [4,"Mez","sageer",30,"python",50000]]
salary=0
for i in lst:
    salary+=i[5]
print(salary)