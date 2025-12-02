# 2. Password CheckerLogical AND
# • Length ≥ 8 characters.
# • Contains at least one digit

password=input("Enter the password: ")
count=0
index=0
while(index<len(password)):
#len()- checks the length of a string
#while loop starts from the first character and the range stop at the length of the password
#(used to check each character)
    if(password[index]>='0' and password[index]<='9'):
        #if password[0](password's first character) or any character is between 0 and 9
        count+=1 #counts the no.of numbers in the password
    index+=1 #increment statement of the index no. to check the nxt character
if(len(password)>=8 and count>=1):
    print("password is valid")
else:
    print("password is invalid")
