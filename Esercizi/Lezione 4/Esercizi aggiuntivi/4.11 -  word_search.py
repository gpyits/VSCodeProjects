# Create a function that solves a word search puzzle.
# Provide a 2D grid representing the puzzle and a list of words to find.
# Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
# Output the locations of the found words within the grid.

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(i for i in row))

def matrix_diagonal(matrix, found_words):
    pass

def matrix_updown(matrix):
    new_matrix=[]
    for i in range(len(matrix)):
        new_row=''
        for j in range(len(matrix)):
            new_row+=matrix[j][i]
        new_matrix.append(new_row)
    return new_matrix

def search(matrix, words, found_words):
    for word in words:
        position={}
        for row in matrix:
            if word in row or word in row[::-1]:
                position[word]=[]
                for letter in word:
                    position[word].append((letter, (matrix.index(row), row.index(letter))))
        found_words.append(position) if position!={} else None

def word_search(matrix: list[str], words: list) -> list[dict]:    
    found_words=[]
    search(matrix, words, found_words)
    search(matrix_updown(matrix), words, found_words)
    return found_words

print(word_search(['HWULV', 'COURT', 'TNIOP', 'ATJOO', 'MLLAB'], ['BALL', 'MATCH', 'COURT', 'POINT']))
#print_matrix(['HWULV', 'COURT', 'TNIOP', 'ATJOO', 'MLLAB'])