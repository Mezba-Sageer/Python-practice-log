#24.Find the common elements in two lists without using set operations.
list1 = [3, 7, 12, 9, 5, 18, 20, 25, 30]
list2 = [4, 9, 12, 20, 33, 7, 40, 50]
for i in list1:
    for j in list2:
        if i==j:
            print(i)