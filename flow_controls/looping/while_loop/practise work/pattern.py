#32.	Print a pattern like:
# *
# **
# ***
# ****
i=1
while(i<5): #1<5T
    j = 1
    while(j<=i):
        print("*",end="") #*
        j+=1
    print()
    i+=1