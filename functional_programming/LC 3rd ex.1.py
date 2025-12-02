#in 1-50 range print the following:
#1-15 - small
#16-35 - medium
#above 35 - large with element
lst=[(i,'small') if 1<=i<=15 else (i,'medium') if 16<=i<=35 else (i,'large') for i in range(1,51)]
print(lst)
