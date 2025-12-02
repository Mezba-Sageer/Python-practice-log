#print the details whose age is 29

lst=[[1,"Mez","sageer",21,"python",50000],[2,"aryan","nair",29,"python",150000],[3,"farseena","azies",29,"python",250000],
     [4,"Mez","sageer",30,"python",50000]]
#age equal to 29
for i in lst:
    if(i[3]==29): #age is in the 3rd index and i is the elements/lists within the parent list
        print(i) #we are printing the list which contains the details of ppl hu are 29

