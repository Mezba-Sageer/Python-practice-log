#create a new list without the duplicates
lst=[10,10,50,80,70,60,50,40,40,30,10,100]
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)
print(lst2)
#here we check if new list has the element in 1st list if not we append it into the list else we don't
#this way we get a new list without any duplicates
