###HOW TO USE###
#Input the green letters along with their index position found in the current game in this format green_letters=[('letter1', position), ('letter2', position)...]
#Input the yellow letters found in the current game in this format yellow_letters='letter1letter2letter3...'

def wordle_solver(green_letters: list[tuple[str, int]], yellow_letters: str) -> list[str]:
    possible_answers=[]
    word=list('#####')
    with open('Tools/Wordle/wordle_stats.txt', 'r') as f:
        lines=f.readlines()
        f.seek(0)
    for i in green_letters:
        for letter, position in i:
            word[position]=letter
    word=''.join(i for i in word)
    return word