# Assignment 3 - Problem 2: Guess the Number Game with 3 Attempts

import random

print("I'm thinking of a number between 1 and 10!")

# generate random number
num = random.randint(1, 10)

# accumulator variable
guess_count = 0

# ask user for guess
guess = int(input("What's your guess? "))

# create boolean variable
guessed = False

if guessed == False:
    if guess == num:
        print("You got it!")
        print("The secret number was", num)
        guessed = True
    elif guess > num:
        print("Too high, try again")
    else:
        print("Too low, try again")
    guess_count += 1

if guessed == False:
    guess = int(input("What's your guess? "))
    if guess == num:
        print("You got it!")
        print("The secret number was", num)
        guessed = True
    elif guess > num:
        print("Too high, try again")
    else:
        print("Too low, try again")
    guess_count += 1
    
if guessed == False:
    guess = int(input("What's your guess? "))
    if guess == num:
        print("You got it!")
        print("The secret number was", num)
        guessed = True
    guess_count += 1

if guessed == True:
    print("It took you", guess_count, "tries to guess the number.")
if guess_count >= 3:
    print("The secret number was", num)
    print("You didn't guess the number")
