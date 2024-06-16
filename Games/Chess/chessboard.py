from exceptions import *
from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class ChessBoard:
    def __init__(self) -> None:
        self.eaten_pieces: dict[str:list[Piece]]={'white':[], 'black':[]}
        self.board={'a7':0, 'b7':0, 'c7':0, 'd7':0, 'e7':0, 'f7':0, 'g7':0, 'h7':0,
                    'a7':0, 'b7':0, 'c7':0, 'd7':0, 'e7':0, 'f7':0, 'g7':0, 'h7':0,
                    'a6':0, 'b6':0, 'c6':0, 'd6':0, 'e6':0, 'f6':0, 'g6':0, 'h6':0,
                    'a5':0, 'b5':0, 'c5':0, 'd5':0, 'e5':0, 'f5':0, 'g5':0, 'h5':0,
                    'a4':0, 'b4':0, 'c4':0, 'd4':0, 'e4':0, 'f4':0, 'g4':0, 'h4':0,
                    'a3':0, 'b3':0, 'c3':0, 'd3':0, 'e3':0, 'f3':0, 'g3':0, 'h3':0,
                    'a2':0, 'b2':0, 'c2':0, 'd2':0, 'e2':0, 'f2':0, 'g2':0, 'h2':0,
                    'a1':0, 'b1':0, 'c1':0, 'd1':0, 'e1':0, 'f1':0, 'g1':0, 'h1':0}
    def setBoard(self, white_pieces: list[Piece], black_pieces: list[Piece]) -> None:
        self.white_pieces: list[Piece]=white_pieces
        self.black_pieces: list[Piece]=black_pieces
        for piece in white_pieces:
            pass ######
    def move(self, piece: Piece, position: str) -> None:
        try:
            if piece in self.white_pieces or self.black_pieces:
                if self.board[position]:
                    old_piece: Piece=self.board[position]
                    self.eaten_pieces[old_piece.color].append(old_piece)
                self.board[position]=piece
            else:
                raise InvalidPieceError('Error: piece is not on the chessboard')
        except KeyError:
            raise InvalidPositionError('Error: position doesn\'t exist')