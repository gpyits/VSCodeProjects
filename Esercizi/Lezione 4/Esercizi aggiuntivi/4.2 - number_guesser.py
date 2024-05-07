'''
Create a function that generates a random number within a range specified by the user.
Prompt the user to guess the number within a specified maximum number of attempts.
Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''
import random

#guesser game, no arguments needed unless you want to set things up for yourself
def number_guesser(max_attempts=5, correct_number=random.randrange(int(input('Insert first number: ')), int(input('Insert second number: '))+1), guess=int(input('Take a guess: '))):
    #correct guess
    if guess==correct_number:
        print('Congratulations! You guessed it!')
        return True
    #ran out of attempts
    elif max_attempts==0:
        print('Sorry, you ran out of attempts. Better luck next time.')
        return False
    #incorrect guess
    else:
        print(f'Too low!' if guess<correct_number else f'Too high!')
        #recursive call
        return number_guesser(max_attempts-1, correct_number, int(input(f'Take another guess, attempts remaining: {max_attempts-1}\n')))

number_guesser()