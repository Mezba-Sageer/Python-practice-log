#2.Map
#Map is applied when you want a corresponding output for each element within a list.
#syntax: var_name=list(map(fn,iterable)
#eg:
#find the square of all elements within a list
lst=[1,2,3,4,5,6,7,8,9,10]
def square(num): #this is the function created to perform the task to find the square
    return num**2
f=list(map(square,lst))
print(f)

#another method to find square
#lambda num:num**2 #this whole line can be passed as function  name too.