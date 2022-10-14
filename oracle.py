from copy import deepcopy
from enum import Enum, auto
from square_board import SquareBoard
from settings import BOARD_LENGTH

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
        
    def __hash__(self) :
        return hash(self.index, self.classification)

class ColumnClassification():
    FULL =  -1 #IMPOSIBLE
    LOSE = 1 #MUY INDESEABLE
    MAYBE = 10 #MAYBE
    WIN = 100   #LA MEJOR OPCION

class SmartOracle(BaseOracle):
    def _get_column_recommendation(self, board, index, player):
        recommendation = super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.LOSE
        return recommendation

    def _is_losing_move(self, board, index, player):
        tmp = self._play_on_tmp_board(board, index, player)
        will_lose = False
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(tmp, i, player.opponent):
                will_lose = True
                break
        return will_lose

    
    def _is_winning_move(self, board, index, player):
        tmp = self._play_on_tmp_board(board, index, player)
        return tmp.is_victory(player.char)
    
    def _play_on_tmp_board(self, board, index, player):

        tmp = deepcopy(board)

        tmp.add(player.char, index)

        return tmp