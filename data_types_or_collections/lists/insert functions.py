#to insert an element into a list using the append()
lst=[]
lst.append(50)
lst.append(87)
lst.append(76)
lst.append(15)
print(lst)
#append() - can be used to add only one element at a time


#extend() is used to add multiple values
lst.extend([12,65,46,35,47])
print(lst)

#insert() is used to add a value at a particular position
lst.insert(1,12) #12 is added to the first index
print(lst)

#study difference btw all 3

#methods to insert a new element into a list- string version
list1=["Neethu","Vipin","Anu","mezba","farsi","Mirzan"]

#1: insert()
list1.insert(1,"Judy")
print(list1)

#2: append()
list1.append("Afthab") #we can add only one element at a time to the last index of the list
print(list1)

#3: extend()
list1.extend(["Pooja,Sany,Joe,Ziya"])
#using extend function within square brackets we can add multiple elements
#when the '[]' is not applied each letter of the whole string is added to the list separately
#adds a list to the last index i.e is the difference btw extend() and append()
print(list1)