#q.8 Write a Python function that processes a list of numbers,
# using continue to skip processing for numbers less than 5.
def numbers():
    for i in range(1,21):
        if(i<5):
            continue
        print(i)
numbers()