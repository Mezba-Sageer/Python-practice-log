f1=open('sample file 2', 'r')
dic={}
for i in f1: #1st iteration: first sentence is taken
    data=i.rstrip('\n').split(" ") #this step is used to split each word from each sentence in a paragraph.
    #bcz the variable data has all words in a sentence.
    for j in data: #used to go through each word in a sentence
      if j not in dic: #checks if the word in that sentence is present in dictionary
        dic[j]=1
      else:
        dic[j]+=1
print(dic)
