#different functions to remove elements from a set
st={10,32,45,56,86,97,45,1,23,95,101,10}

#remove function - removes the element mentioned within the function brackets
st.remove(10)
print(st)

#how to delete multiple elements within a set
#difference_update()
st.difference_update({32,56,86})
print(st)
#we can also add the elements to deleted into a list and use a for loop to iterate thro tht list and use
#discard() to delete those elements from the set

#pop()- this removes some random element from the set not the last element specifically bcz of the insertion order
st.pop()
print(st)

#discard()
#to remove an element within a set, that too without showing an error message when that element is not
#present within the list we use discard().
#the key difference is that unlike other removing/deleting functions discard() doesn't return error if we have to
#remove a value that is not present within the set.
st.discard(200) #this value is not there in the set bt this doesn't return error
print(st)

