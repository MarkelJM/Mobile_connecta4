from square_board import SquareBoard
from oracle import BaseOracle
from player import Player

def test_play():
    """
    comprobamos que se juega en la primera columna disponible
    """
    before = SquareBoard.fromList([None, None, None, None],['x', 'o', 'x', 'o'],  ['x','o', 'x', 'o'],['x', None, None, None] )
    after = SquareBoard.fromList([None, None, None, None],['x', 'o', 'x', 'o'],  ['x','o', 'x', 'o'],['x', None, None, None] )
    
    player = Player('Chip', 'x', oracle = BaseOracle())

    player.play(before)
    assert before == after

def test_is_int():
    a = Player()
    """cuando impor _is_int from player me salta error y aqui no me lo reconoce, pero como lo tengo ahora
    me dice missing value
    """
    assert a._is_int('42')
    assert a._is_int('0')
    assert a._is_int('-32')
    assert a._is_int('  32   ')
    assert a._is_int('hola') == False
    assert a._is_int('') == False
    assert a._is_int('3.14') == False
    


"""
def test_valid_column():
    board = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])

    assert _is_within_column_range(board, 0)
    assert _is_within_column_range(board, 1)
    assert _is_within_column_range(board, 2)
    assert _is_within_column_range(board, 3)
    assert _is_within_column_range(board, 5) == False
    assert _is_within_column_range(board, -10) == False
    assert _is_within_column_range(board, 10) == False



def test_is_non_full_column():

    board = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])
                                  
    assert _is_non_full_column(board,0)
    assert _is_non_full_column(board, 1) == False
    assert _is_non_full_column(board,2) == False
    assert _is_non_full_column(board, 3) 
"""


