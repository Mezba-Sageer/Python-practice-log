#Insertion functions
st={10,32,45,56,86,97,45,1,23,95,101,10}

#to add new elements functions used:

#1. to add elements one at a time - add() #we cannot add duplicate elements into the list using any function
st.add(64)
print(st)

#2.to add multiple elements we use - update()
st.update([12,34,80,19])
print(st)

#we cannot add any elements to a particular index since the insertion order is not preserved
