#print the following pattern :
#        1
#      2 3
#    4 5 6
# 7 8 9 10
num=1
for i in range(1,5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
