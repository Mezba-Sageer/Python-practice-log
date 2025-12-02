#Write a python program to print all  permutations using those three variables
#original collection: [1,2,3]
# Collection of Permutation:
# [3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]
original_lst=[1,2,3]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i!=j) and (i!=k) and (j!=k):
                print(original_lst[i],original_lst[j],original_lst[k])
