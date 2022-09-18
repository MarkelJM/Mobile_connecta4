from settings import BOARD_LENGTH

class LinearBoard():

    def __init__(self):

        self._column = [None  for i in range(BOARD_LENGTH)]
    
    def add(self, char):
        pass
        # buscamos la primera posicion libre(None)
        i = self._column.index(None)
        # lo sustituimos por char
        self._column[i] = char

    def is_victory(self, char):
        return False
    
    def is_full(self):
        pass

   
    def is_tie(self, char1, char2):
        return False