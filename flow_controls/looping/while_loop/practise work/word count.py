#28.	Accept a sentence and count how many words it has using basic loop (without split).
str1=input("Enter a sentence: ")
count=1 #count starts from 1 bcz spaces after 1 word is counted
i=0
while(i<len(str1)): #it runs from 1st index of the sentence till the last
    if(str1[i]==" "): #this condition checks for spaces as words are separated by spaces
        count+=1
    i+=1
print("no of words: ",count)