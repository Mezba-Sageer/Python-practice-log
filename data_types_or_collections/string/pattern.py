#print the pattern
# p
# py
# pyt
# pyth
# pytho
# python
mystring="python"
for i in range(0,len(mystring)+1):
    for j in range(i):
         print(mystring[j],end=" ")
    print()


#another method
x=0
for i in mystring: #when i is not used can use '_' in place of that
    x+=1 #when i=p x=1 #i=y x=2
    print(mystring[0:x]) #0:1-> output:p #0:2 -> output:py




