#print the details of ppl working in bigdata profession and also their age should be above 29
#details to be printed: fname,lname,age
lst=[["mezba","sageer",31,"bigdata","jobless"],["jude ","alron",32,"python"],
     ["afthab","rahman",21,"bigdata"],["farsee","azies",29,"python"]]
for i in lst:
    if(i[3]=="bigdata" and i[2]>=29):
        print(i[0:3])