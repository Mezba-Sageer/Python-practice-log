#read an element from the user and check if that element is present inside the list and print "found" if present
#linear search algorithm - comparing each element in a list with the element to be searched
#the method applied below is linear search algorithm
#drawback of this method - time complexity is high in order to overcome this we use binary search algorithm
lst=[12,56,73,87,90,35,65,43,89]
num=int(input("Enter a number: "))
flag=0
for i in lst:
    if(i==num):
        flag=1
if(flag>0):
    print("found")
else:
    print("not found")

