import random, time
#BLACK '\033[30m'
#YELLOW '\033[33m'
#GREEN '\033[32m'
#RESET '\033[0m'

#stats handler
def user_stats(has_won: bool, time: float, reset=False) -> None:
    with open('Tools/Wordle/wordle_stats.txt', 'r') as f:
        lines=f.readlines()
        f.seek(0)
    profile_name, games_won, games_lost, winrate, current_streak, max_streak, total_time, won_last_game=lines[0][9:-1], int(lines[1][11:-1]), int(lines[2][12:-1]), int(lines[3][9:-2]), int(lines[4][20:-1]), int(lines[5][16:-1]), float(lines[6][20: -6]), bool(lines[7])
    games_won+=1 if has_won else 0 #if player won
    games_lost+=1 if not has_won else 0 #if player lost
    winrate=round(games_won/(games_won+games_lost)*100) #calculates winrate
    current_streak=current_streak+1 if has_won&won_last_game else 0 #calculates win streak
    max_streak=current_streak if current_streak>max_streak else max_streak #updates maximum streak if the current streak is bigger
    time/=3600 #seconds to hour conversion
    total_time+=time #adds time spent
    won_last_game=has_won #updates last game win for streak purposes
    #updates file
    with open('Tools/Wordle/wordle_stats.txt', 'w') as f:
        if not reset:
            lines=[
                f'Profile: {profile_name}\n', 
                f'Games won: {games_won}\n', 
                f'Games lost: {games_lost}\n', 
                f'Winrate: {winrate}%\n', 
                f'Current win streak: {current_streak}\n', 
                f'Max win streak: {max_streak}\n',
                f'Time spent playing: {round(total_time, 2)}hours\n',
                str(won_last_game)
                ]
        else:
            lines=['Profile: Gabriel\n', 'Games won: 0\n', 'Games lost: 0\n', 'Winrate: 0%\n', 'Current win streak: 0\n', 'Max win streak: 0\n', 'Time spent playing: 0hours\n', 'False']
        for line in lines:
            f.write(line)

#prints user statistics
def print_user_stats() -> None:
    with open('Tools/Wordle/wordle_stats.txt', 'r') as f:
        for line in f.readlines()[:-1]:
            print(line.strip('\n'))

#prints letters keyboard
def print_help(help: list[str]) -> None:
    print(*help[:10], '\n ', *help[10:19], '\n  ', *help[19:], '\n')

#prints game matrix for user interface
def print_game(game: list[str]) -> None:
    print('\n### WORDLE ###\nHints: type y for yellow, g for green\n')
    if len(game)!=1:
        for word in game[:-1]:
            print(*word)
    for letter in game[-1]:
        time.sleep(1)
        print(letter, end=' ', flush=True)
    print()

