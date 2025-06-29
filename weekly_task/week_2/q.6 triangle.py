#Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
s1=int(input("Enter the value of first side: "))
s2=int(input("Enter the value of second side: "))
s3=int(input("Enter the value of third side: "))
if(s2==s1==s3):
    print("It is an equilateral triangle")
elif(s1==s2 or s1==s3 or s2==s3):
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")
