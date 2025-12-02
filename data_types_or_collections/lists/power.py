#print the element of the list, where 1st element *1, 2nd*2,3rd*3......eg:[1**1,5**2,9**3,4**4,3**5......]
#print the power of each element - power starting from 1 from the first element and the power later on incrementing
lst=[1,5,9,4,3,7,8,9,10]
num=1
for i in lst:
    print(i**num)
    num+=1


