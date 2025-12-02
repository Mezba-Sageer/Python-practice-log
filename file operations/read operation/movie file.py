#1. ratings abv 4 : collect movies name, year, rating
#2. Below the year 2000 : collect movies name, year, duration
#3, count of movies released in each year
#4. release year above 2005 and rating above 4 name,year, rating
#5. movies starting with 'A' alphabet
f1=open("C:/Users/mezba/OneDrive/Desktop/weekly tasks/movies_cleaned_pandas.csv",'r')
dic={}
for i in f1:
    data=i.rstrip('\n').split(',')
    #q.1 - ratings abv 4
    # if(data[3]>'4'):
    #     print(data[1:4])

    #q.2 - below the year 2000
    # if(data[2]<'2000'):
    #     print(data[1],data[2],data[-1])

 #q.3- count of movies released in each year
#     if(data[2]not in dic):
#         dic[data[2]]=1
#     else:
#         dic[data[2]]+=1
# for k,v in dic.items():
#     print(k,":",v)

    #q.4 release year abv 2005 and rating above 4
    # if(data[2]>'2005' and data[3]>'4'):
    #     print(data[1:4])

    #q.5 movies starting with alphabet a
    if(data[1][0]=="A" or data[1][0]=="a"): #data[1]= access the movie name but
        # data[1][0] access the movie name's first index
        print(data[1])
    #q.5 another method:
    # for i in data[1]:
    #     if(i=='A'):
    #         print(data[1])
    #     break