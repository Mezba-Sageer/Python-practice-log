#properties
#1.how to define:
#empty dictionary is created using- '{}'
#dictionary is a key-value pair

#eg for key-value pair:
#ID:1919 - here key is ID, value is 1919
#name: MEZ - here key is name, value is mez
#age:22 - age is key, 22 is value
#prof:student prof is key, student is value


#syntax of dictionary creation :
dic={'age':21,'name':'Mezba','qualification':'bachelors','salary':30000}
print(dic)
#here the key should be passed inside the ' ' (quotes)

#2.heterogenous data
#a dictionary supports heterogenous data

#3.insertion order
#the insertion order of dictionary is preserved - since the output is in the same order as input

#4.duplicate supporting:
dic1={'age':21,'name':'Mezba','qualification':'bachelors','salary':30000,'salary':45000}
print(dic1)
#dictionary doesn't support duplicate "key"
#since python is a line by line executer the last entered value of the salary is returned as output
#but it supports duplicate value i.e 2 different key having the same value is printed as output

#5.Mutable or Immutable
#dictionary is mutable



