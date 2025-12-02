#theory
#method 3 is used when there is more than one condition is to be met.
#syntax if there's only 2 conditions
#var_name=[print1 if condition 1 else print2 range] #this is if else syntax

#syntax in case of multiple conditions
#var_name=[print1 if condition1 else print2 if condition2 else print3 range] #syntax for if elif else condition

#qstn: in 1-25 range if the number is even print square, else print cube of the odd numbers along with the element
lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,26)]
print(lst)

#qstn2: in 1-15 range if the number is even print "even" if odd print "odd" with element
lst2=[(i,"even") if i%2==0 else (i,"Odd") for i in range(1,16)]
print(lst2)