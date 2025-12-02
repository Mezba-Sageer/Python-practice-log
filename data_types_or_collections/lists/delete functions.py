#how to delete an element
lst=[12,67,89,57,78,35,64,73,97]
#the function used to remove an element from a list - is remove()
#remove() - only removes one element at a time
#inside a remove function we pass the element to delete
lst.remove(12)
lst.remove(35)
print(lst)

#in order to remove multiple values at the same time we use del()
del lst[1:3] #removes values at index 1 and 2
print(lst)

#in order to remove the last value or element from a list we use pop()
lst.pop()
print(lst)
#to delete one specific element from the list using index no.we use pop()
lst.pop(2)
print(lst) #this removes the value given at the index value mentioned

#the difference btw remove() and pop() is that- in remove() the element to be deleted is passed
#while in pop() we pass the index of the element to be deleted

#different methods to remove elements from a list
employee=['Neethu', 'Judy', 'Vipin', 'Anu', 'mezba', 'farsi', 'Mirzan', 'Afthab','Pooja','Sany','Joe','Ziya']

#using del keyword:
del employee[0:3]
print(employee)

#using remove()
employee.remove("Mirzan")
employee.remove("Python") #this is a value error since it's not there in the list
print(employee)

#using del keyword without the index values
del employee #delete the entire list
print(employee)

#using clear()
employee.clear() #output: is a list cleared off all the elements inside the list
print(employee)