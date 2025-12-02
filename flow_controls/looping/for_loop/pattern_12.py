# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0
# for i in range(6,0,-1): #i=6 i=5 i=4 i=3 i=2 i=1
#     for j in range(0,i): #j(0,6(prints 0-5)) #j(0,5) #j(0,4) #j(0,3) #j(0,2) #j(0,1)
#         print(j,end=' ') #0 1 2 3 4 5
#                          #0 1 2 3 4
#     print()
for i in range(5,-1,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print()
