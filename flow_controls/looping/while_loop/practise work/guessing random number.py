#41.	Generate a random number (1–100), ask user to guess it until correct, show attempts.
import random
num=random.randint(1,100)
attempt=1
while(True):
    guess=int(input("Enter your guess: "))
    if(guess==num):
        print("You've guessed it in",attempt,"attempts")
        break
    elif(guess>num):
        print("Your guess is too high")
        attempt+=1
    elif(guess<num):
        print("your guess is too low")
        attempt+=1