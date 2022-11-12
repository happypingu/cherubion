from cherubion_game import interface
from cherubion_game.start_game import start_game
from cherubion_game.load_game import load_game

PLAY = "New Game".lower()
LOAD = "Load Game".lower()
QUIT = "Quit".lower()
COMMANDS = [PLAY, LOAD, QUIT]

def play():
    while True:
        interface.print_("Welcome to Cherubion!\n")

        interface.print_(f'> New Game')
        interface.print_(f'> Load Game')
        interface.print_(f'> Quit')
        command = interface.get_command(COMMANDS)

        # TODO: add load_game() function to load saves
        if command == PLAY:
            start_game()

        if command == LOAD:
            load_game()

        if command == QUIT:
            break
