from tkinter.messagebox import NO
from settings import BOARD_LENGTH

class LinearBoard():

    def __init__(self):

        self._column = [None  for i in range(BOARD_LENGTH)]
        #self._row = [None  for i in range(BOARD_LENGTH)]
    
    def add(self, char):
        #siempre y cuando no este lleno
        if not self.is_full():
            # buscamos la primera posicion libre(None)
        
            i = self._column.index(None)
            # lo sustituimos por char
            self._column[i] = char

    def is_victory(self, char):
        
        def horizonal_victory():
            pass
        def vertical_victory():
            pass
        def diagonal_victory():
            pass
    
    def is_full(self):
        return self._column[-1] != None

   
    def is_tie(self, char1, char2):
        """no hay victoria ni de char1 ni char2"""

        return(self.is_victory('x') == False) and (self.is_victory('o') == False)