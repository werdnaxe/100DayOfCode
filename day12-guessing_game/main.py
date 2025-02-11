from art import logo
import random as ran
import os

def guess_number(num_guesses, number):
   
    while num_guesses > 0:

        try:
            your_guess = int(input("Make a guess: "))
        except ValueError:
            print("You didn't guess a number. Guess again.")
            continue
            
        if num_guesses == 1:
            return your_guess
        
        if your_guess < number:
            print("Too low.\nGuess again.")
        elif your_guess > number:
            print("Too high.\nGuess again.")
        else:
            return your_guess

        num_guesses -= 1
        
        if num_guesses > 1:
            print(f"You have {num_guesses} attempts remaining.")
        else:
            print(f"You have {num_guesses} attempt remaining.")


        
in_game = True

while in_game:
    
    # Game setup
    os.system('clear')
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    
    num_guesses = 0
    
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
        print("You chose 'easy'. You have 10 attempts to guess the number.")
        num_guesses = 10
    else:
        print("You chose 'hard'. You have 5 attempts to guess the number.")
        num_guesses = 5

    # Game
    number = ran.randint(1,100)
    user_guess = guess_number(num_guesses, number)
    
    if user_guess != number:
        print(f"You did not guess the number. The number was {number}.")
    else:
        print(f"You got it! The number was {number}.")

    # Play again?
    if input("Would you like to play again. Type 'yes' or 'no': ").lower() != 'yes':
        in_game = False
        print("Thank you for playing the Number Guessing Game.")
