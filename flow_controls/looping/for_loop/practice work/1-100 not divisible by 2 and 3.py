#26.Print numbers from 1 to 100 that are not divisible by 2 or 3.
for i in range(1,101):
    if i%2==0 or i%3==0:
        continue
    else:
        print(i)