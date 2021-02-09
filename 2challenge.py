"""
    =========== Challenge 2 =============
    Take two inputs from the command line, then
    convert both to an int the first number will
    be the starting number, and the second will be
    the ending number. Create a loop that goes from
    the starting number to the ending number, and only
    prints the even numbers.
"""

x, y = map(int, input("Add two values to check all the even numbers between the numbers given:\n").split())

for num in range(x, y):
    if num % 2 == 0:
        print(num)