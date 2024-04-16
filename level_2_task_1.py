#LEVEL 2 TASK 1

#Write a Python program that generates a
#random number between 1 and 100. The
#user should then try to guess the number.

import random
n = random.randrange(1,100)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")
