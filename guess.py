#Roisin Anglim 19.03.18 
#Guess Game 

#Adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

#Randomly generates a number between the range set
from random import randint
target = randint(1, 100) 
#This sets a limit as the guess is between 1-100 and will never reach 101
guess = 101 

print("Guess a number between 1 to 100: ") 
  
while guess != target:  
    guess = int(input("Guess a number: "))
    if guess == target: 
          print("Well Done")  
    elif guess < target: 
          print("too low")  
    else: 
          print("too high")
