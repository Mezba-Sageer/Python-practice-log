#Bank domain:
# Design a program for the bank domain where there are unlimited denominations of coins (e.g., 1, 2, 5, 10).
# The program takes an amount as input (e.g., 7) and
# calculates the minimum number of coins needed to sum up to that amount.
# For instance, if the input is 7, the output should be 2,
# as the minimum number of coins to make 7 is 2 (using one 5-coin and one 2-coin).


amount=int(input("Enter a number: "))
count=0

count+=amount//10
amount= amount%10

count+=amount//5
amount=amount%5

count+=amount//2
amount=amount%2

count+=amount//1
amount=amount%1

print(count)