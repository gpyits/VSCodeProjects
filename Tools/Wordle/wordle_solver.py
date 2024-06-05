###HOW TO USE###
#Input the word with uppercase green letters in their positions and a dot in place of missing letters in this format ->  green_letters='.letter2..letter5' e.g. '.A..B'
#Input the word with uppercase yellow letters found in the current game in place of green letters dots in this format ->  yellow_letters='letter1letter2letter3' e.g. 'SDE'
import re
def wordle_solver(green_letters: list[tuple[str, int]], yellow_letters: str) -> list[str]:
    possible_answers=[]
    result=[]
    with open('Tools/Wordle/wordle_words_eng.txt', 'r') as f:
        lines=f.readlines()
        f.seek(0)
    letterset=[i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if i not in green_letters and i not in yellow_letters]
    letterset='[^ ]'.replace(' ', ''.join(i for i in letterset))
    for line in lines:
        word=re.findall(letterset, line.strip('\n'))
        new_word=re.findall(green_letters, ''.join(i for i in word))
        if new_word!=[]:
            possible_answers.append(word)
    return [''.join(i for i in r) for r in possible_answers]

print(wordle_solver('B....', 'AS'))