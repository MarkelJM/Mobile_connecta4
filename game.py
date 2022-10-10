import pyfiglet
class Game:
    
    
    def start(self):
        #imprimo nombre o logo del juego
        self.print_logo()
        #configuro la partida
        # arrancar bucle principal
    
    def print_logo(self):
        logo = pyfiglet.Figlet(font='stop')
        print((logo.renderText('Connecta')))