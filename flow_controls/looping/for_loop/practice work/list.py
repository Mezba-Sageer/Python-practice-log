#18.	Accept a list and print all elements that occur more than once.
lst=[1,2,3,4,5,6,7,8,2,3,5,2,5,2,6,9,10]
lst2=[]
duplicates=set()
for i in lst:
    if i not in lst2:
        lst2.append(i)
    else:
        duplicates.add(i)
print(duplicates)


