# imports here
from random import seed, randint
from time import time

def main():
    # ask for user input
    user_input = int(input("Enter an integer: "))
    print(list_of_dice_rolls(user_input))

def list_of_dice_rolls(n):
    # seed rng
    seed(time())
    return [randint(1, 6) for _ in range(n)]

main()
