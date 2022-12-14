from cherubion_game import interface
from .rooms.village import room as village
from .player import races
from .interface import loadnsave
from cherubion_game.interface.loadnsave import load_game

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
            player = races.create_race()
            village.enter(player)

        if command == LOAD:
            load_game(races.Hero(player.ourrace))

        if command == QUIT:
            break