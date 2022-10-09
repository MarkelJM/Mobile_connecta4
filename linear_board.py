
from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import *

class LinearBoard():

    @classmethod
    def fromList(cls, list):
        board = cls()
        board._column = list
        return board

    def __init__(self):

        self._column = [None  for i in range(BOARD_LENGTH)]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._column == other._column
    
    def __hash__(self) :
        return hash(self._column)
            
    
    def add(self, char):
        """
        Juega en la primera posición disponible
        """
        # siempre y cunado no esté lleno...
        if not self.is_full():
            # buscamos la primera posición libre (None)
            i = self._column.index(None)
            # lo sustituimos por char
            self._column[i] = char

    def is_victory(self, char):
        return find_streak(self._column, char, VICTORY_STRIKE)
    
    def is_full(self):
        return self._column[-1] != None

   
    def is_tie(self, char1, char2):
        """no hay victoria ni de char1 ni char2"""

        return (self.is_victory('x') == False) and (self.is_victory('o') == False)