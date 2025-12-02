#20.For a given string, print all substrings of length 3.
str1="Hello world" #len of word 11
for i in range(len(str1)-2): #runs till 8th index
#len of str1 is used to loop thro the string value using index value
    print(str1[i:i+3])
#this prints the substring with character length as three
#for hello world first i=0 at h then prints hel
#i=1 at e prints ell
#i=8 rld
#when i=9 it prints ld
#when i=10 it prints d
#now this doesn't meet the condition that is why we give -2
#and for loop starts from 0 even if len starts from 1 