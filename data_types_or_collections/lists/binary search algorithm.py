#binary search algorithm
#steps to follow:
#lst=[79,1,3,57,87,45,2,5,6,56,84]
#1.sort a list in ascending order
#2.declare 2 variables low and upper- and assign them the index value of the first and last elements respectively
#low=0 and upper=len(lst)-1
#3.calculate the mid index of the list- (low+upper//2) eg:(0+8//2)=4th index
#4.check 3 conditions
#a)element>lst[mid] ==> if true we change - low=mid+1
#b)element<lst[mid] ==> if true we change - upper=mid-1
#c)element==lst[mid] ==> if true- output: "Element found"

