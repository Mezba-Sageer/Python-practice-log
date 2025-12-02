#19.	Print a hollow square pattern of given size:
#*****
#*   *
#*   *
#*   *
#*****
#method 1: my logic
for i in range(1,6):
    if i==1 or i==5:
        print("*"*5)
    elif(i==2 or i==3 or i==4):
        print("*"+" "*3+"*")
#method 2:
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end="")
        else:
           print(" ",end="")
    print()