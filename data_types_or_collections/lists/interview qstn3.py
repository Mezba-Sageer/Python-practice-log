#peak value problem
lst=[1,3,6,5,4,3,4,6,8,9,10,11,9,7,6,5,6,8,9,15,14,12,11]
#print the following output: [1,6,3,11,5,15]
#logic behind this question:
#here we print the elements which break the series
lst1=[lst[0]] #this step is to add 1 to the output list.
for i in range(1,len(lst)-1):
#if simply len(lst) it runs from 0th index
#the range is given as index:1 and len(lst)-1 - so that it avoids the number at the first and last index bcz there's
#no numbers bfr the first index and after the last index to compare.
    if(lst[i]>lst[i-1] and lst[i]>lst[i+1]) or (lst[i]<lst[i-1] and lst[i]<lst[i+1]):
    #the above condition is to check if the middle number is greater than the no.s on either side we add it to the list
    #similarly to check if the middle number is less than the no.s on either side we add it to the list.
    #this is bcz that middle number is the starting or end of a series of ascending and descending
        lst1.append(lst[i])
print(lst1)
