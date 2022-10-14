
import pyfiglet
from enum import Enum, auto
from match import Match
from oracle import SmartOracle, BaseOracle
from player import HumanPlayer, Player
from square_board import SquareBoard
from list_utils import reverse_matrix
from beautifultable import BeautifulTable
from settings import BOARD_LENGTH

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()


class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
class Game:
    
    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player('Chip'), Player('Chop'))) :
        self.round_type = round_type
        self.match = match

        self.board = SquareBoard()

    def start(self):
        #imprimo nombre o logo del juego
        self.print_logo()
        #configuro la partida
        self._configure_by_user()
        # arrancar bucle principal
        self._start_game_loop()
    
    def print_logo(self):
        logo = pyfiglet.Figlet(font='stop')
        print((logo.renderText('Connecta')))
    
    def _start_game_loop(self):
        while True:
            current_player = self.match.next_player
            current_player.play(self.board)
            self.display_move(current_player)
            self.display_board()
            if self._is_game_over():
                self.display_results()
                break
    
    def display_move(self, player):
        print(f'\n {player.name} ({player.char}) has moved in column {player.last_move}')


    def display_board(self):
        matrix = self.board.as_matrix()
        matrix = reverse_matrix(matrix)

        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]

        print (bt)

    def display_results(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f'\n{winner, name} ({winner.char}) wins!!!')
        else:
            print(f'\n A tie between {self.match.get_player("x").name} (x) and {self.match.get_player("o").name} (o)')


    def _is_game_over(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            return True
        elif self.board.is_full():
            return True
        else:
            return False

    

    def _configure_by_user(self):
        self.round_type = self._get_round_type()
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()
        self.match = self._make_match()
    
    def _get_difficulty_level(self):
        print("""elige tu oponente:
        1) Bender: nivel bajo
        2)T-800: Medio
        3) T-100: Dificil
        """)
        while True:
            response = input('elige 1,2 o 3:').strip()
            if response ==1:
                level = DifficultyLevel.LOW
                break
            elif response == 2:
                level = DifficultyLevel.MEDIUM
                break
            else:
                level = DifficultyLevel.HIGH
                break
        return level

    def _get_round_type():
          
        print("""
        Select the type of round:
        1) Computer vs Computer
        2) Computer vs Human
        """)

        response = ""
        while response != "1" or response != "2":
            response = input("escribe 1 o 2")
        if response == 1:
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN

    def _make_match(self):
        
        _levels = {DifficultyLevel.LOW : BaseOracle(),
        DifficultyLevel.MEDIUM : SmartOracle(), DifficultyLevel.HIGH : SmartOracle()}
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player1 = Player('T-X', oracle=SmartOracle())
            player2 = Player('T-1000', oracle=SmartOracle())
        else:
            player1 = Player('T-800', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name=input("escribe tu nombre"))

        return Match(player1, player2)