
from oracle import BaseOracle, ColumnClassification, ColumnRecommendation

class Player():
    """
    Juega en un tablero después de preguntar a un oráculo
    """

    def __init__(self, name,  char = None, opponent = None,   oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        """
        Elige la mejor columna de aquellas que recomienda el oráculo
        """
        recommendations = self._oracle.get_recommendation(board, self)

        best = self._choose(recommendations)

        board.add(self.char, best.index)

    def _choose(self, recommendations):
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recommendations))

        return valid[0]