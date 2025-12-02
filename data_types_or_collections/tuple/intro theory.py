#tuple - 5 properties

#1. symbol or function used to define a tuple
#syntax- variable_name=() - we use paranthesis to define a tuple
#eg:
tu=()
print(type(tu)) #output shows that it is a tuple
tu1=tuple() #we can also use the tuple() - also known as tuple function to define a tuple


#2.supporting data type
#a tuple supports all types of data hence: tuple supports hetrogenous data
#eg:
tu2=(10,20,5,'bigdata','python',True,False,10.5)
print(tu2)


#3.supporting of duplicate data
#tuple supports duplicate values
tu3=(10,5,5,'bigdata','python',True,True,False,10.5)
print(tu3)


#4.insertion order is preserved/or not
#tuple's insertion format is preserved bcz the output is in the same order as the input

#5.Mutable or immutable
#a tuple is immutable as we cannot edit once entered elements inside a tuple
tu3[1]=11
print(tu3)


