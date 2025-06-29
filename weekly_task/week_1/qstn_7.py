#10. Swap the values of two variables x and y without using a temporary variable
# (use arithmetic operators).
x=int(input("Enter a number 1: "))
y=int(input("Enter no.2: "))
print("X and Y before swapping: ")
print("x=",x)
print("y=",y)
sum=x+y
x=sum-x
y=sum-y
print("X and Y after swapping: ")
print("x=",x)
print("y=",y)
