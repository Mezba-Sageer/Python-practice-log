#1. if age above 50: fname,lname,age,prof
#2. if age range 25-40: fname,lname,age,prof
#3. if work in india : fname,lname,age,prof
#4. if work in India and age abv 50 : fname,lname,age
#5. if work in UK : fname,lname,age,prof
#6. doctor prof: fname,lname, age
#7. doctor prof and age below 40: fname,lname, age
#8. prof - pilot : fname,lname, age
#9. each prof count
#10. each location count
f1=open("C:/Users/mezba/OneDrive/Desktop/weekly tasks/python/customer1.txt",'r')
dic={}
for i in f1:
    data=i.rstrip('\n').split(',')
    print(data)
#q.1   #print("age abv 50")
    # if(data[3]>'50'):
    #     print(data[1:5])
#q.2   # print("age range of 25-40")
    # if(data[3]>='25' and data[3]<='40'):
    #     print(data[1:5])
#q.3   #print("work in india")
    # if(data[-1]=="india"):
    #     print(data[1:5])
#q.4   #print("work in india and age abv 50")
    # if(data[-1]=="india" and data[3]>'50'):
    #     print(data[1:4])
#q.5   #print("work in UK")
    # if(data[-1]=="uk"):
    #     print(data[1:5])
#q.6   #print("Doctor")
    # if(data[4]=="Doctor"):
    #     print(data[1:4])
#q.7   #print("doctor prof and age abv 40")
    # if(data[4]=="Doctor" and data[3]>'40'):
    #     print(data[1:4])
#q.8   # print("pilot prof")
    # if(data[4]=="Pilot"):
    #     print(data[1:4])
#q.9   #print("Profession count")
#     profession=data[4]
#     if(profession not in dic):
#         dic[profession]=1
#     else:
#         dic[profession]+=1
# print(dic)
#q.10   #print("location count")
#     location=data[-1] #this method is assigning the index to another variable
#     if(location not in dic):
#       dic[location]=1
#     else:
#       dic[location]+=1
# print(dic)
#q.10 #another method
# print("Location count")
#     if(data[-1] not in dic):
#         dic[data[-1]]=1 #this method is without assigning the index to another variable
#     else:
#         dic[data[-1]]+=1
# print(dic)
# for k,v in dic.items():
#     #items() is used only in dictionary in order to get both key and the value printed in separate lines.
#     print(k,":",v)
