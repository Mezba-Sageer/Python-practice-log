#find the odd numbers and find the cube of those odd numbers
lst=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda num:num%2!=0,lst))
cube=list(map(lambda num:num**3,odd))
print(cube)