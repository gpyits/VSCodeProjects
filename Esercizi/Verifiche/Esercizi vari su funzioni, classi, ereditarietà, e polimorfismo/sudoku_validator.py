# Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

# Nota:

#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.
def valid_sudoku(board: list[list[str]]) -> bool:
    #try board[8] except IndexError, to prevent this calculation again
    #calculate segmented board
    if len(board)==9 or len(board==3): #check if this works logically
        for row in board:
            row_numbers=[int(number) for number in row if number!='.']
            #if len(row_numbers[i])!=len(set(row_numbers[i]))
            if [row_numbers[i] for i in range(len(row_numbers)-1) if row_numbers[i]==row_numbers[i+1]]!=[]: return False
            for column in row:
                column_numbers=[int(number) for number in board[row.index(column)][board.index(row)] if number!='.']
                if [column_numbers[i] for i in range(len(column_numbers)-1) if column_numbers[i]==column_numbers[i+1]]!=[]: return False
    else:
        #recursive call to validate segmented board and returning True
        pass

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
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

# # Controlla tutti i sottogruppi 3x3
# for box_row in range(0, 9, 3):
#     for box_col in range(0, 9, 3):
#         # Costruisce una lista degli elementi del sottogruppo 3x3 corrente
#         box = [
#             board[r][c]
#             for r in range(box_row, box_row + 3)
#             for c in range(box_col, box_col + 3)
#         ]