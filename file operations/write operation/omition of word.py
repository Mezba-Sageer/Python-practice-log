f1=open('C:/Users/mezba/PycharmProjects/may_DA/file operations/write operation/sample file 3','r')
f2=open('omitted file','w')
for i in f1:
    if("apple" not in i): #here the word apple is checked thro line by line
        f2.write(i)
    #another method
    # if(i!="apple\n"): #in this method the entire file is checked at once
    #     f2.write(i)

#pep8(suggestion shown when there is error is pep8) - used for writing clean python code