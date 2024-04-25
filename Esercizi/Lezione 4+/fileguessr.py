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
    #correct guess
    if guess==correct_number:
        print('Congratulations! You guessed it!')
        return True
    #ran out of attempts
    elif max_attempts==0:
        print('Sorry, you ran out of attempts. Better luck next time.')
    #incorrect guess
    else:
        print(f'Too low!\nAttempts remaining: {max_attempts}' if guess<correct_number else f'Too high!\nAttempts remaining: {max_attempts}')
        #recursive call
        guess_core(max_attempts-1, int(input(f'Take another guess, attempts remaining: {max_attempts-1}\n')), correct_number)

#guesser game, attempt handling
def number_guesser(max_attempts, chosen_range=range_creator()):
    correct_number=random.randrange(chosen_range[0], chosen_range[1])
    guess_core(max_attempts, int(input('Take a guess: ')), correct_number)
    
number_guesser(5)