#to add a new key and value
dic1={'age':21,'name':'Mezba','qualification':'bachelors','salary':30000}
#syntax
dic1['location']='kochi' #step to add a key value pair
print(dic1)

#how to check if a key/value is present in a dictionary
print('age' in dic1) #this checks if a certain key is in dictionary
print('location' in dic1)
print('experience' not in dic1) #return true since there is no experience key in dic1


#how to delete a key value pair in a dictionary
del dic1['qualification']
print(dic1)

