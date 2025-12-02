#interview question: update the value 30 to 100
tu=(10,20,30,40,50)
#since tuple is immutable we have to convert the tuple into list
#make the changes to the value using index and then convert back to tuple
lst=list(tu) #list() is used to convert tu into list
lst[2]=100 #changes the value 30 to 100 using index
tu=tuple(lst) #using tuple () we convert the list into tuple
print(tu) #prints a tuple with the changed value
