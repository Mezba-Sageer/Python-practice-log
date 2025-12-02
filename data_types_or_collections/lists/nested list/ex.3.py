#print the details whose age is working in big data profession,only the following details: fname,lname,age

lst=[[1,"Mez","sageer",21,"bigdata",50000],[2,"aryan","nair",31,"python",150000],[3,"farseena","azies",29,"python",250000],
     [4,"Afthab","Rahman",30,"bigdata",50000]]

for i in lst:
    if(i[4]=="bigdata"):
        print(i[1:4])


#similarly print the details of the people in python profession, the details: fname,age,salary
for j in lst:
    if(j[4]=="python"):
        print(j[1:6:2]) #in this the range can also be passed as [1::2]