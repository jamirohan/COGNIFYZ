#LEVEL 2 TASK 2

#Number Guesser

import random
x=random.randint(20,100)
guess=0
print("You only have 3 chances")
i=6
while i>0:
    guess=int(input("Enter a number:"))
    if(guess>x):
        print("Oops!choose a lower value")
    elif(guess<x):
        print("Oops!choose a higher value")
    else:
        print("Yes!you guess it right,Woww")
    i=i-1
print("Sorry no chances remain")