#adds properly colored word to the game matrix
def word_adder(correct_word: str, guess: str, game: list[str], found_letters: dict[str:list]) -> None:
    #counts letters in correct word
    correct_count={}
    for letter in correct_word:
        if letter in correct_count: correct_count[letter]+=1
        else: correct_count[letter]=1
    #creates empty word
    color_guess=[]
    for i in range((len(guess))):
        #if letter is green
        if guess[i]==correct_word[i]:
            correct_count[guess[i]]-=1
            color_guess+=[f'\033[32m{guess[i]}\033[0m'] #append
            try: found_letters['g'][i][0]=color_guess[-1]
            except IndexError: print(found_letters['g'], i, correct_word)
            found_letters['g'][i][1]-=1
            found_letters['y'][i][0]=f'\033[33m{color_guess[-1]}\033[0m'
            found_letters['y'][i][1]-=1
            #help keyboard logic
            if guess[i] in help:
                help[help.index(guess[i])]=f'\033[32m{guess[i]}\033[0m'
            elif f'\033[33m{guess[i]}\033[0m' in help:
                help[help.index(f'\033[33m{guess[i]}\033[0m')]=f'\033[32m{guess[i]}\033[0m'
            elif f'\033[30m{guess[i]}\033[0m' in help:
                help[help.index(f'\033[30m{guess[i]}\033[0m')]=f'\033[32m{guess[i]}\033[0m'
        #if letter is black
        else:
            color_guess+=[f'\033[30m{guess[i]}\033[0m']
            found_letters['b'].append(color_guess[-1])
            #help keyboard logic
            if guess[i] in help and f'\033[32m{guess[i]}\033[0m' not in help and f'\033[33m{guess[i]}\033[0m' not in help:
                help[help.index(guess[i])]=f'\033[30m{guess[i]}\033[0m'
    #if letter is yellow
    for i in range(len(color_guess)):
        if guess[i] in correct_word and color_guess[i]==f'\033[30m{guess[i]}\033[0m':
            if correct_count[guess[i]]>0:
                color_guess[i]=f'\033[33m{guess[i]}\033[0m'
                correct_count[guess[i]]-=1
                found_letters['y'][shuffled.index(guess[i])][0]=f'\033[30m{guess[i]}\033[0m'
                found_letters['y'][shuffled.index(guess[i])][1]-=1
                #help keyboard logic
                if guess[i] in help:
                    help[help.index(guess[i])]=f'\033[33m{guess[i]}\033[0m'
                elif f'\033[30m{guess[i]}\033[0m' in help:
                    help[help.index(f'\033[30m{guess[i]}\033[0m')]=f'\033[33m{guess[i]}\033[0m'
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
game=[] #game matrix
attempts=6 #attempts
correct_word=random.choice(file.readlines()).strip('\n') #chooses word
#hints
found_letters={'b':[], 'y':[], 'g':[]}
for i in correct_word: found_letters['g'].append(['\033[30m#\033[0m', 1]), found_letters['y'].append(['#', 1])
#yellow hints logic
shuffled=list(correct_word)
random.shuffle(shuffled)
shuffled=''.join(i for i in shuffled)
#keyboard help
help=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
#starting banner
print('\n### WORDLE ###\nHints: type y for yellow, g for green\n')
#game difficulty
easy=input('Choose difficulty: [easy/else] ').lower()
#starts timer for current game
timer_start=time.time()
while attempts>0:
    #makes sure input is a real, length-5 word 
    while True:
        file.seek(0)
        guess=input('Guess word: ').upper().strip()
        if len(guess)==5 and guess+'\n' in file.readlines():
            #difficulty catcher
            if easy=='easy':
                choice=0
                for letter in guess:
                    if f'\033[30m{letter}\033[0m' in help:
                        choice=input(f'Word {guess} contains black letters, do you want to proceed anyways? [y/n]').lower()
                        break
                if choice=='y' or choice==0: break
            else: break
        #yellow letter hint
        elif guess=='Y':
            for letter in shuffled:
                if [f'\033[33m{letter}\033[0m', 1] not in [i for i in found_letters['y']]:
                    if found_letters['y'][shuffled.index(letter)][1]>0:
                        found_letters['y'][shuffled.index(letter)][0]=f'\033[33m{letter}\033[0m'
                        found_letters['y'][shuffled.index(letter)][1]-=1
                        #help keyboard logic
                        if letter in help:
                            help[help.index(letter)]=f'\033[33m{letter}\033[0m'
                        elif f'\033[30m{letter}\033[0m' in help:
                            help[help.index(f'\033[30m{letter}\033[0m')]=f'\033[33m{letter}\033[0m'
                        print(f'Hint: \033[33m{letter}\033[0m')
                        break
        #green letter hint
        elif guess=='G':
            for letter in range(len(correct_word)):
                if f'\033[32m{correct_word[letter]}\033[0m' not in [i[0] for i in found_letters['g']]:
                    if found_letters['g'][letter][1]>0:
                        found_letters['g'][letter][0]=f'\033[32m{correct_word[letter]}\033[0m'
                        found_letters['g'][letter][1]-=1
                        #help keyboard logic
                        if correct_word[letter] in help:
                            help[help.index(correct_word[letter])]=f'\033[32m{correct_word[letter]}\033[0m'
                        elif f'\033[33m{correct_word[letter]}\033[0m' in help:
                            help[help.index(f'\033[33m{correct_word[letter]}\033[0m')]=f'\033[32m{correct_word[letter]}\033[0m'
                        elif f'\033[30m{correct_word[letter]}\033[0m' in help:
                            help[help.index(f'\033[30m{correct_word[letter]}\033[0m')]=f'\033[32m{correct_word[letter]}\033[0m'
                        print('Hint:', ''.join(i[0] for i in found_letters['g']), sep=' ')
                        break
        else:
            print(f'Invalid word "{guess}"')
    #adds word to the game
    word_adder(correct_word, guess, game, found_letters)
    print_game(game)
    print(), print_help(help)
    #if user wins the game
    if guess==correct_word:
        time.sleep(0.5)
        print(f'\nCongratulations! You won!\nAttempts: {6-attempts}')
        user_stats(True, time.time()-timer_start)
        print_user_stats()
        break
    #if guess isn't the right word
    else:
        attempts-=1
        if attempts==0:
            time.sleep(0.5)
            print(f'\nYou lost. Correct word was {correct_word}')
            user_stats(False, time.time()-timer_start)
            print_user_stats()