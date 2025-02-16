import random
import os

#RANDOM GAME KUR ME MINXI PATA RRYM

number= random. randint(1,10)
guess=input("Guess random number beetwen 1 through 10 ")
guess = int(guess)

if guess == number:
     print("You WON!")
else:print("YOU LOST")