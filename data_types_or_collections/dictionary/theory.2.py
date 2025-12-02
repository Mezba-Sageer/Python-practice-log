#how to collect a "value" in a dictionary
#in order to collect a value from a dictionary we use the key of the value and not the index number
dic1={'age':21,'name':'Mezba','qualification':'bachelors','salary':30000}

#syntax for collecting values within a dictionary:
print(dic1['age']) #here the key acts as almost like an index
print(dic1['name'])


#how to iterate a dictionary or collect each element at a time - i.e to get key and value at the same time the syntax
#is the following
#we use a for loop for that:
for i in dic1:
    #print(i) - this prints only the key name
    print(i,dic1[i]) #this prints both the value and key within a dictionary
    #i collects the "key", dic_name[i] collect the corresponding value of key

#how to update values within a dictionary
#syntax:
dic1['age']=30 #this is how u change values
dic1['qualification']="Post graduate"
dic1['salary']+=500
print(dic1['age'])
print(dic1['qualification'])
print(dic1['salary'])

