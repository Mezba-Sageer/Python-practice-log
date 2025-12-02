#print pattern
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# for i in range(1,6): #i=1 2 3
#     for j in range(i,6) #j(1,6) j=1 2 3 4 5 #j(2,6) j=2 3 4 5 #j(3,6) j=3 4 5
#         print(i,end=' ') #1 1 1 1 1
#                          #2 2 2 2
#                          #3 3 3
#     print()
for i in range(1,6):
    for j in range(i,6):
        print(i,end=" ")
    print()