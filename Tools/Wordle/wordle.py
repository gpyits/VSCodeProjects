import random, time
#BLACK '\033[30m'
#YELLOW '\033[33m'
#GREEN '\033[32m'
#RESET '\033[0m'

'''things to add:
Add hints:
 -level 1 hints: YELLOW letter
 -level 2 hints: GREEN letter
Add help:
 -level 1 help: prints a keyboard list with all the black, yellow and green letters
 -level 2 help: says word is invalid when there are known black letters in it
Add statistics:
 Create a file statistics.txt with wins, losses and winrate%. Add time spent to win/lose at the end of the game (and for each word? maybe not)
'''

#prints game matrix for user interface
def print_game(game: list[str]) -> None:
    print('\n### WORDLE ###\n')
    if len(game)!=1:
        for word in game[:-1]:
            print(*word)
    for letter in game[-1]:
        time.sleep(1)
        print(letter, end=' ', flush=True)
    print()

#adds properly colored word to the game matrix
def word_adder(correct_word: str, guess: str, game: list[str]) -> None:
    #counts letters in correct word
    correct_count={}
    for letter in correct_word:
        if letter in correct_count:
            correct_count[letter]+=1
        else:
            correct_count[letter]=1
    #creates empty word
    color_guess=[]
    for i in range((len(guess))):
        #if letter is green
        if guess[i]==correct_word[i]:
            correct_count[guess[i]]-=1
            color_guess+=[f'\033[32m{guess[i]}\033[0m']
        #if letter is black
        else:
            color_guess+=[f'\033[30m{guess[i]}\033[0m']
    #if letter is yellow
    for i in range(len(color_guess)):
        if guess[i] in correct_word and color_guess[i]==f'\033[30m{guess[i]}\033[0m':
            print(True)
            if correct_count[guess[i]]>0:
                color_guess[i]=f'\033[33m{guess[i]}\033[0m'
                correct_count[guess[i]]-=1
            else:
                continue
    game.append(color_guess)

#language selection snippet
wordle_language=input('Select this wordle game\'s language: [en/it] ').lower().strip()
if wordle_language=='en':
    file=open('Tools/Wordle/wordle_words_eng.txt', 'r')
elif wordle_language=='it':
    file=open('Tools/Wordle/wordle_words_ita.txt', 'r')
else:
    raise NameError(f'invalid language "{wordle_language}"')

#game starter
game=[]
attempts=6
correct_word=random.choice(file.readlines()).strip('\n')
print('\n### WORDLE ###\n')
while attempts>0:
    #is this really necessary?
    if attempts==0:
        time.sleep(0.5)
        print(f'\nYou lost. Correct word was {correct_word}')
    #makes sure input is a real, length-5 word
    while True: 
        file.seek(0)
        guess=input('Guess word: ').upper().strip()
        if len(guess)==5 and guess+'\n' in file.readlines():
            break
        else:
            print(f'Invalid word "{guess}"')
    #adds word to the game
    word_adder(correct_word, guess, game)
    print_game(game)
    #if user wins the game
    if guess==correct_word:
        time.sleep(0.5)
        print(f'\nCongratulations! You won!\nAttempts: {6-attempts}')
        break
    #if guess isn't the right word
    else:
        attempts-=1