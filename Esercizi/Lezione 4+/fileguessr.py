'''
Create a function that generates a random number within a range specified by the user.
Prompt the user to guess the number within a specified maximum number of attempts.
Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''
import random

#creates a tuple simulating a range given user input
def range_creator():
    return (int(input('Insert first number: ')), int(input('Insert second number: '))+1)

#guesser game core
def guess_core(max_attempts, guess, correct_number):
    if guess==correct_number:
        print('Congratulations! You guessed it!')
        return True
    elif guess!=correct_number:
        print(f'Too low!\nAttempts remaining: {max_attempts}' if guess<correct_number else f'Too high!\nAttempts remaining: {max_attempts}')
        guess_core(max_attempts-1, int(input('Take another guess, attempts remaining: #--->>>>continue here')), correct_number)

#guesser game, attempt handling
def number_guesser(max_attempts, chosen_range=range_creator()):
    correct_number=random.randrange(chosen_range[0], chosen_range[1])
    guess_core(max_attempts, int(input('Take a guess: ')), correct_number)
    
number_guesser(5)