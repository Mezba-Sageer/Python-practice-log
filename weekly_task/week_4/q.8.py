#print the following pattern:
#5 5 5 5 5
#5 5 5 5
#5 5 5
#5 5
#5
for i in range(1,6): #i=1 #i=2 #i=3
    for j in range(5,i-1,-1): #j=5-0 output:5 times
                              #j=5 to 2-1= 5-1 output:4 times
                              #j=5 to 3-1= 5-2 output:4 times
                              #j=5 to 4-1= 5-3 output:4 times
                              #j=5 to 5-1=(4) = 5-4 output:4 times
        print("5",end=" ")
    print()
