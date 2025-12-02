#print the following pattern
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# for i in range(1,5):
#     for s in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()
for i in range(1,5):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(j-1,0,-1):
        print(k,end=" ")
    print()