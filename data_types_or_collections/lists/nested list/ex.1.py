#nested list is something where we can pass a list inside another list - very important
#eg:
lst=[["mezba","sageer",21,"graduated","jobless"],["jude ","alron",22,"starting school"],
     ["afthab","rahman",21,"pg"],["farsee","azies",21,"diploma"]]
print(lst)
print()
print(lst[3])
print()

#in this example each list is passed as one single element
#this is referred to as nested list. list within a list
#in total there are 4 elements
#and 4 elements are passed as lists
#in order to get each list within that list printed just print it using for loop
#i.e each list has it's own index no.
for i in lst:
    print(i)