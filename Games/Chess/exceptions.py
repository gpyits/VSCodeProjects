class InvalidPositionError(Exception):
    '''Raises error when user tries to move a valid piece to an invalid position'''
    pass
class InvalidPieceError(Exception):
    '''Raises error when user tries to move an invalid piece'''
    pass