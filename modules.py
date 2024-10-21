"""https://wiki.python.org/moin/PythonBooks
"""
import random

def main():

    guess = int(input("Please guess a number from 1 to 100 : "))
    random_value = random.randint(1,100)
    difference = abs(random_value)

    while not guess == random_value :
        guess_again = int(input("Please guess again : "))
        guess = guess_again
        print(difference)
        print(f"The random value is {random_value}")
    else : 
        print("Your answer is correct")

    


main()
