#set
#1.how to define:
#to create an empty list we use - 'set()'
#but values passed inside a {1,2,3} - this is read as a set
#but empty '{}' brackets is for creating an empty dictionary.
st={10,20,30,40,50} #this is a set
print(st)
#2.insertion order
#the insertion order of a list is not preserved - i.e the output isn't in the same order as the input-drawback

#3.Heterogenous data
st1={10,10.5,True,False,"Mez"}
print(st1)
#set supports heterogenous data,i.e supports all types of data

#4.Duplicate support
st2={10,10,20,20,True}
print(st2)
#do not support duplicate values only prints a value once
#another example:
st3={0,1,True,False}
print(st3)
#this returns only 0 and 1 as output since set doesn't support duplicates.

#5.Mutable or Immutable
#set is mutable - we can change the values within a set
