#23.From a list of numbers, find the count of numbers that have more than two digits.
lst=[12,94,57,384,47,49,4,203,4839,143]
count_of_num=0
for i in lst:
    if(len(str(i))>2):
        count_of_num+=1
print("Count of numbers with more than 2 digits is: ",count_of_num)


