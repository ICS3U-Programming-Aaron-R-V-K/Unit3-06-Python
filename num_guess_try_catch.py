# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 27 2025
# This program is a guessing number from 0-9 using try catch
# It uses if else statement and try catch to avoid run time errors

import random


def main():
    # Generate the random number from 1 to 10
    random_number = random.randint(0, 9)

    # Get user guess for the random number
    guess_number = input("Guess a random number from 0 to 9: ")

    # Try catch to check if the user number is valid
    try:
        guess_number_integer = int(guess_number)

        # If statement for the right answer
        if random_number == guess_number:
            print("Your are correct")

        # Else statement for any other answer that is not the correct number
        else:
            print("You are wrong, the correct answer was: {} ".format(random_number))
        
    # Except statement if the answer is not an integer 
    except Exception:
        print(f"That was not an integer")

    # Final statement at the end of the program no matter the answer
    finally:
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
