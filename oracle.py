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

    def update_to_bad(self):
        pass

    def backtrack(self, move):
        pass
    
    def no_good_options(self, board, player):
        columnRecommendations = self.get_recommendation(board, player)

        result = True
        for rec in columnRecommendations:
            if (rec.classification == ColumnClassification.WIN) or (rec.classification == ColumnClassification.MAYBE):
                result = False
                break
        return result
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
    BAD = 1 #MUY INDESEABLE
    MAYBE = 10 #MAYBE
    WIN = 100   #LA MEJOR OPCION

class SmartOracle(BaseOracle):
    def _get_column_recommendation(self, board, index, player):
        recommendation = super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.BAD
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
    

class MemoizingOracle(SmartOracle):

    def __init__(self) -> None:
        super().__init__()
        self._past_recommendations = {}
    
    def _make_key(self, board_code, player):

        return f'{board_code.as_code().raw_code}:@{player.char}'

    def get_recommendation(self, board, player):
        key = self._make_key(board.as_code(), player)
        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)

        return self._past_recommendations[key]

class LearningOracle(MemoizingOracle):
    
    
    def update_to_bad(self, move):
        key = self._make_key(move)
        recommendation = self.get_recommendation(SquareBoard.fromBoardCOde(move.board_code), move.player)
        recommendation[move.position] = ColumnRecommendation(move.position, ColumnClassification.BAD)
        self._past_recommendations[key] = recommendation
    
    def backtrack(self, list_of_moves):
        for move in list_of_moves:
            self.update_to_bad(move)

            board = SquareBoard.fromBoardCOde(move.board_code)
            if not self.no_good_options(board, move.player):
                break
        
