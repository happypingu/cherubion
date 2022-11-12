from text_based_rpg import interface
from text_based_rpg.start_game import start_game
from text_based_rpg.load_game import load_game

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
