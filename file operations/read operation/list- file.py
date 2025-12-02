lst=[]
f=open('C:/Users/mezba/PycharmProjects/may_DA/Identifiers/numbers', 'r')
for i in f:
        #lst.append(i) #this command gives the output as string with '/n' at the end of each element in the list
        lst.append(int(i.rstrip('\n')))
        #the output is by default in string that is why we add int to convert that into integer value
        #rstip(\n) is used to remove the '\n' in the final output on the right side
        #because if that is not used there will be \n in all output
print(lst)
print(sum(lst))

#rstrip()- is used to remove unnecessary characters from the right side of an element
#syntax: eg:
data="hello/n"
data1=data.rstrip("o/n")
print(data1)

#rstrip()-removes values from the right side of the word, removes the characters we've entered
#to remove within the function
#lstrip()- is used to remove unnecessary characters from the left side of an element
#by default new line is represented as - '\n'
