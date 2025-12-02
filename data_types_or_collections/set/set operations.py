#different types of set operations
#1.union
#2.Intersection
#3.Difference
st1={1,2,3,4,5,6,7,8,9,10}
st2={5,6,7,8,9,10,11,12,23,35}

#1.union -
#combining 2 sets into 1 single set(or result) is referred as union without duplicates.
st3=st1.union(st2)
print(st3) #prints the elements in both lists without duplicates

#2.intersection-
#collects the common elements within 2 lists
st4=st1.intersection(st2)
print(st4) #prints the common elements in both sets

#3.difference:
#elements in set1 - set2 gives elements in set 1 which is not present in set2
#set2 - set1 gives elements in set 2 which is not present in set1
st5=st1.difference(st2)
print(st5) #only prints elements from set 1 which is not present in set 2.
st6=st2.difference(st1)
print(st6) ##only prints elements from set 2 which is not present in set 1.