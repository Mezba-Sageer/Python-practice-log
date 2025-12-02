#search an element using binary search algorithm
#in this method we keep changing the range until the search element becomes equal to middle index value
lst=[1,34,2,56,4,54,8,9,11,31,46,78]
num=int(input("Enter an element to search: "))
lst.sort()
low=0
upper=len(lst)-1
flag=0
while(low<=upper):
#for loop is not used to avoid going through each element in a list
#while loop doesn't involve goin thro each element but rather using index no.and ranges
    mid=(low+upper)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upper=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("Element not found")
