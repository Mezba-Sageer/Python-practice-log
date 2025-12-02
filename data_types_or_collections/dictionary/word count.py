#important question for interview
#word count problem using dictionary - is checking how much times each word within a sentence or paragraph repeats.
line='cat is cat being cat dog is a dog dog bird being a bird'
#the above sentence is a line data rather than a word data so in order to take the count of each word in the sentence
#we have to convert it into a word by word data so inorder to do that we use a split()
data=line.split(' ')
#inside the split() we pass the condition to split i.e we split the sentence using spaces
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
#in for loop if the range is given i iterates the index number
#if the list name is given in the for loop it checks the data presents within the list
