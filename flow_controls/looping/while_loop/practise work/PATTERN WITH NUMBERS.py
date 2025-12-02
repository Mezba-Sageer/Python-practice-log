#print a pyramid pattern with numbers using while loop
#           1
#         1   2
#       1   2   3
#     1   2   3   4
#    1  2   3   4   5
i=1
rows=5

while(i<=rows):
    space=1
    while(space<=rows-i):
        print(" ",end=" ")
        space+=1
    j=1
    while(j<=i):
        print(j," ",end=" ")
        j+=1
    print()
    i+=1


