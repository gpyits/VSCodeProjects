# Board positions are:
#   '1'  '2'  '3'
#   '4'  '5'  '6'
#   '7'  '8'  '9'
class Board:
    def __init__(self) -> None:
        self.board: list[str]=['', '', '',
                               '', '', '',
                               '', '', '']
    def printBoard(self) -> None:
        print(self.board[0], '|', self.board[1], '|', self.board[2],'\n',\
              '---------','\n',\
              self.board[3], '|', self.board[4], '|', self.board[5],'\n',\
              '---------','\n',\
              self.board[6], '|', self.board[7], '|', self.board[8],'\n')
    def tic(self, position: int=int(input('Choose X position: ').strip('\n'))) -> None:
        if not self.board[position]:
            self.board[position-1]='X'
            self.printBoard()
        else:
            return self.tic(position=int(input(f'Error: Position {position} already occupied. Choose X position: ').strip('\n')))
    def tac(self, position: int=int(input('Choose O position: ').strip('\n'))) -> None:
        if not self.board[position]: 
            self.board[position-1]='O'
            self.printBoard()
        else:
            return self.tic(position=int(input(f'Error: Position {position} already occupied. Choose O position: ').strip('\n')))
    def toe(self) -> bool:
        board: list[str]=[[self.board[0], self.board[1], self.board[2]],
                          [self.board[3], self.board[4], self.board[5]],
                          [self.board[6], self.board[7], self.board[8]]]
        if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
            self.printBoard()
            print(f'\nCongratulations player {row[0]}! You won!')
            return True
        else:
            for row in board:
                if row[0]==row[1]==row[2]:
                    self.printBoard()
                    print(f'\nCongratulations player {row[0]}! You won!')
                    return True
            for column in range(3):
                if board[column][0]==board[column][1]==board[column][2]:
                    print(f'\nCongratulations player {row[0]}! You won!')
                    return True
        if '' not in self.board:
            self.printBoard()
            print('\nDraw')
            return True
        return False
    def tictactoe(self) -> None:
        self.printBoard()
        while True:
            self.tic()
            self.tac()
            if self.toe():
                return

Board().tictactoe()