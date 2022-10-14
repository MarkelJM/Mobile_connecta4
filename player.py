from random import random
from settings import  BOARD_LENGTH
from oracle import BaseOracle, ColumnClassification, ColumnRecommendation

class Player():
    """
    Juega en un tablero después de preguntar a un oráculo
    """

    def __init__(self, name,  char = None, opponent = None,   oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent
        self.last_move = None

    @property
    def opponent(self):
        return self._opponent

    @property.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other.opponent = self



    def play(self, board):
        """
        Elige la mejor columna de aquellas que recomienda el oráculo
        """
        #Preegunto al oráculo
        (best, recommendations) = self.ask_oracle(board)
        # Juego en la mejor
        self._play_on(board, best.index)

    def _play_on(self,board, position):
        #juega en la pos
        board.add(self.char, position)
        self.last_move = position

    def _ask_oracle(self, board):
        """
        Pregunta al oráculo y devulve la mejor opcion
        """
        # obtenemos las recommendaciones
        recommendations = self._oracle.get_recommendation(board, self)
        # seleccionamos la mejor
        best = self._choose(recommendations)

    def _choose(self, recommendations):
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recommendations))

        valid = sorted(valid, key=lambda x: x.classification.value, reverse=True)

        if all_same(valid):
            return random.choice(valid)

        else:
            return valid[0]
        

class HumanPlayer(Player):

    def __init__(self, name, char=None) :
        super().__init__(name, char)

    def _ask_oracle(self, board):
        """pido al humano que es mi oraculo"""
        while True:
            raw = input('Select a cloumn: ')
            if self._is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)


    def _is_non_full_column(board, num):
        return not board._columns[num].is_full()

    def _is_within_column_range(board, num):
        return num >= 0 and num < len(board)
    
    def _is_int(aString):
        try:
            num = int(aString)
            return True
        except:
            return False