#Accept a string and check if its length is more than 5 and it ends with 'z'.

# str1=input("Enter a word: ").lower()
# if((len(str1)>5) and (str1[-1]=="z")):
#     print("conditions are met")
# else:
#     print("conditions not met")
#

str1=input("Enter a string: ")
if((len(str1)>5) & (str1[-1]=='z')):
    print("Conditions ok")
else:
    print("no")