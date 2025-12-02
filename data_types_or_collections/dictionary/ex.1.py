#using list comprehension print key of elements with value above 4500
dic={'car':3500,'bus':8000,'minibus':5000,'bike':500,'cycle':500}
f1=[i.upper() for i in dic if(dic[i]>4500)]
print(f1)
