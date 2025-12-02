#first add 1-20 to an empty list
#and then add cube of each elements into a new list
lst=[]
cube_lst=[]
for i in range(1,21):
    lst.append(i)
for j in lst:
    cube_lst.append(j**3)
print(lst)
print(cube_lst)
