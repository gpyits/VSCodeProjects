# Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

# Nota:

#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.
def valid_sudoku(board: list[list[str]]) -> bool:
    for row in board:
        row_numbers=[int(number) for number in row if number!='.']
        if len(row_numbers)!=len(set(row_numbers)): return False
        for column in row:
            column_numbers=[int(number) for number in board[row.index(column)][board.index(row)] if number!='.']
            if len(column_numbers)!=len(set(column_numbers)): return False
    for row in [0, 3, 6]:
        for column in [0, 3, 6]:
            box_numbers=[int(number) for number in [board[r][c] for r in range(row, row+3) for c in range(column, column+3)] if number!='.']
            if len(box_numbers)!=len(set(box_numbers)): return False
    return True

board = [["5","3",".",  ".","7",".",  ".",".","."],
         ["6",".",".",  "1","9","5",  ".",".","."],
         [".","9","8",  ".",".",".",  ".","6","."],

         ["8",".",".",  ".","6",".",  ".",".","3"],
         ["4",".",".",  "8",".","3",  ".",".","1"],
         ["7",".",".",  ".","2",".",  ".",".","6"],

         [".","6",".",  ".",".",".",  "2","8","."],
         [".",".",".",  "4","1","9",  ".",".","5"],
         [".",".",".",  ".","8",".",  ".","7","9"]]

print(valid_sudoku(board)) #True

board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board)) #False