#1st method:
#1st methods includes adding a range of elements into a list without any conditions.
#the method below is the traditional methond for adding elements into a list
# lst=[]
# for i in range(1,21):
#     lst.append(i)
# print(lst)

#the method below can also be used to add elements into a list
lst=[i for i in range(1,21)]
print(lst)
#the traditional method which took 3 steps to add the range can be simplified into 1 step
#print elements from 10-30
lst1=[j for j in range(10,31)]
print(lst1)
#basically syntax is:
#var_name=[element to print loop]
#element to print here is the iterating variable
