#3.Filter
#Filter is used when you want to apply a condition to the list to extract only elements which meet that condition
#syntax:
#var_name=list(filter(fn,iterable)
#here fn: is the function which is to be performed to the list
#while iterable is the name of the list on which operations is to be performed
lst=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda num:num%2==0,lst))
print(even)
