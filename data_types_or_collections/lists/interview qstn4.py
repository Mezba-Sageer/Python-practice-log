#pass few elements into a list and print only the prime numbers from that list.
lst=[12,34,13,5,3,56,87,44,32,24,76]
for i in lst:
    if(i<2):
        continue #continue is used to skip those values
    j=2
    count=0
    while(j<i):
      if(i%j==0):
        count+=1
      j+=1
    if(count==0):
      print(i)