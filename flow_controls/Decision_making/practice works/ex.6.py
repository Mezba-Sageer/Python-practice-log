#26.	Accept marks of 3 subjects and print:
# •	"Pass" if all above 40,
# •	"Retest" if one below 40,
# •	"Fail" if more than one is below 40.
sub1=int(input("Enter the marks of sub1: "))
sub2=int(input("Enter the marks of sub2: "))
sub3=int(input("Enter the marks of sub3: "))
count=0
if(sub1<40):
    count+=1
if(sub2<40):
    count+=1
if(sub3<40):
    count+=1
if(count==0):
    print("pass")
elif(count==1):
    print("Retest")
else:
    print("Fail")
