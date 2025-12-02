#continue statement
#continue skips the value mentioned in the condition,
# in this the output doesn't print 10 as continue skips the value
#continue statement skips over the current iteration and continues to the next iteration based on its condition
for i in range(20):
    if(i==10):
        continue
    print(i)
