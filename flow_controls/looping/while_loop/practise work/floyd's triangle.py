#33.	Print Floyd’s Triangle using a while loop.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
i=1
num=1
while(i<=5): #1<=5T #2<=5T
    j=1
    while(j<=i): #0<1T #
        print(num,end=" ") #1
        num+=1
        j+=1
    print()
    i+=1