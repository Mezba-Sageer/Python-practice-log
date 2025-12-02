#13.	Print a diamond pattern of stars for an odd number input:
#   *
#  ***
# *****
#  ***
#   *
for i in range(1,6):
    for s in range(3-i):
        print(" ",end=" ")
    if(i%2==1):
        for j in range(i):
            print("*",end=" ")
        print()
for i in range(3,0,-2):
    for s in range((5-i)//2):
      print(" ",end=" ")
    if(i%2==1):
        for j in range(i):
            print("*",end=" ")
        print()

