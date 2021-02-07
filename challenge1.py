
import random
number = random.randint (1, 100)

while true:

    guess = int(input("How many chances do you need to choose the right number? It is between 0 and 100, what is it?\n"))
    if guess = number:
        print ("WOW! You got this one!")
        break
    elif guess < 1:
    print("Jeez!!! Read the question! >:( ")
    elif guess > 100: 
    print("Seriously ?!?!")