#print the details whose age is above 29,only the following details: fname,lname,age,profession

lst=[[1,"Mez","sageer",21,"python",50000],[2,"aryan","nair",31,"python",150000],[3,"farseena","azies",29,"python",250000],
     [4,"Mez","sageer",30,"python",50000]]

for i in lst:
    if(i[3]>29): #age is in the 3rd index and i is the elements/lists within the parent list
        print(i[1],i[2],i[3],i[4])
        print(i[1:5]) #instead of passing each index num, we can also pass the slicing range which is easier
