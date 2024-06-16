from abc import ABC, abstractmethod
from chessboard import ChessBoard

#Piece class
#takes name and color
#canMove checks if self can move according to their rule 
class Piece(ABC):
    def __init__(self, name: str, color: str) -> None:
        self.name: str=name
        self.color: str=color
    @abstractmethod
    def canMove(self, board: ChessBoard, position: str) -> bool:
        pass
    @abstractmethod
    def move(self, board: ChessBoard, position: str) -> None:
        pass

class Pawn(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass