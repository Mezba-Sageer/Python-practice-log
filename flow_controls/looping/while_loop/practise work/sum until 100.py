#22.	Accept numbers until the sum exceeds 100; print how many entries it took.
sum=0
count=0
while(sum<=100):
    num = int(input("Enter a number: "))
    sum+=num
    count+=1

print("no.of enteries: ",count)

