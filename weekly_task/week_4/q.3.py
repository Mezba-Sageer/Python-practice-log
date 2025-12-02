#3: print the following pattern
#* * * *
#* * *
#* *
#*
#* *
#* * *
#* * * *

# for i in range(1,5):
#     for j in range(4,i-1,-1):
#         print("*",end=" ")
#     print()
# for i in range(1,4): #i=1 i=2
#     for j in range(0,i+1): #(0,2) output 2 stars (0,3) #print 3 stars
#         print("*",end=" ")
#     print()
for i in range(1,5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()
for i in range(1,4):
    for j in range(1,i+2):
        print("*",end=" ")
    print()