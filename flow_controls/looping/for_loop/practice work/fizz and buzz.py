#9.	**Print numbers from 1 to 100 replacing:
# Multiples of 3 with "Fizz"
# Multiples of 5 with "Buzz"
# Multiples of both with "FizzBuzz"**
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzBuzz",end=" ")
    elif(i%3==0):
        print("Fizz",end=" ")
    elif(i%5==0):
        print("Buzz",end=" ")
    else:
        print(i,end=" ")