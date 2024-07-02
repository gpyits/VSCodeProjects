###HOW TO USE###
#Input the word with uppercase green letters in their positions and a dot in place of missing letters in this format ->  green_letters='.letter2..letter5' e.g. '.A..B'
#Input all the uppercase yellow letters found in the current game in this format ->  yellow_letters='letter1letter2letter3' e.g. 'SDE'
#Input all the uppercase black letters found in the current game in this format ->  black_letters='letter1letter2letter3' e.g. 'ANGOPDH'
import re

def wordle_solver(green_letters: list[tuple[str, int]], yellow_letters: str, black_letters: str) -> list[str]:
    with open('Games/Wordle/wordle_words_eng.txt', 'r') as f:
        lines=f.readlines()
    yellow_count={k:yellow_letters.count(k) for k in set(yellow_letters)}
    if not green_letters and yellow_letters:
        return sorted([word.strip('\n') for word in lines if all(letter in word for letter in yellow_letters) and all(yellow_count[letter]=={k:word.count(k) for k in set(word)}[letter] for letter in yellow_letters) and all(letter not in word for letter in black_letters)])
    elif not green_letters and not yellow_letters and black_letters:
        return [word.strip('\n') for word in lines if all(letter not in word for letter in black_letters)]
    else:
        result=list(set(word for word in [word [0] for word in [re.findall(green_letters, line.strip('\n')) for line in lines] if word] if all(letter in word for letter in yellow_letters)))
        return sorted([word for word in result if all(yellow_count[letter]=={k:word.count(k) for k in set(word)}[letter] for letter in yellow_letters) and all(letter not in word for letter in black_letters)])

print(wordle_solver('..L..', 'AIN', 'CHRMOUTBES'))