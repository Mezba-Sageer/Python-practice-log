#swapping of numbers - with the use of a third variable
num1=10
num2=20


print("Before Swapping")
print("Number 1 is",num1)
print("Number 2 is",num2)

temp=num1 #assign num1 value to a temporary variable
num1=num2 #num1=num2 i.e num1=20 now
num2=temp #num2=temp in order to assign 10 to num2 for swapping

print("After Swapping")
print("Number 1 is",num1)
print("Number 2 is",num2)


