
#csv- files is comma separated values
f1=open('C:/Users/mezba/OneDrive/Desktop/weekly tasks/temperature file.unknown','r')
dic={}
for i in f1:
    data=i.rstrip('\n').split(',')
    district=data[0] #this step is done bcz the list only has 2 elements district and value this is the index of dist.
    temp=data[1] #index of temperature
    if(district not in dic):
        dic[district]=temp
    else:
        old = dic[district] #this step is used update the value
        # if district is already present in the dictionary we assign the value that is currently present in the dic
        #to another variable, and the temperature that is currently being checked is in temp.
        if(temp>old):
            dic[district]=temp
for k,v in dic.items(): #to print output in key value pair format.
    print(k,":",v)
