#Encryption question:
# Create a program that takes a number as input (e.g., 2) and an alphabet letter (either uppercase or lowercase).
# The output should be the letter that is the given number of positions ahead of the input letter in the alphabet.
# For example, if the input is 2 and the letter is 'A', the output should be 'C'. Similarly, for lowercase letters,
# if the input is 2 and the letter is 'a', the output should be 'c'.
num=int(input("Enter a number: "))
alpha=input("Enter an alphabet: ")
ascii_num = ord(alpha)
#ord() - this converts and alphabet to its ASCII number
out_put = ascii_num + num
print(chr(out_put))


