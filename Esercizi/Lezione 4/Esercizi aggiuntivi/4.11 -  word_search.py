# Create a function that solves a word search puzzle.
# Provide a 2D grid representing the puzzle and a list of words to find.
# Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
# Output the locations of the found words within the grid.

#neatly prints word matrix
def print_matrix(matrix: list[str]) -> None:
    for row in matrix:
        print(' '.join(i for i in row))

#assigns positions to each letter
def get_positions(matrix: list[str]) -> list[list[tuple[str, tuple[int, int]]]]:
    new_matrix=[[letter for letter in word] for word in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j]=(new_matrix[i][j], (j, i))
    return new_matrix

#casts matrix diagonals retaining original position
def matrix_diagonal(matrix: list[list[tuple[str, tuple[int, int]]]]) -> list[list[tuple[str, tuple[int, int]]]]:
    new_matrix=[]
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[0])):
            try:
                new_matrix[i].append(matrix[i+j][j])
            except IndexError:
                continue
    return new_matrix

#casts matrix upwards retaining original position
def matrix_updown(matrix: list[list[tuple[str, tuple[int, int]]]]) -> list[list[tuple[str, tuple[int, int]]]]:
    new_matrix=[]
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(matrix[j][i])
    return new_matrix

#searches the matrix for words, in all directions
def search(matrix: list[str, tuple], words) -> None:
    for word in words:
        for row in matrix:
            if word in ''.join(i[0] for i in row) or word in ''.join(i[0] for i in row)[::-1]:
                lenght=0
                print(f'Found word {word} at positions:')
                if word in ''.join(i[0] for i in row)[::-1]:
                    for letter in row[::-1]:
                        if lenght==len(word):
                            break
                        print(f'{letter[0]}: {letter[1]}')
                        lenght+=1
                else:
                    for letter in row:
                        if lenght==len(word):
                            break
                        print(f'{letter[0]}: {letter[1]}')
                        lenght+=1

#handles printing the matrix and searching words, while not changing original matrix
def word_search(matrix: list[str], words: list) -> None:
    print_matrix(matrix)
    new_matrix=get_positions(matrix)
    search(new_matrix, words)
    search(matrix_updown(new_matrix), words)
    search(matrix_diagonal(new_matrix), words)
    search(matrix_diagonal(new_matrix[::-1]), words)

word_search(['HWULV', 'COURT', 'TNIOP', 'ATJOO', 'MLLAB'], ['BALL', 'MATCH', 'COURT', 'POINT'])