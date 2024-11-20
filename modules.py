"""https://wiki.python.org/moin/PythonBooks
Python books that worth to check 
"""

import random

# Define main fucntion
def main():
    try:
        guess = ""
        number = random.randint(1,100)
        #print('This is a random number :', number)
        while guess != number:
            guess = int(input("Please guess a number (1-100): "))
            if guess == number:
                # Stop the program if condition is met 
                print(f"You guessed right , random number was : {number}")
                break
            difference = abs(guess)-abs(number)
            difference = abs(difference)
            #print(difference)
            # Give hints about how close the guess was 
            if difference <=5:
                print("Very Hot")
            elif difference >5 and difference <16:
                print("Hot")
            elif difference >15 and difference <26:
                print("Cool")
            elif difference >25:
                print("Cold")
    except ValueError :
        # No ValueError shown in the terminal and instead writes this message
        print("Wrong Value")


main()
