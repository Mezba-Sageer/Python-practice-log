#0
# 0 1
# 0 2 4
# 0 3 6 9
# 0 4 8 12 16

# for i in range(0,6): #i=0 i=1 i=2 i=3
#     for j in range(0,i+1): #j=(0-1) #j=(0-2) #j=(0-3) #j=(0-4)
#         print(j*i,end=' ') #0*0, #0*1, 1*1  #0*2, 1*2, 2*2  #0*3, 1*3, 2*3, 3*3
#     print()

for i in range(0,6):
    for j in range(0,i+1):
        print(j*i,end=" ")
    print()
