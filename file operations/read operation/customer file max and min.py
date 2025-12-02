f1=open("C:/Users/mezba/OneDrive/Desktop/weekly tasks/customer1.txt",'r')
dic={}
for i in f1:
    data=i.rstrip('\n').split(',')
    #print the max age of ppl in each profession
#     prof=data[4]
#     age=data[3]
#     if(prof not in dic):
#         dic[prof]=age
#     else:
#         old_age=dic[prof]
#         if(age>old_age):
#             dic[prof]=age
# for k,v in dic.items():
#     print(k,":",v)
    
    #print the minimum age of ppl in each location
    location=data[-1]
    new_age=data[3]
    if(location not in dic):
        dic[location]=new_age
    else:
        old_age=dic[location]
        if(new_age<old_age):
            dic[location]=new_age
for k,v in dic.items():
    print(k,":",v)
