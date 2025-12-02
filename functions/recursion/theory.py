#factorial (!)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#eg:5
#5*factorial(4)-> this is calling the function again
#5*(4*factorial(4-1))
#5*4*3*factorial(2-1)......

#fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(15))