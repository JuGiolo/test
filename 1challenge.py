
"""
    =========== Challenge 1 =============
    The code below generates a random number
    make a game that loops and takes user input 
    at the command line. The input is the user's
    guess at what the number is. Taking their input
    you should print either: 'too high', 'too low' or
    'Correct guess'.
    For example let's assume the number is 4 a sample
    output of the game would look like this:
        >> Enter Guess: 2
        Too Low
        >> Enter Guess: 5
        Too High
        >> Enter Guess: 4
        Correct Guess

import random
number = random.randint() # Generates a random number

"""


import random
number = random.randint (1, 100)

while True:

    guess = int(input("How many chances do you need to choose the right number? It is between 0 and 100, what is it?\n"))
    if guess == number:
        print ("WOW! You got this one!")
        break
    elif guess < 1:
        print("Jeez!!! Read the question! >:( ")
    elif guess > 100: 
        print("Seriously ?!?!")
    elif guess > number: 
        print("Ops... Too high!")
    elif guess < number: 
        print("Guessed WRONG! Guess higher")