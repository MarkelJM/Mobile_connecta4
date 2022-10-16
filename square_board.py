
from linear_board import LinearBoard
from list_utils import displace_matrix, replace_all_in_matrix, reverse_matrix, transpose
from string_utils import _explode_list_of_strings
from settings import BOARD_LENGTH


class SquareBoard():
    """
    Representa un tablero cuadrado
    """
    @classmethod
    def fromList(cls, list_of_lis):
        """
        transformar una lista de listas en una lisr de LinearBoard
        """
        board = cls()
        board._columns = map(lambda element: LinearBoard.fromList(element), list_of_lis)
        return board
    
    @classmethod
    def fromBoardCOde(cls, Board_code):
        return cls.fromBoardRawCode(Board_code.raw_code)

    @classmethod
    def fromBoardRawCode(cls. board_raw_code):
        list_of_strings = board_raw_code.split("|")
        matrix = _explode_list_of_strings(list_of_strings)
        matrix = replace_all_in_matrix(matrix, '.', None)
        
        return cls.fromList(matrix)


    def __init__(self) :
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def __repr__(self) :
        return f'{self.__class__}:{self._columns}'
    
    def __len__(self):
        return len(self._columns)

    def __eq__(self, other) :
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._columns == other._columns
        
    def __hash__(self) :
        return hash(self._columns)
        

    def is_full(self):
        """
        True si todos los LinearBoard están llenos
        """

        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    def as_code(self):
        return BoardCode(self)

    def as_matrix(self):
        """
        Devuelve una representacion en formato de matriz, lista de listas
        """
        return list(map(lambda x: x._column, self._columns))
    
    def add(self, char, column):
        self._columns[column].add(char)

    # Detectar victoria
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)
    
    
    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        # Transponemos _columns
        transp = transpose(self.as_matrix())
        # Creamos un tablero temporal con esa matriz transpuesta
        tmp = SquareBoard.fromList(transp)

        # comprobamos si tiene una victoria temporal
        return tmp._any_vertical_victory(char)

        
    
    def _any_rising_victory(self, char):
        #obtener las columnas
        m = self.as_matrix()
    
        # las invertimos
        rm = reverse_matrix(m)
        # creamos tablero temporal con esa matriz
        tmp = SquareBoard.fromList(rm)
        # devolvemos si tiene una victoria descendente
        return tmp._any_sinking_victory(char)
    
    def _any_sinking_victory(self,char):
        m = self.as_matrix()
        d = displace_matrix(m)
        tmp = SquareBoard.fromList(d)
        return tmp._any_horizontal_victory(char)

    # DUNDERS
    def __repr__(self) :
         return f'{self.__class__} : {self._columns}'

class BoardCode:
    def __init__(self, board) :
        self._raw_code = collapse_matrix(board.as_matrix())
    
    @property
    def raw_code(self):
        return self._raw_code

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False

        else:
            return self.raw_code == other.raw_code

    def __hash__(self) -> int:
        return hash(self.raw_code)

    def __repr__(self):
        return f'{self.__class__}: {self.raw_code}'