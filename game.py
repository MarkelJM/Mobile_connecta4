import imp
import pyfiglet
from enum import Enum, auto
from match import Match
from player import Player
from square_board import SquareBoard

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()


class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGHT = auto()
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
    
    def print_logo(self):
        logo = pyfiglet.Figlet(font='stop')
        print((logo.renderText('Connecta')))

    def _configure_by_user(self):
        self.round_type = self._get_round_type()

        self.match = self._make_match()

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
        pass