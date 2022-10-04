from enum import Enum, auto
from square_board import SquareBoard

class BaseOracle():
    def get_recommendation(self, board, player):
        """
        Returns a list of ColumnRecommendations
        """
        recommendations = []
        for i in range(len(board)):
            recommendations.append(
                self._get_column_recommendation(board, i, player))
        return recommendations

    def _get_column_recommendation(self, board, index, player):
        """
        Classifies a column as either FULL or MAYBE and returns an ColumnRecommendation
        """
        classification = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClassification.FULL

        return ColumnRecommendation(index, classification)
class ColumnRecommendation():
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    def __eq__(self, other):
        # si son de clases distintas, pues distintos
        if not isinstance(other, self.__class__):
            return False
        # sólo importa la clasificación
        else:
            return self.classification == other.classification
        
       

class ColumnClassification():
    FULL = auto()
    MAYBE = auto()