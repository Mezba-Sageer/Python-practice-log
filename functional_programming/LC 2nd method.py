#syntax: var_name=[print_item range condition]

#to print even numbers within the range of 1-10
lst=[i for i in range(1,21) if i%2==0]
print(lst)


#to print odd number from 1-50
lst2=[j for j in range(1,51) if j%2==1]
print(lst2)

#print the square of even numbers from 1-30
lst3=[(k,k**2) for k in range(1,31) if(k%2==0)]
print(lst3)

#print the cube of odd numbers and element in the range of 1-25
lst4=[(i,i**3) for i in range(1,26) if i%2==1]
print(lst4)