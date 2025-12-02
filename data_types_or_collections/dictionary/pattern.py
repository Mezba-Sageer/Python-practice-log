#using dictionary print the first recursive character in a word - first repetitive character in the word
pattern='ABCGDHSAAABDHCS'
dic={}
for i in pattern: #iterates thro each character in the word
    if(i not in dic):
        dic[i]=1
    else:
        print(i)
        break
