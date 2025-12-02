#create an empty list and add 1-100 elements
#from the abv list add the even numbers and odd numbers to a new separate list
#and find the sum of all 3 lists
lst1=[]
lst2=[]
lst3=[]
for i in range(1,101):
    lst1.append(i)
    if i%2==0:
        lst2.append(i)
    else:
        lst3.append(i)
print("list 1: ",lst1)
print("even list: ",lst2)
print("odd list: ",lst3)
print("sum of 1st list: ",sum(lst1))
print("sum of even list: ",sum(lst2))
print("sum of odd list: ",sum(lst3))

