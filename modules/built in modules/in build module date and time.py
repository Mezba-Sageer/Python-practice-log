import datetime
from time import strftime #strftime is to import string values
x=datetime.datetime.now() #doubt
print("Current date and time is: ",x)
print(x.strftime("%a")) #%a - give half of a word
print(x.strftime("%A")) #A- output gives whole string value
#strf is used to change the value of time into string

