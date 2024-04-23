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

#guesser game
def guesser(chosen_range=range_creator()):
    correct_number=random.randrange(chosen_range[0], chosen_range[1])
    guess=int(input('Guess the number: '))
    max_attempts=5 #3 attempts starter
    while max_attempts!=0:
        if guess==correct_number:
            print('\nWell done! You guessed it right!')
            return True
        #if guess is near the number
        elif guess in range(correct_number-5, correct_number+5):
            max_attempts-=1
            print('Wrong! Almost there!.\nAttempts remaining: {max_attempts}')
        #if guess is too low
        elif guess in range(chosen_range[0], correct_number-10):
            max_attempts-=1
            print('Wrong! Too low!\nAttempts remaining: {max_attempts}')
        #if guess is too high
        elif guess in range(correct_number+10, chosen_range[1]):
            max_attempts-=1
            print('Wrong! Too high!\nAttempts remaining: {max_attempts}')
    else:
        print('Ran out of attempts, better luck next time!')
        return False

guesser()