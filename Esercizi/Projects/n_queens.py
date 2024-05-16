#find every position in which n number of queens in an nxn grid don't touch each other
import itertools

def chessboard_combinations(chessboard):
    pass

def n_queens(queen_number: int) -> list[dict]:
    pass

print(n_queens(8))





# def n_queens(queen_number: int) -> list[dict]:
#     def print_chessboard(chessboard):
#         for row in chessboard:
#             print(row)
#     def cast_diagonals(chessboard, row, column):
#         if chessboard[row][column]=='Q':
#                 #replaces 'E' with 'X' on the right and left
#                 for r in range(len(chessboard[row])):
#                     if chessboard[row][r]!='X' or chessboard[row][r]!='Q':
#                         chessboard[row][r]!='X'
#                     else: return False
#                 #same thing but up and down
                    
#     chessboard=[['Q' for i in range(queen_number)]]+[['E'for i in range(queen_number)]for i in range(queen_number-1)]
#     calculated_queen_positions, possible_queen_positions=[], #[every possible combination of queen on the board]
#     for row in range(len(chessboard)):
#         for column in range(len(chessboard)):
#             if cast_diagonals(chessboard, row, column):
                

#     print_chessboard(chessboard)