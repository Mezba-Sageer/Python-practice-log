#q.1 print the fname,lname,age and ph no. of ppl whose age equal to 21
#q.2 print the following details of ppl working in chennai: fname,lname,age
#q.3 print the following details of ppl whose age is abv 23 and working in chennai: fname,lname,age,ph.no

f1=open("C:/Users/mezba/OneDrive/Desktop/weekly tasks/sample4.txt",'r')
for i in f1:
    data=i.rstrip('\n').split(',')
 #q.1   # if(data[3]=='21'):
        # print(data[1:5])
 #q.2   # if(data[5]=="Chennai"):
        #print(data[1:4])
 #q.3   # if(data[3]>'23' and data[5]=="Chennai"):
        #print(data[1:5])
