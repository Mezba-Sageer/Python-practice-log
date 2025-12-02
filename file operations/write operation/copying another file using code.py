f1=open('C:/Users/mezba/PycharmProjects/may_DA/file operations/write operation/sample file.2','r')
f2=open('copied file','w')
for i in f1:
   f2.write(i)
#this program is used to copy all the contents within sample file 2.
# to a new file-"copied file" created using write operation
#here we create 2 reference 1 for read and another one for write
#for loop is used to get each sentence of the sample file
#and we write that content in 'i' to another file
