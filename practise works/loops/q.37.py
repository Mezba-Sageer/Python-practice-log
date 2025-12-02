#037
#Ask the user to enter their name and display each letter in their name on a separate line.

name=input("enter your name: ")
index=0
#while loop method
while(index<len(name)):
    print(name[index])
    index+=1


#for loop method
for i in range(len(name)):
    print(name[i])
