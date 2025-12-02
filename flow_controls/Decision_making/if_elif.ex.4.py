#read 4 subject marks
#find total marks of 4 sub
#print total mark
#180 - a+
#160-179 - a
#140-159 - b+
#120-139 - b
#100-119 - c+
#below 100- fail
sub1=int(input("enter marks of subject 1: "))
sub2=int(input("enter marks of subject 2: "))
sub3=int(input("enter marks of subject 3: "))
sub4=int(input("enter marks of subject 4: "))
sum=sub1+sub2+sub3+sub4
print("Total marks is",sum)
if(sum>=180):
    print("your grade is A+")
elif(sum>=160)&(sum<=179): #160<=sum<=179
    print("Your grade is A")
elif(sum>=140)&(sum<=159):
    print("your grade is B+")
elif(sum>=120)&(sum<=139):
    print("your grade is B")
elif(sum>=100)&(sum<=119):
    print("your grade is c+")
else:
    print("fail")
