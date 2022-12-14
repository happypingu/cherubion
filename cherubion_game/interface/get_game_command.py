from .get_command import get_command
from .built_in_methods import print_
from .loadnsave import save_game
from ..player import races

_STATS = "stats"
_SAVE = "save"

_BASE_COMMANDS = [
    _STATS,
    _SAVE
]

def get_game_command(player, room, additional_commands=[]):
    commands = additional_commands.copy()
    commands.extend(_BASE_COMMANDS)

    while True:
        print_()
        command = get_command(commands, True)

        if command in additional_commands:
            return command

        if command == _STATS:
            race = races.Hero(player.ourrace)
            print(race)
        
        if command == _SAVE:
            save_game(races.Hero(player.ourrace))