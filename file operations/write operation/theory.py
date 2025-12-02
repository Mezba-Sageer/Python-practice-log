#write operation is used create an entire file from the scratch
#1. create file reference
f1=open('sample file','w') #sample file - is the name given to the new file you want to create using write.
f1.write('Luminar\n')
f1.write('Technolab\n')
#'\n' is used to print lines or else all the content added into a file is printed in a single line.