"""
    =========== Challenge 2 =============
    Take two inputs from the command line, then
    convert both to an int the first number will
    be the starting number, and the second will be
    the ending number. Create a loop that goes from
    the starting number to the ending number, and only
    prints the even numbers.
"""

x = 0 

check_value = int(input("How many even number can we find "))

while x < 10:
    if ((x % 2) == 0): # If the number is even
        print(x)

    else: # If the number is odd
        continue # Go to next iteration