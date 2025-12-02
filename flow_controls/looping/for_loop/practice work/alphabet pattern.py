#11.	Generate a pattern of right-aligned triangle using letters:
#     A
#    AB
#   ABC
#  ABCD
# ABCDE
#the letters are being printed using the ASCII code : i.e.
#for capital A-Z : 65 to 90
#for small a-z: 97 to 123
for i in range(1,6):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i): #this loop starts from 0, if i=1 #i=2
        print(chr(65+j),end=" ") #j=0 chr(65+0)-> A #j=0 chr(65+0)->A j=1 chr(65+1)->B
    print()