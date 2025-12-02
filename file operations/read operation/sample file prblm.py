f=open('sample file', 'r')
#this is the file reference
#where 'sample file' is the name of the file, when the file is within the package where the operations are performed
#only mention the file name
#'r' is the operation to be performed
for i in f: #for loop is used to get each sentence within the file
    print(i)

f1=open('/practise works/sample file 2', 'r')
for i in f1:
    print(i)
#for reading file in other packages and directories we have to copy the path of that file
#steps to follow
#1. right click the file name
#2. copy the reference
#3. select absolute path
#4. and paste it within the quotes as argument 1

#the problem with copying the path is that the slashes of the path is backward slash - this gives an error
#so change the slashes to forward slashes to avoid error-(windows prblm)


#/n is the reason y output has long spaces between each output- '/n' this is new line